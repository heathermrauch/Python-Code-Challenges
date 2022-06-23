'''
Duplicate letter checker

Create a function in Python that accepts one parameter: a string that’s a
sentence. This function should return True if any word in that sentence
contains duplicate letters and False if not.

Original Challenge found here:
https://www.codecademy.com/resources/blog/advanced-python-code-challenges/
'''


def duplicates(sentence:str):
    words = [x.lower() for x in sentence.split()]
    for word in words:
        letters = set(word)
        if len(word) > len(letters):
            return True
    return False


if __name__ == '__main__':

    sentence = 'this is a sentence containing words with duplicate letters'
    print(duplicates(sentence))

    sentence = 'boring words with no duplicates'
    print(duplicates(sentence))
