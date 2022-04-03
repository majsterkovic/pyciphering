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
                return (str(POLYBIUS_SQUARE.index(row)+1), str(i+1))

def encode(text):
    for letter in text:
        if letter.upper() in UPPERCASE_ALPHABET:
            text = text.replace(letter, ''.join(polybius_square_coordinates(letter)))
    return text

def decode(text):
    output = ''
    non_numeric_characters = []
    
    for i, c in enumerate(text):
        if not c.isdigit():
            non_numeric_characters.append(i)

    positions = []
    for i, n in enumerate(non_numeric_characters):
        positions.append( (n + i) // 2 )

    numeric_text = ''.join(c for c in text if c.isdigit())
    pairs = [numeric_text[i:i+2] for i in range(0, len(numeric_text), 2)]
    for pair in pairs:
        try:
            x, y = pair
        except:
            print("Error: The text is not encoded properly.")
            return
        try:
            output += POLYBIUS_SQUARE[int(x)-1][int(y)-1]
        except:
            print("Error: The text is not encoded properly.")
            return
    
    for i in range(len(non_numeric_characters)):
         output = output[:positions[i]] + text[non_numeric_characters[i]] + output[positions[i]:]

    return output