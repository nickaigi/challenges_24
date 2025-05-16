from typing import List


class Solution:

    def generate(self, numRows: int) -> List[List[int]]:
        first_row = [1]
        rows = [first_row]

        for _ in range(1, numRows):
            row = [1]
            for i in range(1, len(rows[-1])):
                num = rows[-1][i-1] + rows[-1][i]
                row.append(num)
            row.append(1)
            rows.append(row)
        return rows

    def generate_nicks(self, numRows: int) -> List[List[int]]:
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
