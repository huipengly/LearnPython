def reverse(text):
    return text[::-1]


def is_palindrome(text):
    return text == reverse(text)


something = input('Enter text: ')
if is_palindrome(something):
    print('Yest, it is a palindrome')
else:
    print('No, it is not a palindrome')
