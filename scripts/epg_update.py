#!/usr/bin/env python3
"""epg_update.py — build EPG_Astro_Malaysia.xml.gz from upstream sources.

Runs in GitHub Actions (no VPS). Downloads AqFad2811/epg + epgshare01,
merges, filters to channel ids referenced by MY_TV_Full.m3u, writes
EPG_Astro_Malaysia.xml + .gz next to this script's repo root.

Sources:
  astro, singapore (required) + epg, sooka, unifitv, rtmklik, shareMY, shareSG (optional)
"""
import gzip
import io
import os
import re
import sys
import tarfile
import urllib.request
import xml.etree.ElementTree as ET

UA = "hermes-agent/epg-update"
BASE = "https://raw.githubusercontent.com/AqFad2811/epg/master/compressed"
REQUIRED = ["astro", "singapore"]
OPTIONAL = ["epg", "sooka", "unifitv", "rtmklik", "shareMY", "shareSG"]


def fetch(name: str, url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=180) as r:
        return r.read()


def extract(gz_bytes: bytes):
    """aqfad ships tar.gz (single xml inside); epgshare ships plain gzip."""
    try:
        with tarfile.open(fileobj=io.BytesIO(gz_bytes), mode="r:gz") as tf:
            for m in tf.getmembers():
                if m.isfile():
                    return tf.extractfile(m).read()
    except tarfile.TarError:
        pass
    return gzip.decompress(gz_bytes)


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(here)  # repo root
    work = "/tmp/epg_src"
    os.makedirs(work, exist_ok=True)

    srcs = {}
    for name in REQUIRED:
        url = f"{BASE}/{name}.xml.gz"
        try:
            srcs[name] = extract(fetch(name, url))
        except Exception as e:
            print(f"FATAL: {name} failed: {e}")
            return 1
    for name in OPTIONAL:
        if name in ("shareMY", "shareSG"):
            url = f"https://epgshare01.online/epgshare01/epg_ripper_{name[5:]}1.xml.gz"
        else:
            url = f"{BASE}/{name}.xml.gz"
        try:
            srcs[name] = extract(fetch(name, url))
        except Exception as e:
            print(f"WARN: {name} failed (optional): {e}")

    root = ET.fromstring(srcs["astro"])
    chs = root.findall("channel")
    progs = root.findall("programme")
    cids = {c.get("id") for c in chs}
    orphans = {p.get("channel") for p in progs} - cids
    assert root.tag == "tv" and len(chs) >= 100 and len(progs) >= 10000 and not orphans, "astro validation failed"
    print(f"ASTRO OK: {len(chs)}ch {len(progs)}prog")

    sg = ET.fromstring(srcs["singapore"])
    schs, sprogs = sg.findall("channel"), sg.findall("programme")
    assert len(schs) >= 5 and len(sprogs) >= 300, "sg validation failed"
    REN = {"Ch 5": "Channel5", "Ch 8": "Channel8", "Ch U": "ChannelU"}
    rid = lambda x: REN.get(x, x)
    keep = {rid(c.get("id")) for c in schs} - cids
    nch = 0
    for c in schs:
        if rid(c.get("id")) in keep:
            c.set("id", rid(c.get("id"))); root.append(c); nch += 1
    npr = 0
    for p in sprogs:
        if rid(p.get("channel")) in keep:
            p.set("channel", rid(p.get("channel"))); root.append(p); npr += 1
    print(f"MERGED sg: +{nch}ch +{npr}prog")

    m3u = open(os.path.join(root_dir, "MY_TV_Full.m3u"), encoding="utf-8").read()
    m3u_ids = set(re.findall(r'tvg-id="([^"]+)"', m3u)) - {""}
    done = {c.get("id") for c in root.findall("channel")}
    for name in ["epg", "sooka", "unifitv", "rtmklik"]:
        if name not in srcs:
            continue
        t = ET.fromstring(srcs[name])
        has_prog = {p.get("channel") for p in t.findall("programme")}
        addset = ({c.get("id") for c in t.findall("channel")} & m3u_ids & has_prog) - done
        npr = 0
        for c in t.findall("channel"):
            if c.get("id") in addset:
                root.append(c)
        for p in t.findall("programme"):
            if p.get("channel") in addset:
                root.append(p); npr += 1
        done |= addset
        print(f"EXTRA {name}: +{len(addset)}ch +{npr}prog")

    all_ids = {c.get("id") for c in root.findall("channel")}
    all_refs = {p.get("channel") for p in root.findall("programme")}
    assert not (all_refs - all_ids), f"orphans: {all_refs - all_ids}"
    missing = m3u_ids - all_ids
    print(f"m3u ids without EPG: {len(missing)} -> {sorted(missing)}")

    data = ET.tostring(root, encoding="utf-8", xml_declaration=True)
    with open(os.path.join(root_dir, "EPG_Astro_Malaysia.xml"), "wb") as f:
        f.write(data)
    with open(os.path.join(root_dir, "EPG_Astro_Malaysia.xml.gz"), "wb") as f:
        with gzip.GzipFile(fileobj=f, mode="wb", compresslevel=9, mtime=0) as gz:
            gz.write(data)
    print(f"published: ch={len(all_ids)} prog={len(root.findall('programme'))}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
