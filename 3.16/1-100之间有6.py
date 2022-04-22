#1-100 包含6和6的倍数打印输出求和
i=1
sum =0
while i <101:
    if '6' in str(i) or i%6 == 0:
        print(i)
        sum = sum+i
    i+=1
print("结果是：",sum)