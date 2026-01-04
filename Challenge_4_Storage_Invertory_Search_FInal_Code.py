def find_kth_smallest_element(matrix, n, element):
    low = matrix[0][0]
    high = matrix[n-1][n-1]
    while low < high:
        mid_weight = (low + high) // 2
        count = 0
        r = n - 1
        c = 0
        while r >= 0 and c < n:
            curr = matrix[r][c]

            if curr <= mid_weight:
                count += r + 1
                c += 1
            else:
                r -= 1
        if count < element:
            low = mid_weight + 1
        else:
            high = mid_weight

    return low


print("\nOutput\n8th Smallest Element: ",find_kth_smallest_element(
    [[1, 5, 9], [10, 11, 13], [12, 13, 15]], 3, 8))
