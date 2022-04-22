score =tuple([2,3,6,1,7,8,10,3,5,6])
studentscore = 0
len= score.__len__()-2
for i in range(10):
    if min(score) < score[i] < max(score):
        studentscore += score[i]
totalstuscore = studentscore/len
print(totalstuscore)

