# PyLockAES

PyLockAES is a Python library that provides AES encryption and decryption functionality. It is designed to make it easy for developers to add encryption to their Python projects.

![Screenshot1](https://i.ibb.co/R2rJKX1/Screenshot-from-2023-04-01-22-34-09.png)

## Installation

You can install PyLockAES using pip:

```
pip install pylockaes
```


## Usage

### Encrypting a file

To encrypt a file, you first need to create an instance of the AESEncryption class with a password:

```python
from pylockaes import AESEncryption

password = "mysecretpassword"
encryption = AESEncryption(password)
```

Then you can call the encrypt_file method with the input and output file paths:

```python
encryption.encrypt_file("input_file.txt", "output_file.bin")
```

### Decrypting a file

To decrypt a file, you create an instance of the AESEncryption class with the same password as before:

```python
from pylockaes import AESEncryption

password = "mysecretpassword"
encryption = AESEncryption(password)
```

Then you can call the decrypt_file method with the input and output file paths:

```python
encryption.decrypt_file("encrypted_file.bin", "decrypted_file.txt")
```

# Contributing

Contributions are welcome! If you have a bug fix, enhancement, or new feature to contribute, please open a pull request.

# Licence

PyLockAES is licensed under the MIT License.

Feel free to modify it to better suit your needs!
