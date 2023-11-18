from random import randint

# [1] Get 3 numbers from user: L (low), H (high) and N (no. of numbers to generate)
N = int (input("enter the value of N: "))
H = int (input("enter the value of H: "))
L = int (input("enter the value of L: "))

# [2] We want that we can generate at least 5 numbers between L and H
# If numbers are OK, print them

# [2a] P is the number of integers between L and H
P = H - L - 1

# [2b] Check if N is at least 5, and N is smaller than P
if N >= 5 and P >= N:
    print ("the value of N is: ", N)
    print ("the value of H is: ", H)
    print ("the value of L is: ", L) 
else:
    print ("print at least 5 numbers")
    exit()

# OPEN: What if 2 or more numbers generated are the same?

# [3] Generate N random numbers between L and H and store them in num_list

# [3a] First generate list of integers from L + 1 to H - 1
numlist = list(range(L + 1 , H))
# print(numlist)

# [3b] Now, pick randomly N numbers from numlist
# q counts the number of random numbers generated so far (which should be at max = N)
q = 0
len_numlist = len(numlist)
# Create an empty list to hold randomly picked numbers
randlist = []
# Run the loop till we've generated N numbers, or till no more numbers in numlist
while q < N and len_numlist > 0:
    # Generate a random index i, to pick a number from numlist
    i = randint(0, len_numlist - 1)
    # Remove the number at position i (and store in k) from numlist
    k = numlist.pop(i)
    # Add k to randlist
    randlist.append(k)
    # Increment q
    q = q + 1
    # Re-calculate length
    len_numlist = len(numlist)


# Print the rand_list and ask user to sort them in ascending order

print(randlist)
message = input("Reassemble the given list: ")
try:
    # Split user input, and convert each 'str' to 'int'
    split_input = message.split(",")
    print(split_input)

    answer_list = []
    for s in split_input:
        m = int(s)
        answer_list.append(m)

    answer_list = [int(s) for s in split_input]
    print(answer_list)
except:
    print('Some error occured')
    exit()

#TODO: Sort using only if/for/while, don't use sort function

randlist.sort()
print('expected:', randlist)

# print("The value of your input is", message)

# Check if user entered the numbers in correct order or not.
# If correct, print "Good Work", else print "Better luck next time"


#TODO: Next step, add time limit, the user must enter list in ascending order within 30 seconds