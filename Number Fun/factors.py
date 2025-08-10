P = 13

for d in range(1, P + 1):
    if P % d == 0:
        f = P // d
        print(d, f)

# Write a function to find integer factors of a number n