from typing import List


class compare(str):
    def __lt__(x, y):
        return x + y > y + x


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # nums 리스트를 문자열로 변환
        str_nums = []
        for num in nums:
            str_nums.append(str(num))

        # 정렬 key 는 compare class 를 이용
        result = sorted(str_nums, key=compare)
        # 결과 리스트를 합친후 int 형으로 형변환 '00' 과 같은 문자열을 제거, 다시 str 로 형변환
        return str(int(''.join(result)))


s = Solution()
print(s.largestNumber(nums=[10, 2]))
print(s.largestNumber(nums=[9, 30, 34, 5, 3]))
print(s.largestNumber(nums=[0, 0]))
