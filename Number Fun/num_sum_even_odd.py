n = 6
ab = 0
sum = 0
e=0
o=0

while ab < n:
    ab = ab + 1
    sum = sum + ab
    print (ab)

    rem = ab % 2

    if rem == 0:
        e = e + ab
        print("even")
    else:
        o = o + ab
        print("odd")

print("Even = ", e, ", Odd = ", o)

print("The sum is = ", sum)