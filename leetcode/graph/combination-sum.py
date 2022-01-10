from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(elements, index):
            _sum = sum(elements)
            # 합이 target 보다 크면 재귀 종료
            if _sum > target:
                return
            # 합이 target 이면 결과에 추가후 재귀 종료
            if _sum == target:
                result.append(elements)
                return

            # 중복 조합 탐색
            for i in range(index, len(candidates)):
                dfs(elements + [candidates[i]], i)

        result = []
        dfs([], 0)
        return result