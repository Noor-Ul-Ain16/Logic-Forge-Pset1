def balanced_performance_score(scoresA,scoresB):
    total_length=len(scoresA)+len(scoresB)
    if total_length%2!=0:
        median_index=((total_length+1)/2)
        ptr_A=0
        ptr_B=0
        index_moved=0
        while ptr_A<len(scoresA) and ptr_B<len(scoresB):
            if scoresA[ptr_A]<scoresB[ptr_B]:
                index_moved+=1
                if (index_moved)==median_index:
                    return scoresA[ptr_A]
                ptr_A += 1
            else:
                index_moved+=1
                if index_moved==median_index:
                    return scoresB[ptr_B]
                ptr_B += 1

    else:
        median_index_1=total_length/2
        median_1=0
        median_2=0
        ptr_A = 0
        ptr_B = 0
        index_moved = 0
        while ptr_A < len(scoresA) and ptr_B < len(scoresB):
            if scoresA[ptr_A] < scoresB[ptr_B]:
                index_moved += 1
                if (index_moved) == median_index_1:
                    median_1=scoresA[ptr_A]
                    if ptr_A+1<len(scoresA):
                       median_2=min(scoresA[ptr_A+1],scoresB[ptr_B])
                    else:
                        median_2=scoresB[ptr_B]
                ptr_A += 1
            else:
                if (index_moved) == median_index_1:
                    median_1 = scoresB[ptr_B]
                    if ptr_B+1<len(scoresB):
                      median_2=min(scoresB[ptr_B+1],scoresA[ptr_A])
                    else:
                        median_2=scoresA[ptr_A]
                ptr_B += 1
        return (median_1+median_2)/2

print(balanced_performance_score([1,3],[2]))

print(balanced_performance_score([1,2],[3,4]))

print(balanced_performance_score([1,3],[2,4]))
