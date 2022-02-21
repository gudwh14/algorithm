# 풀이로직 나무들을 나무좌표 배열에 나이를 저장해서 풀이해야함!
def print_board(board):
    for bo in board:
        print(bo)
    print()


# 봄 함수
def spring(N, trees, foods):
    die = []

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            # 해당 좌표에 해당하는 나무들을 찾아서, 오름차순으로 age 정렬
            # 오름차순으로 정렬시, 어떤 idx에서 양분이 부족할경우 그 뒤에 있는 나무들은 무조건 부족하다!
            trees[i][j].sort()
            # age들을 비교
            for idx in range(len(trees[i][j])):
                age = trees[i][j][idx]
                # 양분이 충분하면
                if foods[i][j] >= age:
                    foods[i][j] -= age
                    trees[i][j][idx] += 1
                # 양분이 충분하지 않으면
                else:
                    # 죽은나무는 해당 인덱스부터 끝까지에 해당하는 age
                    die.append([i, j, trees[i][j][idx:]])
                    # 남아 있는 나무는 처음부터 해당 인덱스 -1 까지 age
                    trees[i][j] = trees[i][j][:idx]
                    break
    return die


# 여름 함수
def summer(die, foods):
    for trees in die:
        i, j, ages = trees
        for age in ages:
            foods[i][j] += age // 2


# 가을 함수
def autumn(N, trees):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            for age in trees[i][j]:
                if age % 5 == 0:
                    for direct in directions:
                        ni = i + direct[0]
                        nj = j + direct[1]

                        if 1 <= ni < N + 1 and 1 <= nj < N + 1:
                            trees[ni][nj].append(1)


# 겨울 함수
def winter(N, A, foods):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            foods[i][j] += A[i - 1][j - 1]


def solution(N, M, K, A, trees):
    answer = 0
    # 양분 배열 초기화
    foods = [[5] * (N + 1) for _ in range(N + 1)]

    for i in range(N + 1):
        for j in range(N + 1):
            if i == 0:
                foods[i][j] = 0
            if j == 0:
                foods[i][j] = 0

    # K 년 만큼 반복
    for i in range(K):
        die = spring(N, trees, foods)
        summer(die, foods)
        autumn(N, trees)
        winter(N, A, foods)

    # 남아 있는 나무 개수 카운팅
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            answer += len(trees[i][j])
    return answer


N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
# 나무 배열 초기화
trees = [[[] for _ in range(N + 1)] for _ in range(N + 1)]

# (r,c) 좌표에 해당하는 나무 배열에 age 리스트로 저장하기
for _ in range(M):
    i, j, age = map(int, input().split())
    trees[i][j].append(age)

print(solution(N, M, K, A, trees))
