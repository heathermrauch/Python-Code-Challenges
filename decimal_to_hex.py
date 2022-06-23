'''
Convert a decimal to a hex

For this challenge, you need to write a function in Python that accepts a
string of ASCII characters. It should return each character's value as a
hexadecimal string. Separate each byte by a space, and return all alpha
hexadecimal characters as lowercase.

Original Challenge found here:
https://www.codecademy.com/resources/blog/advanced-python-code-challenges/
'''

import codecs


def decimal_to_hex(characters:str):
    '''Converst a decimal string to a space separated string of lower case
    hexadecimal characters\n
    Required parameters:
    characters (str): the decimal string to convert
    '''
    return ' '.join([codecs.encode(a, 'utf-8').hex() 
                        for a in characters.lower()])


if __name__ == '__main__':

    characters = 'hello'
    print(decimal_to_hex(characters))
