class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, i, visit):
            if i == len(word):
                return True  # found the word

            if (
                r < 0 or c < 0 or r >= ROWS or c >= COLS or
                board[r][c] != word[i] or (r, c) in visit
            ):
                return False

            visit.add((r, c))
            found = (
                dfs(r - 1, c, i + 1, visit) or
                dfs(r + 1, c, i + 1, visit) or
                dfs(r, c - 1, i + 1, visit) or
                dfs(r, c + 1, i + 1, visit)
            )
            visit.remove((r, c))  # backtrack
            return found

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0, set()):
                        return True

        return False
