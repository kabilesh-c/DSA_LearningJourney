class Solution:

    def isValidSudoku(self, board):

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = {}

        for r in range(9):
            for c in range(9):

                value = board[r][c]

                if value == ".":
                    continue

                box = (r // 3, c // 3)

                if box not in boxes:
                    boxes[box] = set()

                if (
                    value in rows[r]
                    or value in cols[c]
                    or value in boxes[box]
                ):
                    return False

                rows[r].add(value)
                cols[c].add(value)
                boxes[box].add(value)

        return True


board = [
["5","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]
]

obj = Solution()
print(obj.isValidSudoku(board))