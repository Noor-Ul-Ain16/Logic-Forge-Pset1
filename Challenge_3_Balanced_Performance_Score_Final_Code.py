def balanced_performance_score(scoresA, scoresB):
    total_length = len(scoresA) + len(scoresB)
    ptr_A = 0
    ptr_B = 0
    index_moved = 0

    if total_length % 2 != 0:
        median_index = (total_length + 1) // 2

        while ptr_A < len(scoresA) and ptr_B < len(scoresB):
            if scoresA[ptr_A] < scoresB[ptr_B]:
                index_moved += 1
                if index_moved == median_index:
                    return scoresA[ptr_A]
                ptr_A += 1
            else:
                index_moved += 1
                if index_moved == median_index:
                    return scoresB[ptr_B]
                ptr_B += 1

        while ptr_A < len(scoresA):
            index_moved += 1
            if index_moved == median_index:
                return scoresA[ptr_A]
            ptr_A += 1

        while ptr_B < len(scoresB):
            index_moved += 1
            if index_moved == median_index:
                return scoresB[ptr_B]
            ptr_B += 1

    else:
        median_index_1 = total_length // 2
        median_index_2 = median_index_1 + 1
        median_1 = 0
        median_2 = 0

        while ptr_A < len(scoresA) and ptr_B < len(scoresB):
            if scoresA[ptr_A] < scoresB[ptr_B]:
                index_moved += 1
                if index_moved == median_index_1:
                    median_1 = scoresA[ptr_A]
                if index_moved == median_index_2:
                    median_2 = scoresA[ptr_A]
                    return (median_1 + median_2) / 2
                ptr_A += 1
            else:
                index_moved += 1
                if index_moved == median_index_1:
                    median_1 = scoresB[ptr_B]
                if index_moved == median_index_2:
                    median_2 = scoresB[ptr_B]
                    return (median_1 + median_2) / 2
                ptr_B += 1

        while ptr_A < len(scoresA):
            index_moved += 1
            if index_moved == median_index_1:
                median_1 = scoresA[ptr_A]
            if index_moved == median_index_2:
                median_2 = scoresA[ptr_A]
                return (median_1 + median_2) / 2
            ptr_A += 1

        while ptr_B < len(scoresB):
            index_moved += 1
            if index_moved == median_index_1:
                median_1 = scoresB[ptr_B]
            if index_moved == median_index_2:
                median_2 = scoresB[ptr_B]
                return (median_1 + median_2) / 2
            ptr_B += 1

print("Outputs:\n")
print("ScoresA:[1,3]\nScoresB:[2]\nOutput: ",balanced_performance_score([1,3],[2]))

print("\nScoresA:[1,3]\nScoresB:[2,4]\nOutput: ",balanced_performance_score([1,3],[2,4]))

print("\nScoresA:[1,2]\nScoresB:[3,4]\nOutput: ",balanced_performance_score([1,2],[3,4]))
