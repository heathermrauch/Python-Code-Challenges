'''
Find the difference between the strings
Write a function in Python that accepts two string parameters. The first
parameter will be a string of characters, and the second parameter will be the
same string of characters, but they’ll be in a different order and have one
extra character. The function should return that extra character.

For example, if the first parameter is "eueiieo" and the second is "iieoedue,"
then the function should return "d."

Original Challenge found here:
https://www.codecademy.com/resources/blog/advanced-python-code-challenges/
'''


def string_difference(a:str, b:str):
    '''Finds the difference between two strings. Second string must be an 
    anogram of the first with one additional letter.\n
    Required parameters:
    a (str): the first string
    b (str): the second string
    '''
    a = list(a)
    b = list(b)
    a.sort()
    b.sort()
    for i in range(len(a)):
        if a[i] != b[i]:
            return b.pop(i)


if __name__ == '__main__':
    a = 'eueiieo'
    b = 'iieoedue'

    print(string_difference(a, b))
