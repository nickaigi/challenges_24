"""

Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

If multiple answers are possible, return any of them.

It is guaranteed that the length of the answer string is less than 104 for all the given inputs.

 

Example 1:
Input: numerator = 1, denominator = 2
Output: "0.5"

Example 2:
Input: numerator = 2, denominator = 1
Output: "2"

Example 3:
Input: numerator = 4, denominator = 333
Output: "0.(012)"
"""
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        result = []
        # Determin eif result should be negative
        # XOR returns True if signs are different
        is_negative = (numerator > 0) ^ (denominator > 0)
        if is_negative:
            result.append("-")

        # work with absolute values to simplify calculation
        dividend, divisor = abs(numerator), abs(denominator)

        # add the integer part
        result.append(str(dividend // divisor))

        # calculate the remainder
        remainder = dividend % divisor

        if remainder == 0:
            return "".join(result)

        # add decimal point for fraction part
        result.append(".")

        # use a dictionary to track remainders and their positions
        # used to detect repeating decimals
        remainder_positions = {}

        while remainder:
            # store current remainder's position in result
            remainder_positions[remainder] = len(result)

            # perform long division: multiply remainder by 10
            remainder *= 10

            # add the next digit to result
            result.append(str( remainder // divisor))

            # calculate the new remainder
            remainder = remainder % divisor

            # check if we've seen this remainder before (repeating patter)
            if remainder in remainder_positions:
                # insert opening parenthesis at the start of the repeating sequence
                result.insert(remainder_positions[remainder], "(")
                # add closing parenthesis at the end
                result.append(")")
                break
        return "".join(result)
