# n is a number which we are cheeking if it is a prime number 
n = 103

# k
k = 2

# if k < n and rem is 0 print (n, "is not prime, since it divides by ", k) else k = k + 1
while k < n:
    rem = n % k
    if rem == 0:
        print (n, "is not prime, since it divides by ", k)
        break
    else:
        #print(k)
        k = k + 1

# if rem > 0 print (n, "is prime")
    
if rem > 0:
    print(n, "is prime")