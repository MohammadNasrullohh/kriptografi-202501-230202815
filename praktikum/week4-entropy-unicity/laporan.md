# Laporan Praktikum Week 4 — Entropy & Unicity Distance

**Nama:** Mohammad Nasrulloh
**NIM:** 230202815
**Mata Praktikum:** Kriptografi - Minggu 4
**Tanggal:** 2025-10-20

---

## 1. Tujuan

Praktikum ini bertujuan untuk:

1. Memahami konsep entropi kunci dan cara menghitungnya.
2. Mengukur unicity distance untuk menilai tingkat keamanan cipher.
3. Melakukan analisis waktu brute-force berdasarkan ukuran ruang kunci.
4. Mengevaluasi kekuatan kunci terhadap potensi serangan komputasional.

---

## 2. Ringkasan Teori

1. **Entropi (H(K))** merupakan ukuran ketidakpastian atau tingkat acak dari ruang kunci. Rumusnya:
   [
   H(K) = \log_2 |K|
   ]
   Semakin besar nilai entropi, semakin tinggi tingkat keamanan karena ruang kunci semakin luas.

2. **Unicity Distance (U)** menunjukkan jumlah minimal ciphertext yang dibutuhkan agar suatu kunci dapat ditentukan secara unik:
   [
   U = \frac{H(K)}{R \cdot \log_2 |A|}
   ]
   dengan ( R ) adalah redundansi bahasa dan ( |A| ) ukuran alfabet. Nilai U kecil menandakan cipher lebih mudah dipecahkan.

3. **Brute Force Attack** adalah metode mencoba semua kemungkinan kunci. Waktu yang dibutuhkan sangat bergantung pada ukuran ruang kunci dan kemampuan komputasi (misalnya percobaan per detik).

---

## 3. Hasil Perhitungan

Perhitungan dilakukan menggunakan Python (file `entropy_unicity.py`).
Hasil utama yang diperoleh:

| Cipher               | Ukuran Kunci | Entropi (bit) | Unicity Distance (karakter) |
| -------------------- | ------------ | ------------- | --------------------------- |
| Caesar Cipher        | 26           | 4.7004        | 0.242                       |
| AES-128              | 2¹²⁸         | 128.0000      | 6.593                       |
| AES-256              | 2²⁵⁶         | 256.0000      | 13.187                      |
| Custom 40-bit Cipher | 2⁴⁰          | 40.0000       | 2.060                       |

**Estimasi Waktu Brute Force (dengan 1e9 percobaan/detik):**

* **Caesar Cipher (26 kunci)** → < 0.00001 detik
* **AES-128 (2¹²⁸ kunci)** → ±1.08×10²² tahun
* **AES-256 (2²⁵⁶ kunci)** → tidak terhitung praktis (lebih dari usia alam semesta)
* **40-bit key** → ±12.7 hari

Seluruh hasil dan log detail tersimpan pada:

* `screenshots/stdout.txt`
* `screenshots/summary.csv`
* `screenshots/hasil_output.txt`

---

## 4. Analisis & Diskusi

1. **Makna Entropi dalam Keamanan Kunci**
   Entropi mengukur banyaknya informasi atau ketidakpastian dalam ruang kunci. Nilai entropi tinggi berarti kunci lebih acak dan sulit ditebak. Misalnya, AES-256 memiliki entropi 256 bit yang jauh lebih tinggi dibanding Caesar (4.7 bit), sehingga hampir mustahil diretas dengan brute force.

2. **Pentingnya Unicity Distance**
   Unicity distance menandakan batas minimal ciphertext agar kunci bisa diidentifikasi secara unik. Cipher dengan U kecil (seperti Caesar) sangat mudah dipecahkan karena informasi yang dibutuhkan untuk mengenali kunci sangat sedikit. Sebaliknya, AES memiliki U besar sehingga meski banyak ciphertext tersedia, kunci tetap tidak dapat disimpulkan tanpa eksplorasi penuh ruang kunci.

3. **Brute Force sebagai Ancaman**
   Meskipun algoritma modern kuat, brute force tetap menjadi ancaman jika kunci terlalu pendek, pengguna memilih password lemah, atau sistem tidak membatasi percobaan login. Oleh karena itu, manajemen kunci dan panjang kunci minimal sangat penting dalam implementasi keamanan.

---

## 5. Kesimpulan

* Nilai **entropi** berbanding lurus dengan kekuatan kunci: semakin besar ruang kunci → semakin aman.
* **Unicity distance** memberi gambaran seberapa sulit cipher dipecahkan dari ciphertext.
* **Brute force** tidak efektif pada cipher modern seperti AES, namun masih relevan pada sistem dengan kunci kecil.

---

## 6. Struktur & Commit

```
praktikum/week4-entropy-unicity/
 ├─ src/entropy_unicity.py
 ├─ screenshots/stdout.txt
 ├─ screenshots/summary.csv
 ├─ screenshots/hasil_output.txt
 └─ laporan.md
```
