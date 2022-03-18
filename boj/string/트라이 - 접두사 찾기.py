def solution(N, M, S, words):
    answer = 0
    trie = {}

    # 트라이 만들기
    for s in S:
        cur_node = trie
        for char in s:
            if char not in cur_node:
                cur_node[char] = {}
            cur_node = cur_node[char]
        cur_node['*'] = s

    # word가 S의 접두사가 되는것이 있는지 판단하기
    for word in words:
        cur_node = trie
        flag = True
        for char in word:
            if char in cur_node:
                cur_node = cur_node[char]
            else:
                flag = False
                break
        if flag:
            answer += 1

    # 트라이 탐색하여 단어 찾기!
    def travel(level, cur):
        if '*' in cur:
            print(cur['*'])
            return

        cur_children = cur

        for child in cur_children:
            travel(level + 1, cur[child])

    # travel(0, trie)
    return answer


N, M = map(int, input().split())
S = [input() for _ in range(N)]
words = [input() for _ in range(M)]
print(solution(N, M, S, words))
