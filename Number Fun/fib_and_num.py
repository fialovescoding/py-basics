from tkinter import N


N = 5
D = 13
k = 0
a = 0
b = 1
while k < N:
    c = a + b
    a = b
    b = c
    rem = c % D

    if rem == 0:
        print (c)
        k = k + 1
