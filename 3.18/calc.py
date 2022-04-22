str = 'just like you a beautyful girl'
for chr in str:
    if chr == 'a':
        break
    else:
        print(chr,end=' ')
print( )
for chr2 in str:
    if chr2 == 'a':
        continue
    else:
        print(chr2,end=' ')