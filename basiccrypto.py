import string
def ceasar_cipher_enc(plaintext):
    #possibly change the input based on pyqt's interface
    alphabet = string.ascii_lowercase
    str.lower(plaintext)
    shifted_alphabet = alphabet[3:] + alphabet[:3]
    table = str.maketrans(alphabet, shifted_alphabet)
    res = plaintext.translate(table)
    return res
#fix it on the main program, but if uppercase or number, check for isalpha()

def ceasar_cipher_dec(ciphertext):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[23:] + alphabet[:23]
    table = str.maketrans(alphabet, shifted_alphabet)
    res = ciphertext.translate(table)
    return res

def punc_cipher(ent):
    #possibly change the input based on pyqt's interface
    alphabet = string.ascii_lowercase
    shifted_alphabet = string.punctuation
    text = str.maketrans(alphabet, shifted_alphabet[:26])
    ent = ent.translate(text)
    return ent

def punc_cipher_dec(plaintext):
    alphabet = string.ascii_lowercase
    shifted_alphabet = string.punctuation[:26]
    text = str.maketrans(shifted_alphabet, alphabet)
    plaintext = plaintext.translate(text)
    return plaintext


