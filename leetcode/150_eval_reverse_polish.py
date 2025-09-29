import math
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stk = []
        for t in tokens:
            if t in '+-*/':
                b, a = stk.pop(), stk.pop()
                if t == '+':
                    stk.append(a + b)
                elif t == '-':
                    stk.append(a - b)
                elif t == '*':
                    stk.append(a * b)
                else:
                    division = a / b
                    if division < 0:
                        stk.append(math.ceil(division))
                    else:
                        stk.append(int((division)))
            else:
                stk.append(int(t))
        return stk[0]
