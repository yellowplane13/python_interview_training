import math
def finalinstances(score, team_size, k):
    #score [ 12,17,13,6,90,20,34] k = 3 teamsize = 2
    team = []
   
    
    while len(team)< team_size:
        max1 = 0
        index1 = 0
        for i in range(0,k+1):
            if score[i] > max1:
                max1 = score[i]
                index1 = i
        for j in range(-1,-k-1,-1):
            if score[j] > max1:
                max1 = score[j]
                index1 = j
        team.append(max1)
        score.pop(index1)
        print(score, "new score after reduction of largest size")
        print(team, "team array in this loop")
    print(team)

finalinstances([12,17,13,6,90,20,34], 2, 3)