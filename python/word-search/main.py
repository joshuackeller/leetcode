from typing import List
from collections import Counter


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        neighbors = [[-1, 0], [0, -1], [1, 0], [0, 1]]

        def dfs(r, c, word_index) -> bool:
            if word_index == len(word) - 1:
                return True

            board[r][c] = "#"

            for r_move, c_move in neighbors:
                new_r, new_c = r + r_move, c + c_move
                if (
                    min(new_r, new_c) >= 0
                    and new_r < ROWS
                    and new_c < COLS
                    and board[new_r][new_c] != "#"
                    and board[new_r][new_c] == word[word_index + 1]
                    and dfs(new_r, new_c, word_index + 1)
                ):
                    return True

            board[r][c] = word[word_index]

            return False

        counter = Counter(word)
        for row in board:
            counter.update(row)

        if counter[word[0]] > counter[word[-1]]:
            word = word[::-1]

        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True

        return False

