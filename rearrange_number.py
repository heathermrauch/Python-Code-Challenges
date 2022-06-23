'''
Rearrange the number

To complete this challenge, write a function that accepts a number as a
parameter. The function should return a number that’s the difference between
the largest and smallest numbers that the digits can form in the number.

For example, if the parameter is "213", the function should return "198", which
is the result of 123 subtracted from 321.

Original Challenge found here:
https://www.codecademy.com/resources/blog/advanced-python-code-challenges/
'''


def rearrange_number(number:int):
    digits = list(str(number))
    min_num = ''.join(sorted(digits))
    max_num = ''.join(sorted(digits, reverse=True))
    return int(max_num) - int(min_num)


if __name__ == '__main__':

    number = 213
    print(rearrange_number(number))
