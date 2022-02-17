import collections
import copy


# 풀이
# 현재 계산한 연잔자 개수를 카운팅한 해쉬값을 만들어, 사용할 수 있는 연산자 개수와 비교하여 DFS 탐색 진행
def solution(n, a, op):
    answer = []
    op_hash = collections.defaultdict(int)

    def dfs(prev, depth, op_count):
        # 연산자가 n - 1개 만큼 쓰이면 종료!
        if depth == n - 1:
            answer.append(prev)
            return

        # + 연산자를 더 사용할수있으면 +연산 진행
        if op_count[0] < op[0]:
            _op_count = copy.deepcopy(op_count)
            _op_count[0] += 1
            dfs(prev + a[depth + 1], depth + 1, _op_count)

        # + 연산자를 더 사용할수있으면 +연산 진행
        if op_count[1] < op[1]:
            _op_count = copy.deepcopy(op_count)
            _op_count[1] += 1
            dfs(prev - a[depth + 1], depth + 1, _op_count)

        # + 연산자를 더 사용할수있으면 +연산 진행
        if op_count[2] < op[2]:
            _op_count = copy.deepcopy(op_count)
            _op_count[2] += 1
            dfs(prev * a[depth + 1], depth + 1, _op_count)

        # + 연산자를 더 사용할수있으면 +연산 진행
        if op_count[3] < op[3]:
            _op_count = copy.deepcopy(op_count)
            _op_count[3] += 1
            # 음수 나눗셈
            if prev < 0:
                prev = -prev
                div = prev // a[depth + 1]
                div = -div
                dfs(div, depth + 1, _op_count)
            else:
                dfs(prev // a[depth + 1], depth + 1, _op_count)

    dfs(a[0], 0, op_hash)
    # 오름차순으로 정렬
    answer.sort()
    # 최대값 출력
    print(answer[-1])
    # 최솟값 출력
    print(answer[0])


n = int(input().split()[0])
a = list(map(int, input().split()))
op = list(map(int, input().split()))

solution(n, a, op)