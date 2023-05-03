num_list = [2, 7, 4]

for o in num_list:
    for t in num_list:
        for h in num_list:
            #cant understand
            if t > o and h % 2 == 0:
                n = h * 100 + t * 10 + o * 1
                print(n)
            else:
                print("condition not met", h, t, o)