def sum_of_digits(n):
    p = n
    sod = 0
    if n == 0:
        return 0
    while p != 0:
        r = p % 10
        p = p // 10
        sod = sod + r
        
    return sod

def count(lowLimit, highLimit):
    boxes = {}
    for i in range(lowLimit, highLimit + 1):
        b = sum_of_digits(i)
        if b in boxes:
            boxes[b] += 1
        else:
            boxes[b] = 1

    max_count = 0
    for ball_count in list(boxes.values()):
        if max_count < ball_count:
            max_count = ball_count
    
    return max_count

print(count(1, 10))