# Laporan Praktikum Kriptografi
Minggu ke-: 9
Topik: Digital Signature (RSA/DSA)
Nama: Mohammad Nasrulloh
NIM: 230202815
Kelas: 5IKRA 

---

# Praktikum Week 9 - Digital Signature

## 1. Tujuan
- Mengimplementasikan tanda tangan digital menggunakan algoritma RSA/DSA.  
- Melakukan verifikasi tanda tangan digital.  
- Memahami fungsi tanda tangan digital dalam integritas dan otentikasi pesan.  

## 2. Dasar Teori
Tanda tangan digital merupakan mekanisme kriptografi yang menjamin keaslian (*authenticity*) dan integritas sebuah pesan. Tidak seperti enkripsi yang bertujuan merahasiakan isi pesan, tanda tangan digital digunakan untuk memvalidasi bahwa pesan benar-benar dibuat oleh pemilik *private key* serta tidak mengalami perubahan.

Pada algoritma RSA untuk tanda tangan digital, proses yang dilakukan adalah:
1. Melakukan hashing terhadap pesan.  
2. Hash tersebut dienkripsi menggunakan *private key* (menjadi signature).  
3. Verifikasi dilakukan dengan mendekripsi signature menggunakan *public key* lalu mencocokkan hasilnya dengan hash pesan asli.  
4. Jika sama, maka tanda tangan dianggap valid.  

## 3. Alat dan Bahan
- Python 3.11  
- Visual Studio Code  
- Git & GitHub  
- Library: pycryptodome  
- OS Windows 10  

## 4. Langkah Percobaan
1. Membuat folder `praktikum/week9-digital-signature/`.  
2. Membuat file `src/signature.py`.  
3. Menuliskan kode untuk generate RSA key, membuat tanda tangan, dan melakukan verifikasi.  
4. Menambahkan uji coba perubahan pesan.  
5. Menjalankan program menggunakan `python signature.py`.  
6. Mengambil screenshot hasil eksekusi dan menyimpannya di folder `screenshots/`.  
7. Membuat file `laporan.md`.  
8. Melakukan commit dan push dengan pesan `week9-digital-signature`.  

## 5. Source Code
```python
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# Generate RSA keys
key = RSA.generate(2048)
private_key = key
public_key = key.publickey()

# Original message
message = b"Hello, ini pesan penting."
h = SHA256.new(message)

# Signing
signature = pkcs1_15.new(private_key).sign(h)
print("Signature:", signature.hex())

# Verification
try:
    pkcs1_15.new(public_key).verify(h, signature)
    print("Verifikasi berhasil: tanda tangan valid.")
except (ValueError, TypeError):
    print("Verifikasi gagal: tanda tangan tidak valid.")

# Modified message
fake_message = b"Hello, ini pesan palsu."
h_fake = SHA256.new(fake_message)

try:
    pkcs1_15.new(public_key).verify(h_fake, signature)
    print("Verifikasi berhasil (seharusnya gagal).")
except (ValueError, TypeError):
    print("Verifikasi gagal: tanda tangan tidak cocok dengan pesan.")
```

## 6. Hasil dan Pembahasan

**Hasil eksekusi program:**
- Signature berhasil dibuat menggunakan *private key* RSA 2048 bit.  
- Verifikasi pesan asli berhasil → menunjukkan bahwa tanda tangan valid.  
- Ketika pesan dimodifikasi, verifikasi gagal → membuktikan bahwa tanda tangan digital melindungi integritas pesan.  

**Pembahasan:**  
Hal ini menunjukkan sifat *non-repudiation* karena hanya pemilik *private key* yang dapat membuat signature tersebut.  

---

## 7. Jawaban Pertanyaan

**1. Perbedaan utama antara enkripsi RSA dan tanda tangan digital RSA?**  
- Enkripsi RSA: *public key* untuk enkripsi, *private key* untuk dekripsi.  
- Digital signature: *private key* untuk menandatangani, *public key* untuk verifikasi.  

**2. Mengapa tanda tangan digital menjamin integritas dan otentikasi pesan?**  
- Karena signature dibuat dari hash pesan → jika pesan diubah sedikit saja, hasil verifikasi langsung gagal.  
- *Private key* hanya dimiliki pembuat pesan → memastikan identitas pengirim (*authentication*).  

**3. Peran Certificate Authority (CA)?**  
- CA menerbitkan dan memvalidasi sertifikat digital.  
- Menjamin bahwa *public key* benar-benar milik individu/organisasi tertentu.  
- Membuat ekosistem tanda tangan digital aman di Internet.  

---

## 8. Kesimpulan
Pada praktikum ini berhasil diimplementasikan tanda tangan digital menggunakan RSA.  
Hasil percobaan menunjukkan bahwa tanda tangan digital efektif untuk menjamin keaslian dan integritas pesan, serta dapat mendeteksi adanya perubahan pada data.  

---

## 9. Daftar Pustaka
- Stinson, D. R. (2019). *Cryptography: Theory and Practice*.  
- Stallings, W. (2018). *Cryptography and Network Security*.  
- Dokumentasi PyCryptodome.  

---

## 10. Commit Log
```
commit week9-digital-signature
Author: Mohammad Nasrulloh <srullasrul59@gmail.com>
Date:   2025-12-01

    week9-digital-signature: implementasi dan laporan
```
