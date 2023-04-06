from Crypto.Cipher import AES
import os


class AESEncryption:
    def __init__(self, password):
        self.key = self.generate_key(password)
        self.iv = os.urandom(AES.block_size)

    @staticmethod
    def generate_key(password):
        key = password.encode("utf-8")
        key += b'\0' * (AES.block_size - len(key) % AES.block_size)
        return key

    def encrypt_file(self, input_file, output_file):
        with open(input_file, "rb") as infile:
            with open(output_file, "wb") as outfile:
                cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
                outfile.write(self.iv)
                while True:
                    chunk = infile.read(64 * 1024)
                    if len(chunk) == 0:
                        break
                    elif len(chunk) % AES.block_size != 0:
                        chunk += b' ' * (AES.block_size - len(chunk) % AES.block_size)
                    outfile.write(cipher.encrypt(chunk))

    def decrypt_file(self, input_file, output_file):
        with open(input_file, "rb") as infile:
            with open(output_file, "wb") as outfile:
                iv = infile.read(AES.block_size)
                cipher = AES.new(self.key, AES.MODE_CBC, iv)
                while True:
                    chunk = infile.read(64 * 1024)
                    if len(chunk) == 0:
                        break
                    outfile.write(cipher.decrypt(chunk))