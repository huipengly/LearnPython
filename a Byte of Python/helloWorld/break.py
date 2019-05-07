while True:
    s = input('Enter somethin : ')
    if s == 'quit':
        break
    print('Length of the string is', len(s))
else:   # break之后不会进入else
    print('done')
print('Done')
