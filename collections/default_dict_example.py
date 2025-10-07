from collections import defaultdict

def example_one() -> None:
    """
    - using list as the default_factory, it is easy to group a sequence of
    key-value pairs into a dictionary of lists
    - when each key is encountered for the first time, it is not already in the
    mapping; so an entry is automatically created using the default_factory
    function which returns an empty list.
    - The list.append() operation then attaches the value to the new list.
    - When keys are encountered again, the look-up proceeds normally (returning
    the list for that key) and the list.append() operation adds another value
    to the list
    """

    s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
    d = defaultdict(list)
    for k, v in s:
        d[k].append(v)

    print(sorted(d.items()))
    print(d)

def example_two() -> None:
    """
    - Setting the default_factory to 'int' makes the defaultdict useful for
    counting.
    """
    s = 'mississippi'
    d = defaultdict(int)
    for k in s:
        d[k] += 1
    print(sorted(d.items()))


if __name__ == '__main__':
    example_one()
    example_two()
