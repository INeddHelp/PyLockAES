from pylockaes import AESEncryption

encryption = AESEncryption("password")

# Encrypt a file
encryption.encrypt_file("text.txt", "encrypted.txt")

# Decrypt a file
encryption.decrypt_file("encrypted.txt", "decrypted.txt")
