def check_combinations(s1, s2):
    input_strs = s1 + s2
    combined_strs = input_strs + input_strs
    balanced = True
    for i in range(len(combined_strs)):
        if combined_strs[i] == combined_strs[i + 1]:
            balanced = False
            break
    return 'No' if balanced else 'Yes'