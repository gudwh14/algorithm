
# 투포인터를 이용해 확장해서 푸는것이 핵심!
class Solution:
    def longestPalindrome(self, s: str) -> str:

        def expand(left: int, right: int) -> str:
            # left , right 가 유효한 인덱스이고 문자열이 팰린드롬이면 반복문 실행
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # while 반복문이 끝나면 반환하고싶은 문자열에서 left - 1 , right + 1 되어있으므로
            # slice 로 반환시 원하는 문자열을 반환하기위해 s[left +1:right] 처리
            return s[left + 1:right]

        # 입력값의 길이가 1 이거나 팰린드롬의 길이가 입력값의 길이랑 같을경우 바로 리턴
        if len(s) == 1 or s == s[::-1]:
            return s

        result = ''
        for i in range(len(s) - 1):
            # 팰린드롬 문자열 길이가 홀수, 짝수 일수 있으니 투포인터를 두가지로 확장!
            result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)

        return result



s = Solution()
print(s.longestPalindrome("babad"))
print(s.longestPalindrome("cbbd"))