
# Convert a decimal to a hex
# accepts a string of ASCII characters
# returns a space delimited lower case string of hexadecimal characters
# Original Challenge found here: https://www.codecademy.com/resources/blog/advanced-python-code-challenges/

import codecs


def decimal_to_hex(characters:str):
    '''Converst a decimal string to a space separated string of lower case
    hexadecimal characters\n
    Required parameters:
    characters (str): the decimal string to convert
    '''
    return ' '.join([codecs.encode(a, 'utf-8').hex() for a in characters.lower()])


if __name__ == '__main__':

    characters = 'hello'
    print(decimal_to_hex(characters))
