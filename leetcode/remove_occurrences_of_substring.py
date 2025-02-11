"""
1910. Remove all occurrences of a substring

Given two strings s and part, perform the following operation on s until all occurrences of the substring part are removed:

Find the leftmost occurrence of the substring part and remove it from s.
Return s after removing all occurrences of part.

A substring is a contiguous sequence of characters in a string.

Example 1:

Input: s = "daabcbaabcbc", part = "abc"
Output: "dab"
Explanation: The following operations are done:
- s = "daabcbaabcbc", remove "abc" starting at index 2, so s = "dabaabcbc".
- s = "dabaabcbc", remove "abc" starting at index 4, so s = "dababc".
- s = "dababc", remove "abc" starting at index 3, so s = "dab".
Now s has no occurrences of "abc".

Example 2:

Input: s = "axxxxyyyyb", part = "xy"
Output: "ab"
Explanation: The following operations are done:
- s = "axxxxyyyyb", remove "xy" starting at index 4 so s = "axxxyyyb".
- s = "axxxyyyb", remove "xy" starting at index 3 so s = "axxyyb".
- s = "axxyyb", remove "xy" starting at index 2 so s = "axyb".
- s = "axyb", remove "xy" starting at index 1 so s = "ab".
Now s has no occurrences of "xy".
"""
class Solution:
    def removeOccurrences_nick(self, s: str, part: str) -> str:
        step = len(part)
        i = 0
        while part in s:
            curr = s[i: i + step]
            if curr == part:
                s = s[0:i] + s[i+step:]
                i = 0
            else:
                i += 1
        return s

    def removeOccurrences(self, s: str, part: str) -> str:
        # Continue removing occurrences of 'part' as long as it exists in 's'
        while part in s:
            # Find the index of the leftmost occurrence of 'part'
            part_start_index = s.find(part)

            # Remove the substring 'part' by concatenating segments before and after 'part'
            s = s[:part_start_index] + s[part_start_index + len(part) :]

        # Return the updated string after all occurrences are removed
        return s
