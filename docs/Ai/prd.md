# 1fichier-haters - Product Requirements Document

## Overview
Build `1fichier-haters` (1Fichier Downloader) untuk pengguna 1fichier.com tanpa akun premium agar dapat mengelola antrian download dari link 1fichier/ouo.io dengan lebih cepat (bypass waktu tunggu free user), aman, konsisten, dan terukur.

## Core Features

### User Management
Tidak relevan. Aplikasi desktop single-user tanpa login, akun, atau role/permission.

### Main Feature
- Menambah, memantau, dan mengelola antrian download: link 1fichier.com dan shortlink ouo.io (dengan bypass reCAPTCHA otomatis).
- Validasi input link dan feedback jelas lewat status di GUI (invalid link, duplicate, proxy gagal).
- Status download per item: queued, downloading, paused, done, failed.
- Detail item dengan progress %, kecepatan, dan proxy yang sedang dipakai (`Protocol://IP:PORT`).

### Organization
- Tampilan utama berupa list/tabel antrian download dengan status dan progress tiap item.
- Kontrol per item: pause, resume, stop.
- Tambah link manual atau otomatis dari clipboard.
- Settings dialog untuk konfigurasi koneksi (proxy list custom via URL), jumlah thread download simultan, dan folder tujuan.

## Technical Requirements

### Frontend
- Gunakan stack frontend project `PyQt5` (`core/gui`, tema `pyqtdarktheme`).
- UI konsisten, mengikuti pola widget dan layout yang ada. Mendukung light/dark theme.
- State management mengikuti pola signal/slot PyQt5 yang sudah ada. Validasi client (format link) hanya pendukung, validasi utama tetap di layer download sebelum request dikirim.

### Backend
- Gunakan stack engine download project `Python 3.11` (`core/download`), tanpa database (state di memory + `app/settings`).
- Worker thread, helper parsing, dan bypass reCAPTCHA mengikuti pola repo (`workers.py`, `helpers.py`, `recapcha.py`).
- Tidak ada schema/migration karena tidak memakai database. Konfigurasi proxy dan settings disimpan di file lokal.
- Error handling dan retry konsisten untuk request ke 1fichier.com, ouo.io, dan proxy.
- Integrasi eksternal `1fichier.com, ouo.io (reCAPTCHA bypass), proxy HTTPS/SOCKS5` memakai konfigurasi dari file list, bukan hardcode di kode.

### Infrastructure
- Konfigurasi berbasis file lokal (`app/settings`, proxy list `.txt`), bukan environment server.
- Automated testing: unittest di folder `tests/` untuk regresi logic download (mis. duplicate download).
- Build/release memakai PyInstaller (`onefile`, Windows `exe`), belum ada CI/CD otomatis.
- Logging dasar ke file (`app/logs.txt`) untuk troubleshooting.

## Success Criteria
- User dapat menambah dan menyelesaikan download 1fichier/ouo.io tanpa menunggu waktu free user secara manual.
- Fitur prioritas (tambah link, bypass reCAPTCHA, multi-thread download, proxy custom) berjalan sesuai acceptance criteria.
- GUI tetap responsif (tidak freeze) saat download berjalan di background.
- Tampilan konsisten di light dan dark theme pada resolusi desktop umum.
- Tidak ada defect critical (crash, duplicate download, kehilangan progress) sebelum release.

## Priority
1. **Phase 1**: Tambah link, download dasar, bypass reCAPTCHA ouo.io, GUI inti (list, status, progress).
2. **Phase 2**: Multi-thread download simultan, proxy custom via settings, add from clipboard, decimal progress %.
3. **Phase 3**: Auto-switch proxy lambat, exception handling duplicate link lanjutan, dukungan asyncio, dukungan situs download lain selain 1fichier.

## Timeline
Target rilis berikutnya: `[DURASI_TARGET]` — belum ada roadmap waktu resmi di repo, isi sesuai rencana Anda.
