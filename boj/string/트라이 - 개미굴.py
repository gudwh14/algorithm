def solution(N, infos):
    trie = {}

    # 트라이 만들기
    for info in infos:
        cur_node = trie
        for food in info:
            if food not in cur_node:
                cur_node[food] = {}
            cur_node = cur_node[food]
        cur_node['*'] = '종료'

    # 트라이 순환해서 읽기
    def travel(level, cur):
        # 끝나면 종료
        if '*' in cur:
            return

        # 자식들 구하기
        cur_children = sorted(cur)

        # 자식들 출력
        for child in cur_children:
            print("--" * level + child)
            # 재귀로 해당 자식들의 자식들 탐색
            travel(level + 1, cur[child])

    travel(0, trie)


N = int(input())
infos = [list(input().split())[1:] for _ in range(N)]
solution(N, infos)
