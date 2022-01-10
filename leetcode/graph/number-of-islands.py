from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # 탐색한 인덱스를 '0'으로 변경후, 인접 인덱스를 방문한다
        def dfs(i, j):
            # 인덱스 범위 넘어가는 예외처리, 중복 탐색 방지
            if i < 0 or i >= len(grid) or \
                    j < 0 or j >= len(grid[0]) or \
                    grid[i][j] != '1':
                return

            grid[i][j] = '0'
            dfs(i + 1, j)
            dfs(i, j + 1)
            dfs(i - 1, j)
            dfs(i, j - 1)

        result = 0
        # grid 2차원 배열을 반복하여 해당 인덱스의 값이 '1'일 경우 dfs 탐색 시작, result + 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    result += 1

        return result


s = Solution()
print(s.numIslands(grid=[
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]))
print(s.numIslands(grid=[
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]))
