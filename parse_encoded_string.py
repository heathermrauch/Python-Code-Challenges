
# Parse an encoded string
# Accepts an encoded string containing first name, last name and id separated
# by an undetermined count of zeros
# Returns a dictionary of parsed values
# Original Challenge found here: https://www.codecademy.com/resources/blog/advanced-python-code-challenges/


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
