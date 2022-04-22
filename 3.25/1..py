number = float(input("please enter a number:"))
number1 = str(number)
flag =False
count =0
for i in number1:
    if i == '.':
        flag=True
        continue
    if flag:
        count+=1
print(count)
        


