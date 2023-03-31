def caesar_cipher(text, key):
    cipher_text = ""
    for char in text:
        if char.isalpha():
            shifted_char = chr((ord(char) - 65 + key) % 26 + 65)
            cipher_text += shifted_char
        else:
            cipher_text += char
    return cipher_text

def caesar_decipher(cipher_text, key):
    text = ""
    for char in cipher_text:
        if char.isalpha():
            shifted_char = chr((ord(char) - 65 - key) % 26 + 65)
            text += shifted_char
        else:
            text += char
    return text

print(caesar_cipher("HELLO WORLD", 5))
print(caesar_decipher("MJQQT BTWQI", 5))
