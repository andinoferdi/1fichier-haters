# Task

## Guide
- Ikuti `git-workflow.md`: mulai dari `main`, pull perubahan terbaru, lalu buat branch baru sesuai `git-naming.md`.
- Kerjakan task di branch tersebut. Setelah selesai dan diverifikasi, add, commit, push, lalu buat PR ke `main`.
- Nama branch, commit, PR title, dan deskripsi wajib mengikuti `git-naming.md` dan `git-workflow.md`.
- Project ini desktop app solo dev, tidak ada environment demo/staging web. Verifikasi dilakukan lokal dengan menjalankan `python 1fichier-dl.py` atau build hasil PyInstaller.
- Tidak ada branch staging/demo terpisah. Jika ada branch eksperimen lain yang tertinggal dari `main`, audit perbedaannya dulu sebelum mengambil perubahan, jangan langsung mengubah workflow.
- Untuk memahami flow, baca `core/gui/gui.py` (GUI/behavior) dan `core/download/workers.py` (worker download) langsung, belum ada diagram flow terpisah di repo.

## Kredensial
Tidak relevan untuk project ini. `1fichier-haters` adalah aplikasi desktop single-user tanpa login, akun, atau environment web staging/demo.

> Jika task ke depan menambahkan integrasi yang butuh kredensial (mis. API key layanan proxy), catat cara isinya di sini dan jangan commit ke repo, dokumentasi, screenshot, log, atau PR.

## Konteks
Inti fitur ini adalah `[JELASKAN_RINGKAS_KONTEKS_FITUR]`.

Contoh kasus:
- `[CONTOH_KASUS_1]`
- `[CONTOH_KASUS_2]`

## Subtask Utama
Di `core/download` (engine) atau `core/gui` (GUI):

- [ ] 1. `[SUBTASK_1]`
  - File/area terkait: `[PATH_FILE_TERKAIT]`
  - Ekspektasi: `[HASIL_YANG_DIHARAPKAN]`

- [ ] 2. `[SUBTASK_2]`
  - Kondisi bug saat ini: `[JELASKAN_BUG]`
  - Ekspektasi: `[HASIL_YANG_DIHARAPKAN]`

- [ ] 3. `[SUBTASK_3]`
  - Tujuan: `[TUJUAN_PERUBAHAN]`
  - Data yang dibutuhkan: `[FIELD_ATAU_DATA]`
  - Referensi internal: `[PATH_REFERENSI]`
  - Catatan integrasi: jika perlu payload/signal baru antara worker dan GUI, tentukan field yang aman dan jelas untuk kedua sisi. Jika tidak, jelaskan sumber data yang dipakai.

## Sebelum Eksekusi
Tidak relevan untuk project ini (tidak ada environment staging/demo web). Sebagai gantinya, telusuri kode `core/download` dan `core/gui` yang terkait, serta jalankan aplikasi lokal (`python 1fichier-dl.py`) untuk mengamati flow yang sudah ada sebelum mengubah kode.

## Audit
- Mulai dari `main` sesuai workflow. PR wajib diarahkan ke `main`.
- Jika ada branch eksperimen lain yang lebih maju dari `main`, jangan langsung menyimpulkan itu source of truth. Audit perbedaannya dulu (`git diff main...origin/nama-branch-lain`).
- Ambil perubahan relevan dengan cara paling aman sesuai `git-branch-tips.md`.
- Hasil akhir harus tetap bisa naik ke PR `main` tanpa merusak workflow, history, atau flow download yang sudah berjalan.
- Catat asumsi branch dan alasan teknis bila ada keputusan yang berpotensi membingungkan reviewer.

## Eksekusi
- Boleh menjalankan aplikasi secara lokal untuk melihat UI, flow, dan perilaku fitur. Tidak boleh mengubah `app/settings` atau proxy list default tanpa izin eksplisit.
- Setelah mengubah kode, jangan add/commit/push sebelum diminta.
- Ikuti pola kode yang ada, hindari refactor besar tak diminta. Jangan ubah bagian kritikal (parsing link, bypass reCAPTCHA, worker thread) tanpa kebutuhan task jelas.
- Jalankan verifikasi relevan (unittest, cek manual GUI) sesuai area perubahan.
- Setelah selesai, laporkan: file yang diubah, ringkasan perubahan, hasil verifikasi, dan risiko/catatan.

## Kredensial Tambahan (opsional)
- Web/API tambahan: url `[ADDITIONAL_URL]`, username `[ADDITIONAL_USERNAME]`, password `[ADDITIONAL_PASSWORD]`.

> Isi hanya jika task butuh environment tambahan seperti sistem integrasi, dashboard admin, atau sandbox service eksternal. Sejauh ini `1fichier-haters` tidak punya environment seperti itu.
