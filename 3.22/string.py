s= ""
string = 'zdr1129hcj1205WXHnizyiqmyitFORWER'
for str in string:
    if str <= 'z'and str >='a':
        s=s+chr(ord(str)-32)
    elif str >= 'A' and str <= 'Z':
        s=s+chr(ord(str)+32)
    else:
        s=s+str
print(s)