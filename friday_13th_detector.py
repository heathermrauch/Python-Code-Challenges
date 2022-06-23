'''
Write a Friday 13th detector

Create a function in Python that accepts two parameters. They’ll both be
numbers. The first will be the month as a number, and the second will be the
four-digit year. The function should parse the parameters and return True if
the month contains a Friday the 13th and False if it doesn’t.

Original Challenge found here: 
https://www.codecademy.com/resources/blog/advanced-python-code-challenges/
'''

import datetime


def has_friday_13(month:int, year:int):
    '''Indicates whether the specified month-year contains Friday the 13th\n
    Required Parameters:
    month (int): the numeric representation of the month to check
    year (int): the four digit year to check 
    '''
    date = datetime.date(year, month, 13)
    day = date.strftime('%A')
    return day == 'Friday'


if __name__ == '__main__':

    month = 5
    year = 2022

    print('May 2022:', has_friday_13(month, year))

    month = 4
    year = 2022

    print('April 2022:', has_friday_13(month, year))
