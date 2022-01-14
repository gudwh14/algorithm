from typing import List


# 분할정복
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # 왼쪽 표현식, 오른쪽 표현식을 op 로 계산해주는 함수
        def compute(left, right, op):
            result = []
            for l in left:
                for r in right:
                    result.append(eval(str(l) + op + str(r)))
            return result

        # 표현식이 숫자만 존재할 경우
        # 재귀의 최종결과로 리턴하게 됨
        if expression.isdigit():
            return [int(expression)]

        result = []
        # 연산자를 만날때마다 연산자를 기준으로 왼쪽 표현식, 오른쪽표현식으로 분할하여 계산
        for index, value in enumerate(expression):
            if value in '+-*':
                left = self.diffWaysToCompute(expression[:index])
                right = self.diffWaysToCompute(expression[index + 1:])
                result.extend(compute(left, right, value))

        return result


s = Solution()
print(s.diffWaysToCompute(expression="2*3-4*5"))
