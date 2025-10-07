from collections import defaultdict

if __name__ == '__main__':
    s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
    # using list as the default_factory, it is easy to group a sequence of key-value pairs into
    # a dictionary of lists
    d = defaultdict(list)
    for k, v in s:
        d[k].append(v)

    print(sorted(d.items()))
    print(d)
