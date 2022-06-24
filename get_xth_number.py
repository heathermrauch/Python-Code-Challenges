'''
Find the Xth Number In Order

Write a function, `getX`, that given an integer `x` and a list `nums` returns
the Xth number if the list was in sorted order. In other words, the Xth
smallest number.

Function Name: `getX`

Input: An integer, `x`, and an unsorted list of integers `nums` that aren't
necessarily distinct

Output: The integer corresponding to the Xth number in the sorted list

Example:
```py
getX(2, [5, 10, -3, -3, 7, 9]) => -3
```
The second number in order is -3
```py
getX(4, [5, 10, -3, -3, 7, 9]) =>
```
The fourth number in order is 7.

Note that this assumes the first number is position 1, not 0. If the input `x`
is greater than the length of the list, or `nums` is empty, return `0`.

Attempt a solution as close to linear `O(n)` (where `n` is the length of `nums`
) time as possible.

Original code challenge located here:
https://www.codecademy.com/code-challenges/code-challenge-find-xth-number-in-order-python
'''


def getX(x, nums):
    if len(nums) == 0 or x > len(nums):
        return 0
    else:
        return sorted(nums)[x-1]


if __name__ == '__main__':

    print(getX(2, [6, 3, -1, 5]))
