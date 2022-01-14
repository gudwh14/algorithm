import collections


# TLE 시간초과 ( 슬라이싱을 사용하면 시간초과)
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window_size = len(s)

        if len(s) == k:
            return k

        while window_size > k:
            left = 0
            right = window_size
            while right <= len(s):
                _slice = s[left:right]
                counts = collections.Counter(_slice)
                if len(_slice) - counts.most_common(1)[0][1] <= k:
                    return len(_slice)
                left += 1
                right += 1
            window_size -= 1


# 투포인터, 슬라이딩 윈도우, Counter 이용
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = right = 0
        counts = collections.Counter()

        # 오른쪽 포인터를 한칸씩 이동
        for right in range(1, len(s) + 1):
            counts[s[right - 1]] += 1
            # 가장흔한 문자 탐색
            max_char_n = counts.most_common(1)[0][1]

            # right - left : 문자열의 길이 , 문자열 길이 - max_char_n 이 k 보다 크면 k 번 연산으로 바꿀수 없다는 뜻
            # 왼쪽 포인터를 한칸 이동시켜준다, 이때 왼쪽 포인터가 가르키는 카운터 개수를 1 감소
            if right - left - max_char_n > k:
                counts[s[left]] -= 1
                left += 1

        print(right, left)
        return right - left


s = Solution()
print(s.characterReplacement(s="AABABBA", k=1))

