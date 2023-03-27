# def start_with(trie, start):
#     cur_node = trie
#     for char in start:
#         if char in cur_node:
#             cur_node = cur_node[char]
#         else:
#             return False
#
#     return True
#
#
# def solution(N, M, S, checks):
#     answer = 0
#     trie = {}
#
#     # 트라이 만들기
#     for string in S:
#         cur_node = trie
#         for char in string:
#             if char not in cur_node:
#                 cur_node[char] = {}
#             cur_node = cur_node[char]
#         cur_node["*"] = string
#
#     # 트라이 찾기
#     for check in checks:
#         cur_node = trie
#         flag = False
#         for char in check:
#             if char in cur_node:
#                 cur_node = cur_node[char]
#             else:
#                 flag = True
#                 break
#         if flag:
#             continue
#         if "*" in cur_node:
#             answer += 1
#
#     return answer

def solution(S, checks):
    trie = {}
    answer = 0

    for string in S:
        cur_node = trie
        for char in string:
            if char not in cur_node:
                cur_node[char] = {}
            cur_node = cur_node[char]
        cur_node['*'] = string

    for check in checks:
        cur_node = trie
        for char in check:
            if char in cur_node:
                cur_node = cur_node[char]
            else:
                break
        else:
            if '*' in cur_node:
                answer += 1

    def travel(level, cur):
        if '*' in cur:
            print(cur['*'])
            return

        cur_children = sorted(cur)

        for child in cur_children:
            print(level, child)
            travel(level + 1, cur[child])

    travel(0, trie)
    return answer


N, M = map(int, input().split())
S = [input() for _ in range(N)]
checks = [input() for _ in range(M)]
# print(solution(N, M, S, checks))
print(solution(S, checks))
