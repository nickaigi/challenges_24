if __name__ == '__main__':
    with open('text_files/pi_digits.txt') as f:
        for line in f:
            print(line.rstrip())
