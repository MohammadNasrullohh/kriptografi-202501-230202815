from secretsharing import SecretSharer

secret_text = "KriptografiUPB2025"

secret_hex = secret_text.encode("utf-8").hex()

shares = SecretSharer.split_secret(secret_hex, 3, 5)
print("Shares:", shares)

recovered_hex = SecretSharer.recover_secret(shares[:3])

recovered_text = bytes.fromhex(recovered_hex).decode("utf-8")
print("Recovered secret:", recovered_text)
