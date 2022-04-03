UPPER_A = ord('A')
LOWER_A = ord('a')

LOWERCASE_ALPHABET =  [chr(i) for i in range(LOWER_A, ord('z') + 1)]
UPPERCASE_ALPHABET =  [chr(i) for i in range(UPPER_A, ord('Z') + 1)]

def encode(text, shift):

    return ''.join([
        chr((ord(letter) - LOWER_A + shift) % 26 + LOWER_A)
            if letter in LOWERCASE_ALPHABET
        else
        chr((ord(letter) - UPPER_A + shift) % 26 + UPPER_A)
            if letter in UPPERCASE_ALPHABET
        else
        letter for letter in list(text)])

def decode(text, shift):
    return encode(text, -shift)