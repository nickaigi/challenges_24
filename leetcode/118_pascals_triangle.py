from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1], [1, 1]]

        for i in range(2, numRows):
            row = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    prev = res[i-  1]
                    val = prev[j - 1]  + prev[j]
                    row.append(val)
            res.append(row)
        return res


if __name__ == '__main__':
    sol = Solution()
    ans = sol.generate(5)
    print(ans)
