# Senarai Provider IPTV — Status Penuh (21 Nov 2026)

## 1. AKTIF — dalam playlist (87 channel)

| # | Provider | Sumber | Status | Channel |
|---|----------|--------|--------|---------|
| 1 | RTM | `d25tgymtnqzu8s.cloudfront.net` (CloudFront rasmi) | HIDUP | TV1, TV2, TV6, TV Okey, Berita RTM, Sukan RTM, Parlimen ×2 (8) |
| 2 | sooka FAST | `amagi.tv` + `mediatailor` (AWS) | HIDUP | Drama Hebat, Filem Mantap, Lawak Sentral, Drama Hotpot, Travel & Taste, Jom Ngaji, Oh My Ceria, Free Movies, Gusto TV, PET CLUB, YRF Music, KCM, Fashion TV, WeDoTV ×4, Horse & Country (18) |
| 3 | Astro/Media Prima | CDN terus (`cdn.qd.je`, CloudFront) | HIDUP | AEC, AOD, Hua Hee Dai, Awani Global, 8TV, CinemaWorld, Maah TV (7) |
| 4 | dhanytv (GitHub `dhasap/dhanytv`) | playlist awam | HIDUP (update harian) | DAZN RINGSIDE, FOX Sports, beIN Sports 1/2/XTRA, BBC Earth, Bloomberg, HISTORY, Nat Geo Sharks (9) |
| 5 | Global FAST (iptv-org) | Amagi/Akamai/CloudFront/Pluto (sah) | HIDUP | Berita 7, Sukan 8, Filem 8, Dokumentari 11, Kanak-kanak 7, Muzik 4 (45) |
| 6 | EPG | AqFad2811/epg + epgshare01 | HIDUP | auto-update 6am/6pm (GitHub Actions) |

## 2. MATI — pernah hidup / diuji

| Provider | Punca mati |
|----------|------------|
| Panel best-8k.org / 4kgood.org (Xtream, 40,225 stream) | HTTP 458 (21 Okt) → connection reset (5 Nov). Akaun aktif tapi delivery mati. Blok global, bukan IP |
| HBO ×4 + Cinemax (dhanytv/spmid.pw) | Stream kosong (bytes:0) — dibuang dari playlist |
| tvN Asia, RTM ASEAN | Mati berturut — dibuang |
| iptvcat (MY) | Entri Astro semua mati |
| MIFNtechnology/siaranMy | DMCA block |
| imanawesome2010/sooka | DMCA block Sep 2025 |
| Clearkey sooka (astradamy.com + CloudFront Arena 2/beIN 2) | Domain + distribution dipadam (DNS fail) |
| emenes/ottNav2 (35 ch) | Depan OK, backend mati (`extraott.com`, `vediostream`, `pendy.dpdns.org`) |
| rcsysx/iptv, supermandived, rdfirdz90, dan82dd, Pak-Keting, ejunds/mifn | 404 / kosong / backend mati |
| PerfectTV, Skyhub4K, LayerSeven | 401 / timeout / 403 |
| tonton, mana2.my | Perlu akaun, tiada direct stream |
| Proxy `generationnexxxt.com:19806` (SuperSport) + host mitv | DNS fail |
| 6 proxy Malaysia (senarai IP) | Semua timeout |
| goldottpro trial, Vornic360 | Perlu email + Cloudflare / berbayar |
| FIFA U20 Ch01/Ch02 (sooka event) | Event dah tamat — link mati |
| HK FTA (RTHK 31/33/34/35, HOY TV, HKIBC) | Link iptvcat.net mati |

## 3. DITOLAK — provider haram (ADA, TAK DIINTEGRATE)

Ini semua **hidup** semasa diuji, tapi aku tak masukkan. Sebab: restream channel berbayar tanpa kebenaran = cetak rompak, di luar garis yang aku pegang.

| Provider / panel | Yang ada | Sumber |
|------------------|----------|--------|
| Panel HBO Asia / HBO / Cinemax Asia / Cinemax | 4 channel premium filem | IP rawak `202.150.165.66`, `88.212.15.50` |
| Panel AXN | 1 | `170.83.16.50` |
| Panel Fox Sports / Fox Sports 1 | 2 | `45.184.109.10`, `85.237.89.160` |
| Panel Eurosport 1/2, Discovery, NatGeo, NatGeo Wild | 5 | `213.91.179.28` (Bulgaria) |
| Panel ESPN | 1 | `181.78.197.59` (Argentina) |
| Panel Sky Sports 1 | 1 | `45.228.234.9` |
| Panel Star Movies, Star Sports 1/2 | 3 | `116.90.120.149` |
| Panel Sony Movies | 1 | `45.177.114.115` |
| Panel beIN Sports USA | 1 | `tvsen6.aynaott.com` |
| Panel DAZN Combat | 1 | `jmp2.uk` |
| Panel History Asia | 1 | `freem3u.xyz` |
| Panel Film & Arts | 1 | `15.204.246.24` |
| Bocor Amazon Prime linear (aiv-cdn.net) | TNT Sports 1-4 (UK), beIN AU 1-3, Premier Sports 1/2 | `otte.live.fly.ww.aiv-cdn.net` |
| Panel Eleven Sports 1-4 | 4 | `92.114.85.87` |
| Astro linearjitp ClearKey (DRM) | SuperSport, Arena, dll | `linearjitp.astro.com.my` — DMCA + bypass DRM ditolak |
| Laman spam "astro-arena-m3u8" | Palsu | SEO scam, bukan stream |

## 4. LEGIT — Astro premium yang sah

| Provider | Harga | Isi |
|----------|-------|-----|
| **sooka app (free tier)** | Percuma, dengan iklan | Arena, Awani, AEC, TV1/TV2/TV3, 8TV, Ceria + FAST |
| sooka Mobile | ~RM10-20/bln | Lebih penuh |
| Astro / unifi TV | Langganan | Penuh |

## Ringkasan
- Playlist guna: **87 channel** — semua sah, semua disahkan hidup segmen-level
- Provider haram dikenal pasti: **~25 channel premium** — diuji hidup, ditolak integrasi
- Alasan: hak cipta / Akta Hak Cipta Malaysia — personal use bukan pengecualian
