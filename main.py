MORSE_CODE = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    '?': '..--..',
    '!': '-.-.--',
    '.': '.-.-.-',
    ',': '--..--',
    ';': '-.-.-.',
    ':': '---...',
    '+': '.-.-.',
    '-': '-...-',
    '/': '-..-.',
    '=': '-...-',
    ' ': '/'
}
ALPHABET = {value: key for key, value in MORSE_CODE.items()}


def convert_to_morse(text):
    text = text.upper()
    morse_text = ' '.join(MORSE_CODE.get(i) if i in MORSE_CODE else ' '.join(i) for i in text)
    return print(morse_text)


def convert_to_alphabet(text):
    text = text.upper()
    alphabet_text = ''.join(ALPHABET.get(i) if i in ALPHABET else ' '.join(i) for i in text.split())
    return print(alphabet_text)


input_text = input('Type your text:')
selection = input("Type 'C' to convert to morse code.\n"
                  "Type 'T' to convert to alphabet.\n").upper()

if selection == 'C':
    convert_to_morse(input_text)
elif selection == 'T':
    convert_to_alphabet(input_text)



