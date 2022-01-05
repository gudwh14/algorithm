import collections
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)

        # 딕셔너리 key 를 srorted(word)로 잡아 anagrams 일경우 딕셔너리에 value 리스트 추가
        for word in strs:
            anagrams[''.join(sorted(word))].append(word)

        return anagrams.values()


s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(s.groupAnagrams([""]))
print(s.groupAnagrams(["a"]))