n = 1
p = 25
r = 2

if n < 5:
    print("print at least 5 numbers :)")
else:
    print("This is the output:")

    for k in range(1, n + 1):
        rem = k % p
        if rem == r:
            print (k)