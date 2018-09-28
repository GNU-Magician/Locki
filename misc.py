import Crypto
from Crypto.Signature import pkcs1_15
from Crypto.PublicKey import RSA
from Crypto import Hash
from Crypto.Hash import SHA, SHA256
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes
import os
import pyAesCrypt
import binascii

def keyPair(fname):
    try:
        key = RSA.generate(2048)
        f = open(fname, 'wb')
        f.write(key.export_key('PEM'))
        f.close()
    except FileNotFoundError:
        return 2

def readKeyPair(pkey, fname):
    try:
        f = open(pkey, 'rb').read()
        key = RSA.import_key(f,passphrase="")
        a = open(fname, 'wb').write(key.publickey().export_key())
    except FileNotFoundError:
        return 2

def encryptRSA(text, keypath):
    try:
        file_data = open(text, "rb").read()
        file_out = open(text, "wb")
        recipient_key = RSA.import_key(open(keypath).read())
        session_key = get_random_bytes(16)
        cipher_rsa = PKCS1_OAEP.new(recipient_key)
        enc_session_key = cipher_rsa.encrypt(session_key)
        cipher_aes = AES.new(session_key, AES.MODE_EAX)
        ciphertext, tag = cipher_aes.encrypt_and_digest(file_data)
        [ file_out.write(x) for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext) ]
    except FileNotFoundError:
        return 2
    else:
        return True


def decryptRSA(text, keypath):
    try:
        file_in = open(text, "rb")
        private_key = RSA.import_key(open(keypath).read())
        enc_session_key, nonce, tag, ciphertext = \
        [ file_in.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1) ]
    # Decrypt the session key with the private RSA key
        cipher_rsa = PKCS1_OAEP.new(private_key)
        session_key = cipher_rsa.decrypt(enc_session_key)
    # Decrypt the data with the AES session key
        cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
        data = cipher_aes.decrypt_and_verify(ciphertext, tag)
        file_out = open(text, "wb").write(data)
    except FileNotFoundError:
        return 2
    except AttributeError:
        return 2
    else:
        return True


def makehash(text):
    hash_object = Hash.SHA256.new(text)
    print(hash_object.hexdigest())
    a = binascii.unhexlify(hash_object.hexdigest())
    return binascii.hexlify(a).decode('utf-8')

def makesig(text, keypath):
    try:
        key = RSA.import_key(open(keypath).read())
        h = SHA256.new(text)
        signature = pkcs1_15.new(key).sign(h)
        print(signature)
        print(text)
        return binascii.hexlify(signature).decode('utf-8')
    # return signature, message
    except AttributeError:
        return 3
    except FileNotFoundError:
        return 3
    except (TypeError, ValueError): 
        return 4


def versig(message, signature, file):
    signature = binascii.unhexlify(signature)
    key = RSA.import_key(open(file).read())
    h = SHA256.new(message)
    try:
        pkcs1_15.new(key).verify(h, signature)
        print("The signature is valid.")
        return True
    except (ValueError, TypeError):
        print("The signature is not valid.")
        return False
    except AttributeError:
        return 3
    except FileNotFoundError:
        return 3


def file_enc(filepath, password):
    try:
        filepath = filepath.replace("/", "\\")
        bufferSize = 64 * 1024
        pyAesCrypt.encryptFile(filepath, filepath + ".aes", password, bufferSize)
        os.remove(filepath)
    except FileNotFoundError:
        return 2
    else:
        return True

def file_dec(filepath, password):
    try:
        bufferSize = 64 * 1024
        pyAesCrypt.decryptFile(filepath, filepath.strip(".aes"), password, bufferSize)
        os.remove(filepath)
    except ValueError:
        return 2
    except FileNotFoundError:
        return 3
    except AttributeError:
        return 3
    else:
        return True


