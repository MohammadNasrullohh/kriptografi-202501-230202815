def encrypt(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char
    return result

def decrypt(text, key):
    return encrypt(text, -key)

if __name__ == "__main__":
    print("=== Program Caesar Cipher ===")
    plaintext = input("Masukkan teks asli (plaintext): ")
    key = int(input("Masukkan kunci (angka): "))

    ciphertext = encrypt(plaintext, key)
    decrypted = decrypt(ciphertext, key)

    print("\n--- Hasil ---")
    print(f"Teks terenkripsi : {ciphertext}")
    print(f"Teks didekripsi  : {decrypted}")
