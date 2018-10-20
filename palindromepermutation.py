def palindrom_permutation(str_input):
    input_dict = {}
    for element in str_input:
        if element in input_dict:
            input_dict[element] += 1
        else:
            input_dict[element] = 1

    total_odds = 0
    for value in input_dict.values():
        if value % 2 != 0:
            if total_odds == 0:
                total_odds = 1
            else:
                return False
    return True

print(palindrom_permutation("civic"))
print(palindrom_permutation("livci"))
print(palindrom_permutation("ivicc"))
