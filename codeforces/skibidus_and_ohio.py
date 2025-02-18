"""

Skibidus and Ohio

Skibidus is given a string s that consists of lowercase Latin letters. If s contains more than 1 letter, he can:

Choose an index i (1≤i≤|s|−1 , |s| denotes the current length of s) such that si=si+1 . Replace si with any lowercase Latin letter of his choice. Remove si+1 from the string.

Skibidus must determine the minimum possible length he can achieve through any number of operations.

Input
The first line contains an integer t
 (1≤t≤100) — the number of test cases.

The only line of each test case contains a string s (1≤|s|≤100). It is guaranteed s only contains lowercase Latin letters.

Output
For each test case, output an integer on the new line, the minimum achievable length of s.
"""


from typing import List


def find_min_len(s: str) -> int:
    n = len(s)
    while n > 1:
    for i in range(1, n):
        if s[i - 1] == s[i]:
            s = s[0:i-1] + s[i+1:]
    return n


if __name__ == '__main__':
    t: int = int(input())
    s_arr: List[str] = []

    for i in range(t):
        s_arr.append(input())

    for s in s_arr:
        res = find_min_len(s)
