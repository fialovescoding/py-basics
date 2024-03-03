num_list = [3,4,2,5,7]
len_list = len(num_list)

# given a list of numbers find all possible odd length of sublist
losl = 1

while losl <= len_list:
    print(losl)

    i = 0
    for i in range(0, len_list - losl + 1):
        j = i + losl
        print(num_list[i:j])

    losl = losl + 2