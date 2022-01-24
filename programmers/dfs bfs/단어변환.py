import collections


def solution(begin, target, words):
    if target not in words:
        return 0

    visit = []
    answer = float('+inf')

    def dfs(word, count):
        if word == target:
            nonlocal answer
            answer = min(answer, count)
            return
        visit.append(word)
        i_count = collections.Counter(word)
        for adjacent in words:
            j_count = collections.Counter(adjacent)
            compare = j_count - i_count
            if adjacent not in visit and len(compare) == 1:
                dfs(adjacent, count + 1)

    dfs(begin, 0)
    if answer == float('+inf'):
        answer = 0

    return answer


print(solution('hit', 'cog', ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution('hit', 'cog', ['cog', 'log', 'lot', 'dog', 'dot', 'hot']))
