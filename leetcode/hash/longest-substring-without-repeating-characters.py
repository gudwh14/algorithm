
# 투포인터 index , start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 사용된 문자 저장하는 해쉬
        used = {}
        # 초기 변수값 설정
        # 결과는 0
        # 시작점 포인터는 0
        result = start = 0

        for index, char in enumerate(s):
            # 이미 사용된 문자고 시작 포인터가 사용된 문자 인덱스 보다 작거나 같으면 시작 포인터 이동
            if char in used and start <= used[char]:
                start = used[char] + 1
            # 새로운 문자거나 , 시작 포인터가 변경되지 않으면 문자열 길이 구하기
            else:
                result = max(result, (index + 1) - start)

            # 사용된 문자 저장
            used[char] = index

        return result


s = Solution()
print(s.lengthOfLongestSubstring("pwwkew"))
print(s.lengthOfLongestSubstring("abcabcbb"))
print(s.lengthOfLongestSubstring("au"))
print(s.lengthOfLongestSubstring("dvdf"))