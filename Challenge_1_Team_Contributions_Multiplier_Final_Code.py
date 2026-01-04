def team_contributions_multiplier(contributions):
    #input=[1,2,3,4]
    #output=[24,12,8,6]
    output=[1]
    product=1
    for i in range(1,len(contributions)):
        product=product*contributions[i-1]
        output+=[product]
    product=1
    for i in range(len(contributions)-2,-1,-1):
        product = product * contributions[i + 1]
        output[i]*=product
    return output


print(team_contributions_multiplier([1, 2, 3, 4]))
print(team_contributions_multiplier([-1, 1, 0, -3, 3]))




