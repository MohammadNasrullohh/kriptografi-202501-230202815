from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Generate key 128-bit
key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_EAX)

# Enkripsi
plaintext = b"Modern Cipher AES Example"
ciphertext, tag = cipher.encrypt_and_digest(plaintext)
print("Ciphertext:", ciphertext)

# Dekripsi
cipher_dec = AES.new(key, AES.MODE_EAX, nonce=cipher.nonce)
decrypted = cipher_dec.decrypt(ciphertext)
print("Decrypted:", decrypted.decode())
