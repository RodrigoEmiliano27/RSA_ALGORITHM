from decimal import Decimal
def encrypt(msg_plaintext, e,n):
    #unpack key value pair
    msg_ciphertext = [pow(ord(c), e, n) for c in msg_plaintext]
    return msg_ciphertext

def decrypt(msg_ciphertext, d,n):
    msg_plaintext = [chr(pow(c, d, n)) for c in msg_ciphertext]
    # No need to use ord() since c is now a number
    # After decryption, we cast it back to character
    # to be joined in a string for the final result
    return (''.join(msg_plaintext))





