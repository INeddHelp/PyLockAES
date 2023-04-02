from Crypto.Cipher import AES
import os


class AESEncryption:
    def __init__(self, password):
        self.key = self.generate_key(password)

    @staticmethod
    def generate_key(password):
        key = password.encode("utf-8")
        key = AES.adjust_key_parity(key)
        return key

    def encrypt_file(self, input_file, output_file):
        with open(input_file, "rb") as infile:
            with open(output_file, "wb") as outfile:
                # Generate a new IV for each encryption
                iv = os.urandom(16)
                cipher = AES.new(self.key, AES.MODE_CBC, iv)
                outfile.write(iv)
                while True:
                    chunk = infile.read(64 * 1024)
                    if len(chunk) == 0:
                        break
                    elif len(chunk) % 16 != 0:
                        chunk += b' ' * (16 - len(chunk) % 16)
                    outfile.write(cipher.encrypt(chunk))

    def decrypt_file(self, input_file, output_file):
        with open(input_file, "rb") as infile:
            with open(output_file, "wb") as outfile:
                iv = infile.read(16)
                cipher = AES.new(self.key, AES.MODE_CBC, iv)
                while True:
                    chunk = infile.read(64 * 1024)
                    if len(chunk) == 0:
                        break
                    outfile.write(cipher.decrypt(chunk))
