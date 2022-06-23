'''
Prime Number Finder
Create a prime_finder() function that takes in a number, n, and returns all the
prime numbers from 1 to n (inclusive). As a reminder, a prime number is a
number that is only divisible by 1 and itself.

For example, prime_finder(11) should return [2, 3, 5, 7, 11]

Original Code Challenge located here:
https://www.codecademy.com/code-challenges/code-challenge-prime-number-finder-python
'''


def prime_finder(n:int):
    return [i for i in range(2, n+1) if all([i % j != 0 for j in range(2, i)])]


if __name__ == '__main__':

    n = 11
    print(prime_finder(n))
