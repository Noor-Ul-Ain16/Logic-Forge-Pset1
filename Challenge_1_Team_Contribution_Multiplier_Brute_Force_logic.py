def team_contributions_multiplier(contributions):
    #input=[1,2,3,4]
    #output=[24,12,8,6]
    output=[]
    n=len(contributions)
    for i in range(n):
        output+=[1]
    count=1
    k=0
    num=0
    while True:
        k=num+count
        if num+count<n:
            output[num]*=contributions[num+count]
        num+=1
        if num==n:
            num=0
            count+=1
        if count==n:
            break
    count=1
    k=0
    num=0
    while True:
        k=num-count
        if num-count>=0:
            output[num]*=contributions[num-count]
        num+=1
        if num==len(contributions):
            num=0
            count+=1
        if count==len(contributions):
            break

    print(output)


team_contributions_multiplier([1,2,3,4])
team_contributions_multiplier( [-1, 1, 0, -3, 3])

