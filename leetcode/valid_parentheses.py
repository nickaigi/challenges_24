"""
20: Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true
"""
from typing import List, Dict


class Solution:
    def isValid(self, s: str) -> bool:
        result: List[str] = []
        parens: Dict[str, str] = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for char in s:
            if char in '({[':
                result.append(char)
            else:
                if not result or parens[char] != result.pop():
                    return False
        return len(result) == 0

if __name__ == '__main__':
    solution = Solution()
    # Example 1
    print(solution.isValid("()"))  # Output: True

    # Example 2
    print(solution.isValid("()[]{}"))  # Output: True

    # Example 3
    print(solution.isValid("(]"))  # Output: False

    # Example 4
    print(solution.isValid("([])"))  # Output: True

    # Test case with nested brackets
    print(solution.isValid("({[]})"))  # Output: True

    # Test case with unmatched opening bracket
    print(solution.isValid("({[]}"))  # Output: False

    # Test case with unmatched closing bracket
    print(solution.isValid("({[]}))"))  # Output: False

    # Test case with empty string
    print(solution.isValid(""))  # Output: True
