import collections
import re
from typing import List

# 내가 푼 코드 ( RunTime : 51ms )
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        most_hashmap = {}

        # 정규표현식을 이용하여 , . ! ? ' ; 를 제거
        paragraph = re.sub("[\.\,\'\!\?\;]", " ", paragraph)

        # 소문자만 사용하여 문자열로 반환하여 딕셔너리에 카운트하여 저장
        for string in paragraph.lower().split():
            if most_hashmap.get(string):
                most_hashmap[string] = most_hashmap.get(string) + 1
            else:
                most_hashmap[string] = 1

        # 오름차순으로 정렬
        most_hashmap = sorted(most_hashmap.items(), key=lambda x: x[1])

        # banned 리스트에 있을경우 pop 연산후 다음 비교 진행, 없을경우 리턴
        while len(most_hashmap) > 1:
            most_str = most_hashmap[len(most_hashmap)-1][0]
            if most_str in banned:
                most_hashmap.pop()
            else:
                return most_str

        # 딕셔너리 길이가 1 일 경우 반환
        return most_hashmap[0][0]

# 책 코드 ( RunTime : 64ms )
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        # 리스트 컴프리헨션을 이용하여 paragraph 구별
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
                 .lower().split()
                 if word not in banned]

        # collections.Counter 모듈을 사용하여 개수를 저장
        counts = collections.Counter(words)
        # 가장 흔하게 등장하는 단어 반환
        return counts.most_common(1)[0][0]


s = Solution()
print(s.mostCommonWord( "Bob hit a ball, the hit BALL flew far after it was hit.",["hit"]))
print(s.mostCommonWord("a.",[]))
print(s.mostCommonWord("a, a, a, a, b,b,b,c, c",["a"]))
