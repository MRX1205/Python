a = int(input("please enter a:"))
b = int(input("please enter b:"))
#比较运算符
if(a!=b):
    if(a>b):
        print("a>b")
    else:
        print("a<b")
else:
    print("a=b")

#+ - * / %
k = input("symbol:")
if k=='+':
    print(a+b)
elif k=='-':
    print(a-b)
elif k =='*':
    print(a*b)
elif k =='/':
    print(a/b)
elif k =='%':
    print(a%b)
else:
    print("it is worng")