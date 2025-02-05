"""
1790. Check if One String Swap Can Make Strings Equal

You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.

Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.

Example 1:

Input: s1 = "bank", s2 = "kanb"
Output: true
Explanation: For example, swap the first character with the last character of s2 to make "bank".

Example 2:

Input: s1 = "attack", s2 = "defend"
Output: false
Explanation: It is impossible to make them equal with one string swap.

Example 3:

Input: s1 = "kelb", s2 = "kelb"
Output: true
Explanation: The two strings are already equal, so no string swap operation is required.

Example 4:
Input: s1 = "caa", s2 = "aaz"
Output: true
"""


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True
        # Find the indices where the characters differ
        diff_indices = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff_indices.append(i)
        
        # If there are exactly two mismatches, check if swapping makes the strings equal
        if len(diff_indices) == 2:
            i, j = diff_indices
            if s1[i] == s2[j] and s1[j] == s2[i]:
                return True
        
        # If there are no mismatches, return True
        if len(diff_indices) == 0:
            return True
        
        # Otherwise, return False
        return False
