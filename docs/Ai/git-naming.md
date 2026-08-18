# Naming, PR, dan Daily Report

Panduan singkat untuk nama branch, commit, PR title, deskripsi PR, dan daily report yang rapi dan konsisten dengan gaya project `1fichier-haters`.

## Branch
- Format: `type/deskripsi-singkat-dengan-dash`. Untuk task personal: `andinoferdi/type/deskripsi-singkat`.
- Type umum: `fix`, `feat`, `feature`, `hotfix`, `refactor`, `chore`, `docs`, `test`.
- Huruf kecil dan dash, bukan spasi atau underscore.

```text
andinoferdi/fix/deskripsi-bug
andinoferdi/feat/nama-fitur
```

## Commit
- Conventional Commits: `type(domain): ringkasan perubahan`.
- `fix` untuk bug, `feat` untuk fitur baru, `refactor` untuk ubah struktur tanpa ubah behavior, `chore` untuk config/dependency, `docs` untuk dokumentasi, `test` untuk testing.
- Ringkasan boleh natural, tetap jelas mencakup perubahan utama.

```text
fix(download): perbaiki flow yang bermasalah
feat(gui): tambah filter dan widget baru
```

Hindari commit terlalu umum: `fix bug`, `update`, `wip`, `tes`.

## PR Title
- Format: `source-branch : ringkasan perubahan`. Project ini solo dev, tidak ada target staging terpisah, semua PR mengarah ke `main`.
- Cek log commit dan PR terbaru agar format tetap konsisten.

```text
andinoferdi/fix/nama-fitur : ringkasan perubahan
andinoferdi/feat/nama-fitur : ringkasan perubahan
```

## PR Description
Singkat, natural, langsung menjelaskan perubahan utama. Tulis test yang benar-benar dijalankan. Project ini tidak memakai database, jadi tulis "Tidak ada migration".

```markdown
## Apa yang berubah?
[ringkasan perubahan]

## Kenapa perlu berubah?
[konteks masalah]

## Cara test
1. [langkah verifikasi]

## Checklist
- [x] Sudah dites sesuai area perubahan
- [x] Tidak ada console error atau log tak perlu
- [x] Tidak ada hardcoded credential atau API key
- [x] Tidak ada migration (project tidak memakai database)
```

## Laporan setelah PR
Kirim laporan singkat ke reviewer/task tracker (bila ada) dengan title dan link PR.

```text
Ringkasan perubahan
[URL_PR]
```

## Daily Report
Minimal 3 item atau sesuai kebutuhan. Bahasa singkat, humanize, langsung menjelaskan pekerjaan.

```text
1. Perbaiki duplicate download saat link ditambah dua kali
2. Perbaiki progress percent yang tidak update
3. Tambah validasi link ouo.io sebelum masuk antrian
4. Tambah handling error saat proxy gagal connect
```
