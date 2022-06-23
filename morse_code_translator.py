'''
Create a Morse code translator

We no longer use Morse code to transfer information, but that doesn't mean you
can't use it in a code challenge. Write a function in Python that takes in a
string that can have alphanumeric characters in lower or upper case.

The string can also contain any special characters handled in Morse code,
including commas, colons, apostrophes, periods, exclamation marks, and question
marks. The function should return the Morse code equivalent for the string.

Original Challenge found here:
https://www.codecademy.com/resources/blog/advanced-python-code-challenges/
'''

MORSE_CODE = { 
    'A':'.-',      'B':'-...',    'C':'-.-.',     'D':'-..',
    'E':'.',       'F':'..-.',    'G':'--.',      'H':'....',
    'I':'..',      'J':'.---',    'K':'-.-',      'L':'.-..',
    'M':'--',      'N':'-.',      'O':'---',      'P':'.--.',
    'Q':'--.-',    'R':'.-.',     'S':'...',      'T':'-',
    'U':'..-',     'V':'...-',    'W':'.--',      'X':'-..-',
    'Y':'-.--',    'Z':'--..',    '1':'.----',    '2':'..---',
    '3':'...--',   '4':'....-',   '5':'.....',    '6':'-....',
    '7':'--...',   '8':'---..',   '9':'----.',    '0':'-----',
    ',':'--..--',  ':': '---...', '\'': '.----.', '.': '.-.-.-',
    '!': '-.-.--', '?': '..--..'
}


def to_morse_code(letters:str):
    '''Converts a string to Morse Code
    Required parameters:
    letters (str): the string to translate to Morse Code
    '''
    encoded = ' '.join([MORSE_CODE.get(x.upper(), '') for x in letters])
    return encoded

def from_morse_code(morse_code:str):
    '''Converts Morse Code to a string
    Required parameters:
    morse_code (str): the Morse Code to translate to letters
    '''
    parsed = [x.split() for x in morse_code.split('  ')]
    decoded = ''
    for word in parsed:
        for letter in word:
            decoded += [k for k, v in MORSE_CODE.items() if v == letter][0]
        decoded += ' '
    return decoded


if __name__ == '__main__':
    
    message = 'This is an english string'
    encoded = to_morse_code(message)
    decoded = from_morse_code(encoded)

    print('Encoded Message:', encoded)
    print('Decoded Message:', decoded)
