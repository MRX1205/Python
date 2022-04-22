stu_score = [[73,40,65,36,25,0],[90,75,85,18,50,30]]

for h in range(2):
    stu_score_sum = 0
    for z in stu_score[h]:
        print(z,end=' ')
        h += 1
        stu_score_sum += z
    print("的总分为：",(stu_score_sum))
    print("\n")
print()
