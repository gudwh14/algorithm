def solution(N, M, K, nums, infos):
    tree = [0 for _ in range(N * 4)]

    # 세그먼트 트리 만들기
    # 재귀 반복문으로 트리의 리프 노드부터 채우기 시작
    def init(start, end, node):
        if start == end:
            tree[node] = nums[start]
            return tree[node]

        mid = (start + end) // 2
        # 노드 = 왼쪽 서브 노드 + 오른쪽 서브 노드
        tree[node] = init(start, mid, node * 2) + init(mid + 1, end, node * 2 + 1)
        return tree[node]

    init(0, N - 1, 1)

    # 부분합 구하기
    def sum(start, end, node, left, right):
        # 구하고 싶은 범위가 넘어가면 0
        if left > end or right < start:
            return 0
        # 범위에 속하면 해당 노드 더해주기
        #  left <= start,end <= right 사이에 있으면
        if left <= start and end <= right:
            return tree[node]

        # 그렇지 않으면 구간 나누어 탐색
        mid = (start + end) // 2
        return sum(start, mid, node * 2, left, right) + sum(mid + 1, end, node * 2 + 1, left, right)

    # 인덱스 업데이트
    # 업데이트는 diff를 이용하여 진행
    def update(start, end, node, index, diff):
        # 인덱스가 해당 구간에 속하지 않으면 종료
        if index < start or index > end:
            return

        # 해당 구간에 속하면 업데이트
        tree[node] += diff
        # 나눌 구간이 없으면 종료
        if start == end:
            return
        # 구간 나눠서 탐색
        mid = (start + end) // 2
        update(start, mid, node * 2, index, diff)
        update(mid + 1, end, node * 2 + 1, index, diff)

    for a, b, c in infos:
        if a == 1:
            diff = c - nums[b - 1]
            nums[b - 1] = c
            update(0, N - 1, 1, b - 1, diff)
        elif a == 2:
            print(sum(0, N - 1, 1, b - 1, c - 1))


N, M, K = map(int, input().split())
nums = [int(input()) for _ in range(N)]
infos = [list(map(int, input().split())) for _ in range(M + K)]
solution(N, M, K, nums, infos)
