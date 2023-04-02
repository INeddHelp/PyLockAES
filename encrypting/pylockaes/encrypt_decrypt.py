from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
import os


class AESEncryption:
    def init(self, password):
        self.key = self.generate_key(password)
        self.iv = os.urandom(16)

    def generate_key(self, password):
        salt = os.urandom(16)
        key = PBKDF2(password, salt, 32, count=1000)
        return key

    def encrypt_file(self, input_file, output_file):
        with open(input_file, "rb") as infile:
            with open(output_file, "wb") as outfile:
                cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
                outfile.write(self.iv)
                while True:
                    chunk = infile.read(16 * 1024)
                    if len(chunk) == 0:
                        break
                    padded_chunk = self.pad(chunk)
                    outfile.write(cipher.encrypt(padded_chunk))

    def decrypt_file(self, input_file, output_file):
        with open(input_file, "rb") as infile:
            with open(output_file, "wb") as outfile:
                iv = infile.read(16)
                cipher = AES.new(self.key, AES.MODE_CBC, iv)
                while True:
                    chunk = infile.read(16 * 1024)
                    if len(chunk) == 0:
                        break
                    padded_chunk = cipher.decrypt(chunk)
                    unpadded_chunk = self.unpad(padded_chunk)
                    outfile.write(unpadded_chunk)

    def pad(self, data):
        padding_len = AES.block_size - len(data) % AES.block_size
        padding = bytes([padding_len] * padding_len)
        return data + padding

    def unpad(self, data):
        padding_len = data[-1]
        if padding_len > AES.block_size or padding_len > len(data):
            raise ValueError("Invalid padding")
        return data[:-padding_len]
