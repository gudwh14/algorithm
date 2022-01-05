from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_list: List[str] = []
        digit_list: List[str] = []

        # 각 원소의 두번째 문자열 부터 letter, digit 으로 구분하여 새로운 리스트에 삽입
        for log in logs:
            if log.split(' ')[1].isdigit():
                digit_list.append(log)
            else:
                letter_list.append(log)

        # 람다 표현식을 이용한 정렬 진행 선순위 정렬로 각 원소의 두번쨰 문자열을 key(기준)으로 사전식정렬, 후순위로 첫번째 문자열을 key로 정렬
        letter_list.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letter_list + digit_list


s = Solution()
s.reorderLogFiles(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"])