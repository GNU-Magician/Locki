import Crypto
import binascii
import os
from Crypto.Cipher import Salsa20
from Crypto.Cipher import AES
class enc():
    def __init__(self):
        self.nonce = None

    def salsa20_encrypt(self, plaintext):
        plaintext = bytes(plaintext, 'utf-8')
        secret = b'*Thirty-two byte (256 bits) key*'
        cipher = Salsa20.new(key=secret)
        msg = cipher.nonce + cipher.encrypt(plaintext)
        return binascii.hexlify(msg).decode("utf-8")

    def salsa20_decrypt(self, msg):
        msg = binascii.unhexlify(msg)  
        secret = b'*Thirty-two byte (256 bits) key*'
        msg_nonce = msg[:8]
        ciphertext = msg[8:]
        cipher = Salsa20.new(key=secret, nonce=msg_nonce)
        plaintext = cipher.decrypt(ciphertext)
        return plaintext

    def aes_encrypt(self, plaintext):
        plaintext = bytes(plaintext, "utf-8")
        key = b'*Thirty-two byte (256 bits) key*'
        cipher = AES.new(key, AES.MODE_EAX)
        nonce = cipher.nonce
        ciphertext, tag = cipher.encrypt_and_digest(plaintext)
        print(ciphertext)
        print(nonce)
        return ciphertext, nonce


    def aes_decrypt(self, ciphertext, nonce):
        ciphertext = binascii.unhexlify(ciphertext)
        nonce = binascii.unhexlify(nonce)
        key = b'*Thirty-two byte (256 bits) key*'
        cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)

        plaintext = cipher.decrypt(ciphertext)
        return plaintext.decode("utf-8")
        

        
