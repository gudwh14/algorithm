import collections
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 카운터 모듈을 사용하여 카운팅 객체 저장
        counts = collections.Counter(nums)
        result = []

        # counts.most_common(k)
        # 내림차순으로 정렬
        sorted_list = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        index = 0
        # k 개 만큼 반복하여 result 에 저장!
        for key, value in sorted_list:
            if index == k:
                break
            else:
                result.append(key)
                index += 1

        return result


s = Solution()
# print(s.topKFrequent(nums = [1,1,1,2,2,3], k = 2))
print(s.topKFrequent(nums = [3,0,1,0], k = 1))