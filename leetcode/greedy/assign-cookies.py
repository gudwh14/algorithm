from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        result = 0
        g.sort()
        s.sort()

        g_pointer = s_pointer = 0
        while g_pointer < len(g) and s_pointer < len(s):
            if g[g_pointer] <= s[s_pointer]:
                result += 1
                g_pointer += 1
                s_pointer += 1
            else:
                s_pointer += 1

        return result


s = Solution()
print(s.findContentChildren(g = [1,2,3], s = [1,1]))
print(s.findContentChildren(g = [1,2], s = [1,2,3]))