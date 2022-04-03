POLYBIUS_SQUARE = [ ['A', 'B', 'C', 'D', 'E'],
                    ['F', 'G', 'H', 'I', 'K'],
                    ['L', 'M', 'N', 'O', 'P'],
                    ['Q', 'R', 'S', 'T', 'U'],
                    ['V', 'W', 'X', 'Y', 'Z'] ]

UPPER_A = ord('A')
LOWER_A = ord('a')

LOWERCASE_ALPHABET =  [chr(i) for i in range(LOWER_A, ord('z') + 1)]
UPPERCASE_ALPHABET =  [chr(i) for i in range(UPPER_A, ord('Z') + 1)]                    

def polybius_square_coordinates(letter):
    letter = letter.upper()
    if letter == 'J':
        letter = 'I'
    for row in POLYBIUS_SQUARE:
        for i, l in enumerate(row):
            if l == letter:
                return (POLYBIUS_SQUARE.index(row), i)

def encode(text):
    non_alphabetic_characters = []
    for i, c in enumerate(text):
        if c.upper() not in UPPERCASE_ALPHABET:
            non_alphabetic_characters.append(i)
    alpha_text = ''.join(c for c in text if c.upper() in UPPERCASE_ALPHABET)

    first_row = []
    second_row = []
    for letter in alpha_text:
        x, y = polybius_square_coordinates(letter)
        first_row.append(x)
        second_row.append(y)
    encoded = first_row + second_row
    output = ''

    for i in range(0, len(encoded), 2):
        if alpha_text[i//2].islower():
            output += POLYBIUS_SQUARE[encoded[i]][encoded[i+1]].lower()
        else:
            output += POLYBIUS_SQUARE[encoded[i]][encoded[i+1]]

    for i in non_alphabetic_characters:
        output = output[:i] + text[i] + output[i:]
    return output

def decode(text):
    non_alphabetic_characters = []
    for i, c in enumerate(text):
        if c.upper() not in UPPERCASE_ALPHABET:
            non_alphabetic_characters.append(i)
    alpha_text = ''.join(c for c in text if c.upper() in UPPERCASE_ALPHABET)

    encoded = []

    for letter in alpha_text:
        x, y = polybius_square_coordinates(letter)
        encoded.append(x)
        encoded.append(y)
    first_row = encoded[:len(encoded)//2]
    second_row = encoded[len(encoded)//2:]
    output = ''

    for i in range(0, len(encoded)//2):
        if alpha_text[i].islower():
            output += POLYBIUS_SQUARE[first_row[i]][second_row[i]].lower()
        else:
            output += POLYBIUS_SQUARE[first_row[i]][second_row[i]]

    for i in non_alphabetic_characters:
        output = output[:i] + text[i] + output[i:]
    return output