# Given a list of numbers
num_list = [0,6,1,7,9,12,5,6,21,7,8]

# And a number to be searched in above list
n = 8

# Seach the position of the number in the list
p = 0
for s in num_list:
    if s == n:
        break
    p = p + 1

# Print the position
print("position of n = ", p)