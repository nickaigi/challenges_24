"""
Input 
[2]
3

Expected: -1

Input 
[5,7,8]
15

Expected: 2

Input 
[186,419,83,408]
6249

Expected: 20

Input 
[1, 2, 5]
11

Expected: 3

"""
def coin_change(coins, amount):
    change = []
    for coin in coins:
        values = amount // coin
        bal = amount % coin
        if bal != 0:
            if bal in coins:
                print('bal', bal)
                change.append(values + 1)
            else:
                continue
        else:
            change.append(values)
    if len(change) > 0:
        return min(change)
    return -1
