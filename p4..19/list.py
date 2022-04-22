score = [73,90,36,85,67,95,36,18,10,36,0,36]
averger = sum(score)/score.__len__()
print(averger)

score.append(86)
print(score)




score1 = [ 25,36,31,45]
score2 = [15,3,5,1,6,6,66,5,5,5,6,5,5,54,4,45,5]
score3 =[12,44,45,27]
scoret =[score1[:],score2[:],score3[:]]
print(scoret)


n = score2.count(5)
print(n)
for i in [0,7]:
    score2.remove(5)

print(score2)