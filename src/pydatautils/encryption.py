from Crypto.Cipher import AES
import base64, hashlib


def encrypt_data(data):
    """
    Encrypts data using AES.MODE_CBC and returns the encrypted data as a base64-encoded string.

    Args:
        key (bytes): The encryption key as a bytes object.
        data (bytes): The data to be encrypted as a bytes object.

    Returns:
        str: The encrypted data as a base64-encoded string.
    """
    iv = b'0123456789abcdef'  # Fixed initialization vector
    data = data.encode('utf-8')
    key = hashlib.sha256("mysecretkey".encode()).digest()
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padding_len = AES.block_size - len(data) % AES.block_size
    data += bytes([padding_len] * padding_len)
    encrypted = cipher.encrypt(data)
    return base64.b64encode(encrypted).decode('utf-8')


def decrypt_data(encrypted_data):
    """
    Decrypts base64-encoded data using AES.MODE_CBC and returns the decrypted data as a bytes object.

    Args:
        key (bytes): The encryption key as a bytes object.
        encrypted_data (str): The base64-encoded encrypted data.

    Returns:
        bytes: The decrypted data as a bytes object.
    """
    iv = b'0123456789abcdef'  # Fixed initialization vector
    key = hashlib.sha256("mysecretkey".encode()).digest()
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted = base64.b64decode(encrypted_data.encode('utf-8'))
    decrypted = cipher.decrypt(encrypted)
    padding_len = decrypted[-1]
    return decrypted[:-padding_len].decode("utf-8")
