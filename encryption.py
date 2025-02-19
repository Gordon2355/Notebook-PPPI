class Encryptor:
    def __init__(self, key):
        self.key = key

    def encrypt(self, data):
        """
        Имитация шифрования данных.
        """
        return f"Encrypted data: {data} with key: {self.key}"

    def decrypt(self, encrypted_data):
        """
        Имитация расшифровки данных.
        """
        return f"Decrypted data: {encrypted_data} with key: {self.key}"