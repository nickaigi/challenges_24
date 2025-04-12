"""
You are given two positive integers low and high.

An integer x consisting of 2 * n digits is symmetric if the sum of the first n digits of x is equal to the sum of the last n digits of x.
Numbers with an odd number of digits are never symmetric.

Return the number of symmetric integers in the range [low, high].

Example 1:

Input: low = 1, high = 100
Output: 9
Explanation: There are 9 symmetric integers between 1 and 100: 11, 22, 33, 44, 55, 66, 77, 88, and 99.

Example 2:

Input: low = 1200, high = 1230
Output: 4
Explanation: There are 4 symmetric integers between 1200 and 1230: 1203, 1212, 1221, and 1230.



Intuition
Enumerate all numbers from low to high:

If it is a two-digit number and is a multiple of 11, then it is a symmetric integer.
If it is a four-digit number, calculate the sum of the thousands and hundreds digits, as well as the sum of the tens and ones digits. If they are equal, it is a symmetric (even) integer.
Finally, it returns the number of symmetric integers in the range.

"""

class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res = 0
        for a in range(low, high + 1):
            if a < 100 and a % 11 == 0:
                res += 1
            if 1000 <= a < 10000:
                left = a // 1000 + a % 1000 //100
                right = a % 100 // 10 + a % 10
                if left == right:
                    res +=1
        return res

if __name__ == '__main__':
    sol = Solution()
    assert 9 == sol.countSymmetricIntegers(low=1, high=100)
