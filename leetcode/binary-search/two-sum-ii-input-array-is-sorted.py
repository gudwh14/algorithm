import bisect
from typing import List


# 이진 탐색은 정렬되어있을때 탐색 가능
# 두개의 합을 찾을때에는 target - value 값으로 찾기
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, num in enumerate(numbers):
            find = target - num
            # 이진 탐색
            index = bisect.bisect_left(numbers, find, i + 1)
            if index < len(numbers) and numbers[index] == find:
                return [i + 1, index + 1]


s = Solution()
print(s.twoSum([2, 7, 11, 15], target=9))
