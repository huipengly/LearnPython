# list里可以混合存储任意类型
# This is my shopping list
shoplist = ['apple', 'mango', 'carrot', 'banana']

print('I have', len(shoplist), 'items to purchase.')

print('These items are', end=' ')
for item in shoplist:
    print(item, end=' ')

print('\nI also have to buy rice.')
shoplist.append('rice')
print('My shopping list is now', shoplist)

print('I will sort my list now')
# Then, we sort the list by using the sort method of the list.
# It is important to understand that this method affects the list
# itself and does not return a modified list - this is different
# from the way strings work. This is what we mean by saying that
# lists are mutable and that strings are immutable.
shoplist.sort()
print('Sorted shopping list is', shoplist)

print('The first item  I will buy is', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('I bought the', olditem)
print('My shopping list is now', shoplist)
