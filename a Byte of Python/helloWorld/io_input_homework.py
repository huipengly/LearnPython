def reverse(text):
    return text[::-1]


def is_palindrome(text):
    return text == reverse(text)


forbidden = ('.', '?', '!', ':', ';', '-', '_', '(', ')', '[', ']', '...', '\'', '"', '/', ',')
something = input('Enter text: ')
# something = "Rise to vote, sir."
something = something.lower()
something = something.replace(' ', '')
s = ''
for ch in something:
    if ch not in forbidden:
        s += ch
if is_palindrome(s):
    print('Yes, it is a palindrome.')
else:
    print('No, it is not a palindrome.')
