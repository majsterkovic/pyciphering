UPPER_A = ord('A')
LOWER_A = ord('a')

LOWERCASE_ALPHABET =  [chr(i) for i in range(LOWER_A, ord('z') + 1)]
UPPERCASE_ALPHABET =  [chr(i) for i in range(UPPER_A, ord('Z') + 1)]

def encode(text, keystring):
    key = [k for k in (UPPERCASE_ALPHABET.index(letter.upper()) if letter.isalpha() else None for letter in keystring) if k is not None]
    output = ''
    k = -1
    for i in range(len(text)):
        k = k + 1
        if text[i] in LOWERCASE_ALPHABET:
            output += chr((ord(text[i]) - LOWER_A + key[k % len(key)]) % 26 + LOWER_A)
        elif text[i] in UPPERCASE_ALPHABET:
            output += chr((ord(text[i]) - UPPER_A + key[k % len(key)]) % 26 + UPPER_A)
        else:
            output += text[i]
            k = k - 1
    return output

def decode(text, keystring):
    key = [k for k in (UPPERCASE_ALPHABET.index(letter.upper()) if letter.isalpha() else None for letter in keystring) if k is not None]
    output = ''
    k = -1
    for i in range(len(text)):
        k = k + 1
        if text[i] in LOWERCASE_ALPHABET:
            output += chr((ord(text[i]) - LOWER_A - key[k % len(key)]) % 26 + LOWER_A)
        elif text[i] in UPPERCASE_ALPHABET:
            output += chr((ord(text[i]) - UPPER_A - key[k % len(key)]) % 26 + UPPER_A)
        else:
            output += text[i]
            k = k - 1
    return output