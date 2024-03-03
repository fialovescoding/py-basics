# Program to check if a number is present in the list

import random
import timeit

NUM_MAX = 100
n = 10

# Generates a list with n numbers in the range 0 to NUM_MAX
num_list = random.sample(range(0, NUM_MAX), n)
print(num_list)

# Write the code to search if p is in the list
def linear_search(num_2_search, list_of_nums):
    for p in list_of_nums:
        if num_2_search == p :
            return True
    return False

# Test code
p = random.randint(0, NUM_MAX)
print(f'Searching {p}...')
p_found_in_list = linear_search(num_2_search=p, list_of_nums=num_list) #(p in num_list)
print(p_found_in_list)