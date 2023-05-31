# Given two numbers, L and H, such that L < H, find pL and pH so that pL is the smallest prime number and pL > L, and pH is the largest prime number and pH < H

# Next, given another number M, print the prime numbers starting from pL, increasing till pH, then reducing towards pL, and continuing this wave until M prime numbers have been printed

# e.g., L = 1, H = 12, M = 10, then output should be pL = 2, pH = 11 and print: 2, 3, 5, 7, 11, 7, 5, 3, 2, 3, 5
L = 3
H = 12
M = 10






# Function to check if n is prime or not
def check_prime(n):
    # Corner case
    if n == 1:
        return False

    if n == 2:
        return True
    
    # Below code works only for n > 2
    k = 2

    # if k < n and rem is 0 print (n, "is not prime, since it divides by ", k) else k = k + 1
    while k < n:    
        rem = n % k
        if rem == 0:
            # print (n, "is not prime, since it divides by ", k)
            return False
            break
        else:
            #print(k)
            k = k + 1

    # if rem > 0 print (n, "is prime")
    if rem > 0:
        # print(n, "is prime")
        return True    
    


for n in range(1, 20):
    is_prime = check_prime(n)
    print(n, is_prime)

pL = L + 1
print('Start value of pL=', pL)

while check_prime(pL) == False:
    pL = pL + 1

print ('Found smallest prime=', pL)

pH = H - 1

while check_prime(pH) == False:
    pH = pH - 1 

print ('Found bigest prime=',pH)
print('End value of pH=', pH)
P = L + 1
Plist = [ ]
while P < H :
if check_prime (P) = True:
Plist.append(P)
print (Plist)
M = 8
Q = 0
S = len (Plist) pL 
for n in range (0,M)
print (Plist [Q])
add = 1
Q = Q + add
if Q = S:
add = - 1
if Q = 0:
add = 1