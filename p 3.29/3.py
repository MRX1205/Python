key = '55624569645'
passwd = input("pleasr enter you password: ")
mim = ' '
for i in range(len(passwd)):
    mim = mim +key[int(passwd[i])]
print(mim)
