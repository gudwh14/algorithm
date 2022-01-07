from typing import List


# 투포인터를 사용해서 풀어야함
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        if len(nums) < 3:
            return result

        # 투 포인터가 index 의 +1 과 맨마지막 인데스를 가르키므로 len - 2 까지 반복
        for i in range(len(nums) - 2):
            # 기준값이 이전값이랑 같은 값이면 중복값이므로 스킵
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 투 포인터 선언
            left = i + 1
            right = len(nums) - 1
            while left < right:
                # 세수의 합
                sum = nums[i] + nums[left] + nums[right]
                # 세수의 합이 0이면 결과 저장 및 포인터 이동
                if sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    # 다음 포인터 값이 현재 포인터 값이랑 같을경우 포인터 이동, 중복 결과값 방지
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # 다음 포인터 값이 현재 포인터 값이랑 같을경우 포인터 이동, 중복 결과값 방지
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
        return result


s = Solution()
print(s.threeSum([-1, 0, 1, 2, -1, -4]))
