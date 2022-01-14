import collections

# 어려움
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.Counter(t)
        missing = len(t)
        left = start = end = 0

        # 오른쪽 포인터 이동
        for right, char in enumerate(s, 1):
            missing -= need[char] > 0
            need[char] -= 1

            # 필요 문자가 0이면 왼쪽 포인터 이동 판단
            if missing == 0:
                # 왼쪽 포인터가 불필요한 문자를 가르키고 있으면 음수일 것이다
                # 0을 가르키는 위치까지 왼쪽 포인터를 이동시킨다
                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1

                # 더 작은 값을 찾을때까지 유지하다가 가장 작은 값인 경우, 리턴
                if not end or right - left <= end - start:
                    start, end = left, right
                    need[s[left]] += 1
                    missing += 1
                    left += 1
        return s[start:end]


s = Solution()
print(s.minWindow(s="ADOBECODEBANC", t="ABC"))
print(s.minWindow(s="aaaaaaaaaaaabbbbbcdd", t="abcdd"))
print(s.minWindow(s = "a", t = "a"))
