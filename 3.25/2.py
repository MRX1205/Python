#一段英文判断单词的个数 把所有的字母大写和小写 首字母大写 找一下单词里面有多少个is 统计里面的is的个数
sentens = input("pleas enter ana sentens:")
count =1
for i in sentens:
    if i == ' ':
        count+=1
print(count)
print(sentens.upper())
print(sentens.lower())
print(sentens.capitalize())
print(sentens.title())
print(sentens.count("is"))

