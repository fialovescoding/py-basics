n = 3
k = 2

while k < n:
    rem = n % k
    if rem == 0:
        print(n, "is not prime, since it divides by ", k)
        break
    else:
        #print(k)
        k = k + 1

if rem > 0:
    print(n, "is prime")