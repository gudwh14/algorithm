from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(index, path):
            # digits 의 길이 만큼 path가 만들어지면 백트래킹
            if len(path) == len(digits):
                result.append(path)
                return

            # 입력값 자릿수 단위 반복
            for i in range(index, len(digits)):
                # 숫자에 해당하는 모든 문자열 반복
                for j in phone[digits[i]]:
                    dfs(i + 1, path + j)

        # 예외 처리
        if not digits:
            return []

        phone = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        result = []
        dfs(0, '')
        return result


s = Solution()
print(s.letterCombinations(digits="234"))
# print(s.letterCombinations(digits = "2"))
