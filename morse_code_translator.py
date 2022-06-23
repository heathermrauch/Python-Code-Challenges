# Morse code translator
# accepts translatable characters as input
# returns Morse code equivalent

MORSE_CODE = {
    'A': '.-',     'B': '-...',   'C': '-.-.',   'D': '-..',
    'E': '.',      'F': '..-.',   'G': '--.',    'H': '....',
    'I': '..',     'J': '.---',   'K': '-.-',    'L': '.-..',
    'M': '--',     'N': '-.',     'O': '---',    'P': '.--.',
    'Q': '--.-',   'R': '.-.',    'S': '...',    'T': '-',
    'U': '..-',    'V': '...-',   'W': '.--',    'X': '-..-',
    'Y': '-.--',   'Z': '--..',   '1': '.----',  '2': '..---',
    '3': '...--',  '4': '....-',  '5': '.....',  '6': '-....',
    '7': '--...',  '8': '---..',  '9': '----.',  '0': '-----',
    ',': '--..--', '?': '..--..', ':': '---...', '&': '.-...',
    ' ': ' '
}

def morse_code(english:str):
    return ''.join([MORSE_CODE.get(x.upper(), '') for x in english])

if __name__ == '__main__'"
    print(morse_code('Hello! My name is Heather!'))
