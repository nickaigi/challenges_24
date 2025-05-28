"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 
Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

Example 2:
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

Constraints:

0 <= x <= 231 - 1
"""
class Solution:
    def mySqrt(self, x: int) -> int:
        """Use binary search"""
        L, R = 1, x

        while L <= R:
            M = (L + R) // 2
            m_squared= M * M
            if m_squared == x:
                return M
            if m_squared < x:
                L = M + 1
            elif m_squared > x:
                R = M - 1
        return R

if __name__ == '__main__':
    sol = Solution()
    assert 2 == sol.mySqrt(4)
    assert 2 == sol.mySqrt(8)
