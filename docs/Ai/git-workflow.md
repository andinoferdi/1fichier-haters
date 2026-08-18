# Git Workflow

Project `1fichier-haters` memakai GitHub Flow sederhana untuk solo dev. `main` adalah satu-satunya branch dan menjadi production/source of truth yang harus selalu stabil. Belum ada branch staging maupun CI di repo ini.

## Aturan paling penting
Jangan push langsung ke `main` untuk perubahan yang belum diverifikasi. Semua perubahan lewat Pull Request: branch dari `main`, kerjakan dan verifikasi di branch itu, lalu PR langsung ke `main` (tidak ada branch staging terpisah).

## Naming
Format: `type/deskripsi-singkat-dengan-dash`. Jika gaya tim memakai prefix nama: `andinoferdi/type/deskripsi-singkat`.

| Type | Untuk |
| --- | --- |
| `feat` / `feature` | Fitur baru |
| `fix` | Bug fix tidak urgent |
| `hotfix` | Fix critical di production |
| `refactor` | Refactor tanpa ubah behavior |
| `chore` | Config, dependency, dan sejenisnya |

Gunakan huruf kecil dan dash, bukan underscore atau spasi. Nama harus deskriptif tanpa konteks tambahan.

## Alur kerja
```bash
# 1. Mulai dari branch utama terbaru
git checkout main
git pull origin main
git checkout -b fix/deskripsi-singkat

# 2. Commit kecil dan sering, satu konteks per commit
git add -p
git commit -m "fix(download): ringkasan perubahan"

# 3. Push dan buka PR ke main
git push origin fix/deskripsi-singkat
```

Buka PR (base: `main`, compare: branch fitur). Review sendiri (solo project) dan pastikan verifikasi lokal sudah dijalankan sebelum merge. Setelah merge, hapus branch:

```bash
git push origin --delete fix/deskripsi-singkat
git branch -d fix/deskripsi-singkat
```

## Commit message
Conventional Commits: `type(domain): deskripsi singkat`. Gunakan imperative mood ("tambah validasi", bukan "menambahkan"). Bayangkan melanjutkan "commit ini akan ...".

Baik: `feat: tambah retry logic untuk timeout proxy` / `fix: duplicate download saat link ditambah dua kali`.
Buruk: `fix bug`, `update`, `wip`, `asdfgh`.

## Pull Request
- Satu PR = satu concern. Jangan campur fitur baru dengan refactor besar.
- Solo project, tidak ada reviewer wajib. Self-review sebelum merge ke `main` dan pastikan tidak ada CI yang menggantikan verifikasi manual.
- Resolve semua comment sebelum merge (bila ada kolaborator lain).
- Tulis test yang benar-benar sudah dijalankan. Project ini tidak memakai database, jadi tulis "Tidak ada migration".

Template deskripsi:

```markdown
## Apa yang berubah?
[ringkasan perubahan utama]

## Kenapa perlu berubah?
[konteks masalah sebelumnya]

## Cara test
1. [langkah verifikasi, misalnya `python 1fichier-dl.py` lalu coba download]

## Checklist
- [ ] Sudah dites manual sesuai area perubahan
- [ ] Tidak ada console error atau log tak perlu
- [ ] Tidak ada migration (project tidak memakai database)
- [ ] Tidak ada hardcoded credential atau API key
```

## Handling conflict
Sync branch dari branch utama pakai merge, bukan rebase (rebase menulis ulang history dan berbahaya bila branch sudah di-push).

```bash
git checkout main
git pull origin main
git checkout fix/deskripsi-singkat
git merge main
# resolve conflict, lalu:
git add .
git commit -m "chore: merge main into fix/deskripsi-singkat"
git push origin fix/deskripsi-singkat
```

Sync setidaknya tiap 2-3 hari untuk task panjang agar conflict tidak menumpuk.

## Yang tidak boleh
- Force push ke branch yang sudah di-share tanpa koordinasi. Gunakan `--force-with-lease` hanya di branch sendiri.
- Commit credential, API key, file environment, private key, atau secret. Sekali ter-commit, dianggap compromised meski dihapus.
- Merge ke `main` tanpa verifikasi manual dulu (jalankan aplikasi, cek flow download terkait).
- Branch dari branch orang lain tanpa alasan jelas (PR akan membawa semua commit branch itu). Selalu branch dari `main`.
- Menggabungkan fitur besar, refactor besar, dan bug fix kecil dalam satu PR.
