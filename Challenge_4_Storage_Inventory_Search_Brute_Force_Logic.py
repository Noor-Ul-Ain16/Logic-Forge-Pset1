def find_kth_smallest_element(matrix,n,element):
    low=matrix[0][0]
    high=matrix[n-1][n-1]
    count=0
    r=n-1
    c=0
    while low<=high:
        while r>=0 and c<n:
            curr = matrix[r][c]
            mid_weight = (low + high) // 2
            if mid_weight <= curr:
                c += 1
                count+=r+c
            else:
                r -= 1
                count+=r+c
        if count>element:
            low=mid_weight
        elif count<element:
            high=mid_weight
        else:
            return low


    return -1

print(find_kth_smallest_element([[1, 5, 9], [10, 11, 13], [12, 13, 15]],3,8))



