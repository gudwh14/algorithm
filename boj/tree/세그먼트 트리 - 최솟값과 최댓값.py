# 최솟값, 최대값을 효율적으로 찾기위해서는 세그먼트 트리를 최대값, 최소값을 가지는 트리로 각각 만들어야 한다.
def solution(N, M, nums, infos):
    min_tree = [0 for _ in range(N * 4)]
    max_tree = [0 for _ in range(N * 4)]

    def min_init(start, end, node):
        if start == end:
            min_tree[node] = nums[start]
            return min_tree[node]

        mid = (start + end) // 2
        min_tree[node] = min(min_init(start, mid, node * 2), min_init(mid + 1, end, node * 2 + 1))
        return min_tree[node]

    def max_init(start, end, node):
        if start == end:
            max_tree[node] = nums[start]
            return max_tree[node]

        mid = (start + end) // 2
        max_tree[node] = max(max_init(start, mid, node * 2), max_init(mid + 1, end, node * 2 + 1))
        return max_tree[node]

    min_init(0, N - 1, 1)
    max_init(0, N - 1, 1)

    def min_find(start, end, node, left, right):
        if left > end or right < start:
            return float('+inf')

        if left <= start and end <= right:
            return min_tree[node]

        mid = (start + end) // 2
        return min(min_find(start, mid, node * 2, left, right), min_find(mid + 1, end, node * 2 + 1, left, right))

    def max_find(start, end, node, left, right):
        if left > end or right < start:
            return -1

        if left <= start and end <= right:
            return max_tree[node]

        mid = (start + end) // 2
        return max(max_find(start, mid, node * 2, left, right), max_find(mid + 1, end, node * 2 + 1, left, right))

    for a, b in infos:
        print(min_find(0, N - 1, 1, a - 1, b - 1), max_find(0, N - 1, 1, a - 1, b - 1))


N, M = map(int, input().split())
nums = [int(input()) for _ in range(N)]
infos = [list(map(int, input().split())) for _ in range(M)]
solution(N, M, nums, infos)
