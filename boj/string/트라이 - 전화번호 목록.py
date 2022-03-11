def solution(lists):
    trie = {}
    lists.sort()
    for string in lists:
        cur_node = trie
        for char in string:
            if char not in cur_node:
                cur_node[char] = {}
            else:
                if "*" in cur_node[char]:
                    return 'NO'
            cur_node = cur_node[char]
        cur_node['*'] = string

    return 'YES'


T = int(input())
for _ in range(T):
    n = int(input())
    lists = [input() for _ in range(n)]
    print(solution(lists))
