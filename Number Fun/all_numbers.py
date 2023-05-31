# making variable num_list
num_list = [2, 7, 4]

# making variables for 100's (h), 10's (t) and 1's (o) through for loops
for o in num_list:
    for t in num_list:
        for h in num_list:
            # If t > o and h is an even number, print n
            if t > o and h % 2 == 0:
                # n is the number formed using place variables
                n = h * 100 + t * 10 + o * 1
                print(n)
            else:
                # Else, selected condition between h,t,o not met
                print("condition not met", h, t, o)