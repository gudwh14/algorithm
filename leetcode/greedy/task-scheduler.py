import collections
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)

        counts = collections.Counter(tasks)
        # 한 스케쥴의 길이는 n + 1 개, 총 스케쥴의 개수는 가장 많은 task 의 수
        # 마지막 줄을 제외한 스케쥴의 총 길이는 (가장 많은 task 의 수 - 1) * 한 스케쥴의 길이(n + 1)
        result = (counts.most_common(1)[0][1] - 1) * (n + 1)

        # 마지막 줄 스케쥴 길이 계산
        for key, value in counts.items():
            if counts[key] >= counts.most_common(1)[0][1] - 1:
                result += counts[key] - (counts.most_common(1)[0][1] - 1)

        # 총task의 수보다 적게 나올경우, tasks 개수를 반환
        return max(result, len(tasks))


s = Solution()
print(s.leastInterval(tasks=["A", "A", "A", "B", "B", "B"], n=2))
print(s.leastInterval(tasks=["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], n=2))
