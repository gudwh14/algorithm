from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 인덱스를 저장해놓는 스택
        index_list = []
        # 결과를 0 으로 모두 초기화 설정
        result = [0] * len(temperatures)

        for i, cur in enumerate(temperatures):
            # 스택에 인덱스가 존재하고 현재온도가, 스택에 존재하는 마지막 온도보다 높으면 -> 스택 pop() , 현재 인덱스에서 빼준 값을 저장
            while index_list and cur > temperatures[index_list[-1]]:
                last = index_list.pop()
                result[last] = i - last
            index_list.append(i)

        return result


s = Solution()
print(s.dailyTemperatures(temperatures=[73, 74, 75, 71, 69, 72, 76, 73]))
print(s.dailyTemperatures(temperatures=[30, 40, 50, 60]))
print(s.dailyTemperatures(temperatures=[30, 60, 90]))
