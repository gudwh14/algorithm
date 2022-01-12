from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 인덱스는 0부터 시작
        index = 0
        # 2일 경우 맨뒤로 정렬, 0 일경우 맨앞으로 정렬, 1 일경우 액션 X
        for _ in range(0, len(nums)):
            if nums[index] == 2:
                nums.append(nums[index])
                nums.pop(index)
            elif nums[index] == 0:
                nums.pop(index)
                nums.insert(0, 0)
                index += 1
            elif nums[index] == 1:
                index += 1

        print(nums)

s = Solution()
print(s.sortColors(nums=[2, 0, 2, 1, 1, 0]))
print(s.sortColors(nums=[2, 0, 1]))
