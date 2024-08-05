dickensian = input()
left_hand = "qwertasdfgzxcvb"
right_hand = "yuiophjklnm"
if dickensian[0] in left_hand:
    for ind, i in enumerate(dickensian):
        if ind % 2 == 0 and i not in left_hand:
            print("no")
            break
        if ind % 2 == 1 and i not in right_hand:
            print("no")
            break
    else:
        print("yes")
else:
    for ind, i in enumerate(dickensian):
        if ind % 2 == 0 and i not in right_hand:
            print("no")
            break
        if ind % 2 == 1 and i not in left_hand:
            print("no")
            break
    else:
        print("yes")
