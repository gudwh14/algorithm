from typing import List


# 내가 푼 코드 On2 로직 브루트 포스
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0, 1]

        for i in range(len(nums)):
            for y in range(i + 1, len(nums)):
                if nums[i] + nums[y] == target:
                    return [i, y]


# 책 풀이 코드
# 딕셔너리를 활용하여 첫 번째 수를 뺀 결과 키 조회 로직
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0, 1]

        # 딕셔너리 key 를 nums 의 배열값으로, value 를 nums 의 index 로 저장
        nums_map = {}
        for index, value in enumerate(nums):
            nums_map[value] = index

        for index, value in enumerate(nums):
            if target - value in nums_map and index != nums_map[target - value]:
                return [index, nums_map[target - value]]



s = Solution()
print(s.twoSum(nums=[2, 7, 11, 15], target=9))
print(s.twoSum(nums=[3, 2, 4], target=6))
print(s.twoSum(nums=[3, 3], target=6))
print(s.twoSum(nums=[3, 2, 3], target=6))
