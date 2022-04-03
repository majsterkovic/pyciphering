TABLES = [
            [ ['A', 'B', 'C'],
              ['I', 'J', 'K'],
              ['R', 'S', 'T'] ],

            [ ['D', '.', 'E'],
              ['L', 'M', 'N'],
              ['U', 'V', 'W'] ],

            [ ['F', 'G', 'H'],
              ['O', 'P', 'Q'],
              ['X', 'Y', 'Z'] ]
        ]

UPPER_A = ord('A')
LOWER_A = ord('a')

LOWERCASE_ALPHABET =  [chr(i) for i in range(LOWER_A, ord('z') + 1)]
UPPERCASE_ALPHABET =  [chr(i) for i in range(UPPER_A, ord('Z') + 1)] 

def polybius_square_coordinates(letter):
    letter = letter.upper()
    if letter == 'J':
        letter = 'I'
    for i, table in enumerate(TABLES):
        for j, row in enumerate(table):
            for k, l in enumerate(row):
                if l == letter:
                    return (i, j, k)

def encode(text):
    non_alphabetic_characters = []
    for i, c in enumerate(text):
        if c.upper() not in UPPERCASE_ALPHABET:
            non_alphabetic_characters.append(i)
    alpha_text = ''.join(c for c in text if c.upper() in UPPERCASE_ALPHABET)

    first_row = []
    second_row = []
    third_row = []
    for letter in alpha_text:
        x, y, z = polybius_square_coordinates(letter)
        first_row.append(x)
        second_row.append(y)
        third_row.append(z)
    encoded = first_row + second_row + third_row
    output = ''

    for i in range(0, len(encoded), 3):
        if alpha_text[i//3].islower():
            output += TABLES[encoded[i]][encoded[i+1]][encoded[i+2]].lower()
        else:
            output += TABLES[encoded[i]][encoded[i+1]][encoded[i+2]]

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
        x, y, z = polybius_square_coordinates(letter)
        encoded.append(x)
        encoded.append(y)
        encoded.append(z)
    first_row = encoded[:len(encoded)//3]
    second_row = encoded[len(encoded)//3:2*len(encoded)//3]
    third_row = encoded[2*len(encoded)//3:]
    output = ''
    for i in range(0, len(encoded)//3):
        if alpha_text[i].islower():
            output += TABLES[first_row[i]][second_row[i]][third_row[i]].lower()
        else:
            output += TABLES[first_row[i]][second_row[i]][third_row[i]]

    for i in non_alphabetic_characters:
        output = output[:i] + text[i] + output[i:]
    return output