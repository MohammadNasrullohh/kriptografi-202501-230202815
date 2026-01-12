import hashlib

target_hash = "5f4dcc3b5aa765d61d8327deb882cf99"

wordlist = [
    "123456",
    "qwerty",
    "admin",
    "letmein",
    "dragon",
    "password",
    "game123",
    "player1"
]

print("Game Login Hash (MD5):", target_hash)
print("Memulai dictionary attack...\n")

password_found = False

for word in wordlist:
    hashed_word = hashlib.md5(word.encode()).hexdigest()
    print(f"Trying: {word} -> {hashed_word}")

    if hashed_word == target_hash:
        print("\nPASSWORD DITEMUKAN!")
        print(f"Akun Game Password: {word}")
        password_found = True
        break

if not password_found:
    print("\nPassword tidak ditemukan dalam wordlist")

