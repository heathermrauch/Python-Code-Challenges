
# Friday 13th detector
# accepts 2 integers representing month and year
# returns True if month contains Friday the 13th
# Original Challenge found here: https://www.codecademy.com/resources/blog/advanced-python-code-challenges/

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
