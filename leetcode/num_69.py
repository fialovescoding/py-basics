n = 9999

# [1] Make a list to store digits of n
dig_list = []
while n != 0:
    r = n % 10
    n = n // 10
    # Insert the digit to list
    dig_list.insert(0,r)
    print (dig_list)

# dig_list = [9, 9, 9, 9,]

l = len(dig_list)

# [2] Replace the 1st 6
for i in range(0, l):
    if dig_list[i] == 6:
        dig_list[i] = 9
        break

print(dig_list)

# [3] Compose the output number from digits
m = 10 ** (l - 1)

# Output number
p = 0
for i in range(0, l):
    p = p + m * dig_list[i]
    m = m / 10

print(int(p))