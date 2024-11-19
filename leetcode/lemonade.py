def lemonadeChange(bills):
    """
    :type bills: List[int]
    :rtype: bool
    """
    note_5 = 0
    note_10 = 0
    note_20 = 0
    for b in bills:
        print(note_5, note_10, note_20)

        if b == 5:
            note_5 = note_5 + 1
        elif b == 10:
            if note_5 >= 1:
                note_10 = note_10 + 1
                note_5 = note_5 - 1
            else:
                return False
        else:
            if note_10 >= 1 and note_5 >= 1:
                note_20 = note_20 + 1
                note_5 = note_5 - 1
                note_10 = note_10 - 1
            elif note_5 >= 3:   
                note_20 = note_20 + 1
                note_5 = note_5 - 3
            else:
                return False
    
    return True
    
print(lemonadeChange([5,5,5,10,20]))