def solution(T, P):
    answer = []
    count = 0
    n = len(P)
    idx = 0
    while idx <= len(T) - n:
        if T[idx] == P[0]:
            # 탐색시작
            find = True
            new_start = []
            for i in range(1, n):
                if T[idx + i] == P[0]:
                    new_start.append(idx + i)
                if T[idx + i] != P[i]:
                    find = False
                    break
            if find:
                answer.append(idx)
                count += 1
            if new_start:
                idx = new_start[0]
            else:
                idx += i
        else:
            idx += 1

    print(count)
    for idx in answer:
        print(idx + 1, end=' ')


T = input()
P = input()
solution(T, P)
