UPPER_A = ord('A')
LOWER_A = ord('a')

LOWERCASE_ALPHABET =  [chr(i) for i in range(LOWER_A, ord('z') + 1)]
UPPERCASE_ALPHABET =  [chr(i) for i in range(UPPER_A, ord('Z') + 1)]

def encode(text):
    return ''.join([
        UPPERCASE_ALPHABET[-1-UPPERCASE_ALPHABET.index(letter)]
            if letter in UPPERCASE_ALPHABET
        else
        LOWERCASE_ALPHABET[-1-LOWERCASE_ALPHABET.index(letter)]
            if letter in LOWERCASE_ALPHABET
        else
        letter for letter in list(text)])

def decode(text):
    return encode(text)