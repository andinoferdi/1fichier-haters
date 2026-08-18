# Code Rules

## Peran
Anda coding agent untuk project `1fichier-haters` dengan stack `Python 3.11 (core/download)` + `PyQt5 (core/gui)` + `tidak ada database`. Baca konteks repo dulu, ikuti pola yang sudah ada, jaga perubahan minimal dan aman.

## Aktivasi
Aktif bersama A + B. File ini tidak di-import permanen lewat `CLAUDE.md`/`AGENTS.md` di project ini — user kirim manual tiap sesi sesuai `1. First-prompt.md`/`2. Send-to-every-prompt.md`. Paling relevan saat pengguna meminta implementasi, audit, refactor, atau perbaikan kode.

## 1. Prinsip inti
- Pahami file terdekat, worker/thread terkait, dan pola modul (`core/download`, `core/gui`) sebelum mengubah kode.
- Perubahan minimal dan spesifik pada task. Jangan refactor besar tanpa diminta.
- Jangan asumsikan stack di luar `Python`/`PyQt5` kecuali task membuktikan ada integrasi terpisah.
- Jangan mengubah perilaku download, filter duplicate, atau kontrak antara `gui.py` dan `workers.py` tanpa alasan yang bisa diverifikasi.
- Hapus import, variable, dan dependency mati saat menyentuh file terkait.
- Nama class, method, variable, signal, dan widget harus deskriptif.
- Tulis komentar seperlunya, cukup 1-2 komentar penting per bagian. Beri komentar hanya untuk menjelaskan alasan atau keputusan yang tidak terlihat dari kode, bukan mengulang hal yang sudah jelas. Kode yang bersih dan nama yang deskriptif lebih baik daripada banyak komentar.
- Jangan tinggalkan komentar sisa hasil AI seperti penanda langkah, catatan basi, atau penjelasan baris demi baris. Hasil akhir harus terlihat seperti ditulis manusia yang rapi.
- Komentar, pesan commit, log, dan teks penjelas pakai bahasa Indonesia yang natural mengikuti kaidah di `human-language-indonesia.md`. Kalimat langsung ke inti, tidak kaku, dan tidak berlebihan.

## 2. Struktur & pola
- Ikuti struktur folder dan arsitektur nyata repo sebagai sumber kebenaran (`core/download` untuk engine, `core/gui` untuk UI).
- Tambahkan file baru sedekat mungkin dengan domain terkait. Jangan buat struktur baru sebelum memeriksa pola sekitar.
- Pisahkan tanggung jawab sesuai pola repo: entry point (`1fichier-dl.py`), GUI/behavior (`core/gui/gui.py`), worker thread (`core/download/workers.py`), helper parsing/download (`core/download/helpers.py`), bypass reCAPTCHA (`core/download/recapcha.py`).
- Pindahkan logic berat atau reusable ke helper/worker yang sesuai, jangan menumpuk di kelas GUI.

## 3. Data & concurrency
- Hindari operasi berat (parsing link, request proxy) berjalan di main/UI thread. Pakai worker thread (`QThread`/`QRunnable`) seperti pola yang sudah ada.
- Lindungi state yang diakses banyak thread (daftar download, cache link, progress) dari race condition.
- Antrian download besar tetap responsif: jangan lakukan scan/rescan penuh pada list yang terus bertambah bila bisa dihindari.
- Pertahankan filter duplicate link dan validasi status download yang sudah ada. Jangan hapus kondisi ini demi menyederhanakan kode.

## 4. Security & input handling
- Validasi URL yang dimasukkan user (1fichier.com, ouo.io) sebelum diproses, jangan asumsikan format selalu benar.
- Jangan percaya response proxy/reCAPTCHA bypass tanpa cek status dan isi sebelum dipakai lebih lanjut.
- Hindari path traversal saat menentukan folder/nama file hasil download dari data eksternal.
- Jangan hardcode secret, credential, proxy berbayar, token, atau API key di kode, test, maupun dokumentasi. Ambil dari config/file settings.

## 5. Error handling
- Bungkus operasi berisiko (request HTTP, proxy, parsing HTML, reCAPTCHA bypass, file I/O) dengan error handling.
- Log error teknis dengan konteks aman (lihat `app/settings`/log file). Jangan log secret atau payload sensitif.
- Jangan biarkan exception di worker thread membuat GUI freeze atau crash diam-diam.
- Tampilkan status/pesan yang jelas dan bisa ditindaklanjuti di GUI (mis. status "Proxy gagal", "Link tidak valid").

## 6. Integrasi eksternal (1fichier.com, ouo.io reCAPTCHA bypass, proxy HTTPS/SOCKS5)
- Semua URL proxy dan endpoint eksternal berasal dari config/file list (`https_proxy_list.txt`, `socks5_proxy_list.txt`), bukan hardcode di kode.
- Tambahkan timeout, retry terbatas, dan fallback ke proxy lain bila relevan.
- Jangan anggap request sukses jika response 1fichier/ouo.io/proxy masih error atau body belum sesuai ekspektasi (misal captcha belum ke-bypass).

## 7. Proses berat & thread pool
- Gunakan thread pool/worker (`QThreadPool`, `FilterWorker`, dsb) untuk download simultan, bukan blocking di UI thread.
- Jangan jalankan proses besar (download banyak file, scan proxy list) sinkron di main thread.
- Pastikan retry/resume download aman dijalankan ulang tanpa duplikasi entry di list.

## 8. Dependencies
- Perubahan dependency minimal, relevan task, dan menjaga konsistensi `requirements.txt`.
- Jangan menambah library jika kebutuhan bisa dipenuhi stack (`requests`, `curl_cffi`, `PyQt5`) atau helper yang ada.
- Hindari upgrade besar tanpa task khusus, review changelog, dan rencana regresi (terutama `curl_cffi`/`pyinstaller` yang versinya di-pin).

## 9. Sebelum & sesudah coding
Baca repo dan `git status` dulu. Setelah mengubah kode, jalankan verifikasi sesuai area perubahan (unittest untuk logic di `core/download`, cek manual GUI untuk `core/gui`). Tulis ringkasan: bagian yang benar, yang diubah, dan verifikasi yang dijalankan.

Jika RTK tersedia, awali shell command dengan `rtk` (contoh kritis):

```powershell
rtk git status
rtk python -m unittest discover -s tests
rtk python 1fichier-dl.py
```

## 10. Sumber kebenaran (WAJIB)
- Aturan ini harus konsisten dengan implementasi aktif di repo. Jika bertentangan dengan kode nyata, menangkan kebutuhan task, praktik aman, dan perilaku runtime nyata.
- Jaga konsistensi antara `code-rules.md`, `chat-rules.md`, `Agents.md`, `requirements.txt`, dan perilaku aplikasi.
- Jika ada konflik pola ideal vs legacy, pilih perubahan terkecil yang menyelesaikan masalah tanpa merusak alur download yang sudah berjalan.
