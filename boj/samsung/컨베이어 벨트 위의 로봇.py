# 컨베이어 벨트 회전
def turn_right(N, A, robot):
    temp = None
    next_temp = None

    for i in range((N * 2) - 1):
        if temp == None:
            next_temp = A[i + 1]
            A[i + 1] = A[i]
            temp = next_temp
        else:
            next_temp = A[i + 1]
            A[i + 1] = temp
            temp = next_temp

    A[0] = temp

    delete = False
    for idx in range(len(robot)):
        if robot[idx] == N * 2 - 1:
            robot[idx] = 0
        else:
            robot[idx] += 1
            if robot[idx] == N - 1:
                delete = True

    if delete:
        robot.remove(N - 1)


# 로봇 움직이는 함수
def move_robot(N, A, robot):
    count = 0
    delete = False
    for idx in range(len(robot)):
        locate = robot[idx]

        if locate != N * 2 - 1 and A[locate + 1] > 0 and (locate + 1) not in robot:
            robot[idx] += 1
            A[locate + 1] -= 1
            if A[locate + 1] == 0:
                count += 1
            if locate + 1 == N - 1:
                delete = True
        elif locate == N * 2 - 1 and A[0] > 0 and 0 not in robot:
            robot[idx] = 0
            A[0] -= 1
            if A[0] == 0:
                count += 1

    if delete:
        robot.remove(N - 1)
    return count


def solution(N, K, A):
    count = 0
    answer = 0
    robot = []

    while True:
        answer += 1
        turn_right(N, A, robot)
        count += move_robot(N, A, robot)
        if A[0] > 0:
            robot.append(0)
            A[0] -= 1
            if A[0] == 0:
                count += 1
        if count >= K:
            break
    return answer


N, K = map(int, input().split())
A = list(map(int, input().split()))
print(solution(N, K, A))
