def password_recovery_window(log,pattern):
    # log = "ADOBECODEBANC", pattern = "ABC"
    if not log:
        return ""
    pattern_frequency={}
    for letter in pattern:
        if letter not in pattern_frequency:
            pattern_frequency[letter]=1
        else:
            pattern_frequency[letter]+=1
    sliding_window={}
    left=0
    right=0
    conditions_met=0
    smallest_window=""
    for i in range(len(log)):
        if log[i] in pattern:
            if log[i] not in sliding_window:
                sliding_window[log[i]]=1
            else:
                sliding_window[log[i]]+=1
            if sliding_window[log[i]] == pattern_frequency[log[i]]:
                conditions_met+= 1
        right+=1
        if conditions_met==len(pattern_frequency):
          while True:
             temp_window=log[left:right]
             temp=log[left]
             left+=1
             if temp in pattern:
                 if not smallest_window or len(temp_window) < len(smallest_window):
                     smallest_window = temp_window
                 sliding_window[temp] -= 1
                 if temp in pattern and sliding_window[temp] < pattern_frequency[temp]:
                     conditions_met -= 1
                 if conditions_met < len(pattern_frequency):
                     break
             if left==right:
                      break
    if smallest_window:
        return smallest_window
    else:
        return ""

print("Outputs:\n\nlog:'ADOBECODEBANC' pattern: 'ABC'\n answer string:",password_recovery_window("ADOBECODEBANC","ABC"))
print("\nlog:'a' pattern:'aa'\n answer string:",password_recovery_window("a","aa"))
print("\nlog = 'a', pattern = 'a'\n answer string: ",password_recovery_window('a','a'))




