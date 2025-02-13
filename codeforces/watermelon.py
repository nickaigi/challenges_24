def can_divide_watermelon(w: int):
    if w % 2 == 0 and w > 2:
        return "YES"
    return "NO"

if __name__ == '__main__':
    w = int(input())
    print(can_divide_watermelon(w))
