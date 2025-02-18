if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        b = list(map(int, input().split()))
        valid = True
        for i in range(len(b) - 2):
            if b[i] == 1 and b[i+1] == 0 and b[i+2] == 1:
                valid = False
                break
        print("YES" if valid else "NO")
