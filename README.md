# Tugas Besar 2 IF3170
## SmartObjectDetection
An app that can recognize various shapes built with python and clipspy

Tugas Besar II pada kuliah IF3170 bertujuan agar peserta kuliah mengimplementasikan Knowledge Based
System (KBS) untuk mendeteksi bentuk dasar geometri. Point utama dari implementasi knowledge based
system ini adalah rule of representation, construction of inference engine, knowledge base construction,
the image pre-processing dan user interface.

## Requirements
Untuk menjalankan aplikasi ini, dibutuhkan Python 3.x. Aplikasi ini tidak kompatibel dengan Python 2.x.

## Getting Started
### Instalasi
Untuk menjalankan aplikasi ini, diperlukan dependensi pihak ketiga. Untuk memasang dependensi tersebut, jalankan
```shell
pip -r requirements.txt
```
### Menjalankan Program
Untuk menjalankan aplikasi ini, jalankan file `GUI.py`.
```shell
python GUI.py
```

## Panduan Pengguna
Untuk menggunakan aplikasi ini, pengguna dapat:
1. Menekan tombol open image untuk memilih gambar yang akan dianalisis dengan menggunakan OpenCV dan CLIPS.
2. Menekan tombol rule editor untuk melihat dan mengubah rules yang berjalan di balik algoritma deteksi objek
3. Menekan tombol show rules untuk memperlihatkan rules yang berjalan di balik algoritma deteksi objek
4. Menekan tombol show facts untuk melihat fakta-fakta yang aktif saat itu

## Anggota Kelompok (Kelas K-02)
1. 13517002 - Isa Mujahid Darussalam
2. 13517029 - Reyhan Naufal Hakim
3. 13517077 - Dandi Agus Maulana
4. 13517104 - Muhammad Fikri Hizbullah
