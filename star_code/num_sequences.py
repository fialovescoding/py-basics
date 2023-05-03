# Generate number sequences using remainders
n = 25

for px in range(1, n):
    for rx in range(1, n):
        lst = [k for k in range(1, n + 1) if k % px == rx]
        if len(lst) > 0:
            print(px, rx, lst)