def start_with(trie, start):
    cur_node = trie
    for char in start:
        if char in cur_node:
            cur_node = cur_node[char]
        else:
            return False

    return True


def solution(N, M, S, checks):
    answer = 0
    trie = {}

    # 트라이 만들기
    for string in S:
        cur_node = trie
        for char in string:
            if char not in cur_node:
                cur_node[char] = {}
            cur_node = cur_node[char]
        cur_node["*"] = string

    # 트라이 찾기
    for check in checks:
        cur_node = trie
        flag = False
        for char in check:
            if char in cur_node:
                cur_node = cur_node[char]
            else:
                flag = True
                break
        if flag:
            continue
        if "*" in cur_node:
            answer += 1

    return answer


N, M = map(int, input().split())
S = [input() for _ in range(N)]
checks = [input() for _ in range(M)]
print(solution(N, M, S, checks))
