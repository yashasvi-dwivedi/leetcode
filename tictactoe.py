class Solution(object):
    def tictactoe(self, moves):
        board = [[0] * 3 for _ in range(3)]

        is_A = True
        for r, c in moves:
            board[r][c] = "X" if is_A else "O"
            is_A = not is_A

        for i in range(3):
            if board[i][0] and board[i][0] == board[i][1] == board[i][2]:
                return "A" if board[i][0] == "X" else "B"
            if board[0][i] and board[0][i] == board[1][i] == board[2][i]:
                return "A" if board[0][i] == "X" else "B"

        if board[1][1] and (
            board[0][0] == board[1][1] == board[2][2]
            or (board[0][2] == board[1][1] == board[2][0])
        ):
            return "A" if board[1][1] == "X" else "B"

        return "Draw" if len(moves) == 9 else "Pending"


# Test Cases
if __name__ == "__main__":
    sol = Solution()

    moves = [[0, 0], [1, 1], [0, 1], [0, 2], [1, 0], [2, 0]]
    print(sol.tictactoe(moves))  # Output: B

    moves = [[0, 0], [1, 1], [2, 2]]
    print(sol.tictactoe(moves))  # Output: "Pending"

    moves = [[0, 0], [1, 1], [2, 0], [1, 0], [1, 2], [2, 1], [0, 1], [0, 2], [2, 2]]
    print(sol.tictactoe(moves))  # Output: "Draw"

    moves = [[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]]
    print(sol.tictactoe(moves))  # Output: "A"
