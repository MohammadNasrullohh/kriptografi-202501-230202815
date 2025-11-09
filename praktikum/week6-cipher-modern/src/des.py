from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

# Generate key 64-bit
key = get_random_bytes(8)
cipher = DES.new(key, DES.MODE_ECB)

# Enkripsi
plaintext = b"ABCDEFGH"
ciphertext = cipher.encrypt(plaintext)
print("Ciphertext:", ciphertext)

# Dekripsi
decipher = DES.new(key, DES.MODE_ECB)
decrypted = decipher.decrypt(ciphertext)
print("Decrypted:", decrypted)
