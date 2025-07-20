class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def dfs(r, c, region):
            # If it's outside, then the region is not surrounded
            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return False
            if board[r][c] == 'X' or (r, c) in visited:
                return True

            visited.add((r, c))
            region.append((r, c))

            up = dfs(r - 1, c, region)
            down = dfs(r + 1, c, region)
            left = dfs(r, c - 1, region)
            right = dfs(r, c + 1, region)

            return up and down and left and right

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O' and (r, c) not in visited:
                    region = []
                    surrounded = dfs(r, c, region)
                    if surrounded:
                        for x, y in region:
                            board[x][y] = 'X'