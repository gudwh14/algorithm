import collections


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # 문자열의 각 문재의 개수를 Counter 를 통해 저장
        # stack, seen (set : unordered)
        counter, stack, seen = collections.Counter(s), [], set()

        for char in s:
            # 카운터 -1
            counter[char] -= 1
            # 이미 처리된 문자일 경우 스킵
            if char in seen:
                continue
            # 사전식 순서로 뒤에 붙일수 있는 문자열이면, char 보다 앞에 존재하는 문자 삭제 (stack, seen 에서 제거)
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            # stack, seen 에 저장
            stack.append(char)
            seen.add(char)

        return ''.join(stack)


s = Solution()
print(s.removeDuplicateLetters("bcabc"))
# print(s.removeDuplicateLetters("cbacdcbc"))