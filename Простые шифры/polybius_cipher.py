def polybius_cipher(text):
    cipher_text = ""
    polybius_table = {
        'A': '11', 'B': '12', 'C': '13', 'D': '14', 'E': '15', 
        'F': '21', 'G': '22', 'H': '23', 'I': '24', 'J': '24', 
        'K': '25', 'L': '31', 'M': '32', 'N': '33', 'O': '34', 
        'P': '35', 'Q': '41', 'R': '42', 'S': '43', 'T': '44', 
        'U': '45', 'V': '51', 'W': '52', 'X': '53', 'Y': '54', 'Z': '55'
    }
    for char in text:
        if char.isalpha():
            cipher_text += polybius_table[char.upper()]
        else:
            cipher_text += char
    return cipher_text

def polybius_decipher(cipher_text):
    text = ""
    polybius_table = {
        '11': 'A', '12': 'B', '13': 'C', '14': 'D', '15': 'E', 
        '21': 'F', '22': 'G', '23': 'H', '24': 'I/J', '25': 'K', 
        '31': 'L', '32': 'M', '33': 'N', '34': 'O', '35': 'P', 
        '41': 'Q', '42': 'R', '43': 'S', '44': 'T', '45': 'U', 
        '51': 'V', '52': 'W', '53': 'X', '54': 'Y', '55': 'Z'
    }
    # Convert each pair of numbers to corresponding letter
    for i in range(0, len(cipher_text), 2):
        pair = cipher_text[i:i+2]
        if pair in polybius_table:
            text += polybius_table[pair]
    return text

print(polybius_cipher("HELLO WORLD"))
print(polybius_decipher("2315313134  5234423114")) # "HELLO WORLD"
