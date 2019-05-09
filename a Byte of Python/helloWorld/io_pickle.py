import pickle

shoplistfile = 'shoplist.data'
shoplist = ['apple', 'mango', 'carrot']

f = open(shoplistfile, 'wb')
pickle.dump(shoplist, f)
f.close()

del shoplist

f = open(shoplistfile, 'rb')    # 这里不能写'b'
storedlist = pickle.load(f)
print(storedlist)
f.close()
