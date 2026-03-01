# 🔐 Implementasi Algoritma RSA Menggunakan Python

## 📌 Deskripsi Proyek
Program ini merupakan implementasi algoritma kriptografi kunci publik 
RSA (Rivest–Shamir–Adleman) menggunakan bahasa pemrograman Python.

Implementasi dilakukan dari dasar (tanpa menggunakan library kriptografi eksternal)
untuk memahami konsep matematis yang mendasari algoritma RSA.

Proyek ini dibuat untuk memenuhi tugas mata kuliah Kriptografi / Keamanan Informasi
Program Studi Teknik Informatika.

---

## 🧠 Konsep Dasar RSA

RSA adalah algoritma kriptografi kunci publik yang menggunakan dua kunci:
- Public Key → untuk proses enkripsi
- Private Key → untuk proses dekripsi

Langkah-langkah algoritma RSA:

1. Pilih dua bilangan prima p dan q
2. Hitung:
   n = p × q
   φ(n) = (p − 1)(q − 1)
3. Pilih bilangan e sehingga:
   1 < e < φ(n)
   gcd(e, φ(n)) = 1
4. Hitung d sebagai invers modulo:
   d × e ≡ 1 (mod φ(n))
5. Proses:
   Enkripsi  : C = M^e mod n
   Dekripsi  : M = C^d mod n

---

## ⚙️ Struktur Program

Program terdiri dari beberapa fungsi utama:

- is_prime(n) → Mengecek apakah bilangan prima
- gcd(a, b) → Menghitung Greatest Common Divisor
- extended_gcd(a, b) → Extended Euclidean Algorithm
- mod_inverse(e, phi) → Menghitung invers modulo
- mod_exp(base, exp, mod) → Modular Exponentiation
- Proses utama RSA (key generation, enkripsi, dekripsi)

---

## 🖥 Persyaratan Sistem

- Python 3.x
- Tidak memerlukan library tambahan

Untuk mengecek versi Python:
python --version

---

## 🚀 Cara Menjalankan Program

1. Clone repository:

git clone https://github.com/username/rsa-python.git

2. Masuk ke folder project:

cd rsa-python

3. Jalankan program:

python rsa.py

atau

python3 rsa.py

---

## 🧪 Contoh Penggunaan

Input:
Masukkan bilangan prima p: 17
Masukkan bilangan prima q: 11
Masukkan plaintext: HI

Output yang ditampilkan:
- Nilai n
- Nilai φ(n)
- Public Key (e, n)
- Private Key (d, n)
- Ciphertext
- Hasil Dekripsi

---

## 📊 Alur Program

1. Validasi p dan q sebagai bilangan prima
2. Hitung n dan φ(n)
3. Tentukan e dengan syarat gcd(e, φ(n)) = 1
4. Hitung d menggunakan Extended Euclidean Algorithm
5. Enkripsi plaintext berdasarkan nilai ASCII
6. Dekripsi kembali ciphertext
7. Tampilkan hasil akhir

---

## ⚠️ Catatan Penting

- Program ini dibuat untuk keperluan pembelajaran.
- Bilangan prima yang digunakan masih berukuran kecil.
- Implementasi RSA asli menggunakan bilangan prima sangat besar (2048-bit atau lebih).

---

## 👨‍🎓 Identitas Mahasiswa

Nama  : Yudis  
NIM   : 24051204024  
Program Studi : Teknik Informatika  

---

## 📄 Lisensi

Proyek ini dibuat untuk keperluan akademik.
