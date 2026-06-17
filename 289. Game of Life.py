class Solution:

    def gameOfLife(self, board):

        rows = len(board)
        cols = len(board[0])

        copyBoard = [row[:] for row in board]

        directions = [
            (-1,-1), (-1,0), (-1,1),
            (0,-1),          (0,1),
            (1,-1),  (1,0),  (1,1)
        ]

        for r in range(rows):
            for c in range(cols):

                live_neighbors = 0

                for dr, dc in directions:

                    nr = r + dr
                    nc = c + dc

                    if (
                        0 <= nr < rows and
                        0 <= nc < cols and
                        copyBoard[nr][nc] == 1
                    ):
                        live_neighbors += 1

                if copyBoard[r][c] == 1:

                    if live_neighbors < 2 or live_neighbors > 3:
                        board[r][c] = 0

                else:

                    if live_neighbors == 3:
                        board[r][c] = 1


board = [
    [0,1,0],
    [0,0,1],
    [1,1,1],
    [0,0,0]
]

obj = Solution()

obj.gameOfLife(board)

for row in board:
    print(row)