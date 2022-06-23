'''
Parse an encoded string

In this Python challenge, you need to write a function that accepts an encoded
string as a parameter. This string will contain a first name, last name, and an
id.

Values in the string can be separated by any number of zeros. The id is a
numeric value but will contain no zeros. The function should parse the string
and return a Python dictionary that contains the first name, last name, and id
values.

An example input would be "Robert000Smith000123". The function should return
the following using that input:

{ "first_name": "Robert", "last_name": "Smith", "id": "123" }

Original Challenge found here: 
https://www.codecademy.com/resources/blog/advanced-python-code-challenges/
'''


def parse_str(string:str):
    '''Parses a 0 delimited string containing first_name, last_name, and id\n
    Required parameters:
    string (str): 0 delimited string containing first_name, last_name, and id
    '''
    parsed = [x for x in string.split('0') if x != '']
    return {'first_name': parsed[0], 'last_name': parsed[1], 'id': parsed[2]}


if __name__ == '__main__':

    encoded_str = 'Robert000Smith000123'
    print(parse_str(encoded_str))
