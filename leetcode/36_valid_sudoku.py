class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # validate rows
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in seen:
                        return False
                    else:
                        seen.add(board[i][j])

        # validate cols
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[j][i] != ".":
                    if board[j][i] in seen:
                        return False
                    else:
                        seen.add(board[j][i])

        # validate 3x3 box
        start_points = [
            [0, 0],
            [0, 3],
            [0, 6],
            [3, 0],
            [3, 3],
            [3, 6],
            [6, 0],
            [6, 3],
            [6, 6],
        ]
        return True


if __name__ == "__main__":
    sol = Solution()
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]

    sol.isValidSudoku(board)
    # assert sol.isValidSudoku(board)
    board = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]

    sol.isValidSudoku(board)

    # assert not sol.isValidSudoku(board)
