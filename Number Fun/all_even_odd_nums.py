n = 15
e = 0
if e == 1:
    start = 2
    if n % 2 == 0:
        stop = n + 1
    else:
        stop = n
else:
    start = 1
    if n % 2 == 0:
        stop = n
    else:
        stop = n + 1

for i in range (start, stop, 2):
    print (i)

 
