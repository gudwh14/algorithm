from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(elements: List[int], index):
            if len(elements) == k:
                result.append(elements[:])
                return

            for idx, data in enumerate(nums):
                if idx > index:
                    dfs(elements + [data], idx)

        result = []
        nums = range(1, n + 1)
        dfs([], -1)

        return result


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []

        def dfs(elements, start: int, k: int):
            if k == 0:
                results.append(elements[:])

            # 자신 이전의 모든 값을 고정하여 재귀 호출
            for i in range(start, n + 1):
                elements.append(i)
                dfs(elements, i + 1, k - 1)
                elements.pop()

        dfs([], 1, k)
        return results


s = Solution()
print(s.combine(4,2))
