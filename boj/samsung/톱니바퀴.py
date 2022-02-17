import collections


# 기어를 반시계 방향으로 회전하는 함수
def turn_left(gear):
    temp = None
    for i in range(7, -1, -1):
        idx = i - 1
        if idx < 0:
            idx = 7

        if temp == None:
            temp = gear[idx]
            next_temp = temp
            gear[idx] = gear[i]
        else:
            next_temp = gear[idx]
            gear[idx] = temp
            temp = next_temp


# 기어를 시계방향으로 회전하는 함수
def turn_right(gear):
    temp = None
    for i in range(8):
        idx = i + 1
        if idx > 7:
            idx = 0

        if temp == None:
            temp = gear[idx]
            next_temp = temp
            gear[idx] = gear[i]
        else:
            next_temp = gear[idx]
            gear[idx] = temp
            temp = next_temp


# 어떤 방향으로 어떤 기어가 회전하는지 구하는 함수
def calc_turn_gear(start, gears, turn):
    # 해쉬 선언
    turns = collections.defaultdict(list)
    # 시작 기어는, 시작 방향으로 회전
    turns[turn].append(start)

    # 시작 기어가 1 일경우 오른쪽기어들을 쭉 체크하면된다
    if start == 1:
        for i in range(1, 4):
            if gears[i][2] != gears[i + 1][6]:
                # 기어가 한번 돌때마다 기존과 반대방향으로 회전
                turn = -turn
                turns[turn].append(i + 1)
            else:
                break

    # 시작 기어가 2일경우 왼쪽에 있는 1번 기어 체크후, 오른쪽 기어들 체크
    if start == 2:
        if gears[2][6] != gears[1][2]:
            turns[-turn].append(1)
        for i in range(2, 4):
            if gears[i][2] != gears[i + 1][6]:
                # 기어가 한번 돌때마다 기존과 반대방향으로 회전
                turn = -turn
                turns[turn].append(i + 1)
            else:
                break

    # 시작기어가 3번일경우, 오른쪽에있는 4번기어를 체크후, 왼쪽기어들 체크
    if start == 3:
        if gears[3][2] != gears[4][6]:
            turns[-turn].append(4)
        for i in range(3, 1, -1):
            if gears[i][6] != gears[i - 1][2]:
                # 기어가 한번 돌때마다 기존과 반대방향으로 회전
                turn = -turn
                turns[turn].append(i - 1)
            else:
                break

    # 시작 기어가 4일 경우 왼쪽기어들을 쭉 체크하면된다
    if start == 4:
        for i in range(4, 1, -1):
            if gears[i][6] != gears[i - 1][2]:
                # 기어가 한번 돌때마다 기존과 반대방향으로 회전
                turn = -turn
                turns[turn].append(i - 1)
            else:
                break
    return turns


def solution(gears, k, command):
    answer = 0
    gears.insert(0, [])

    for gear, turn in command:
        # 회전할수있는 기어들 구하기
        turns = calc_turn_gear(gear, gears, turn)
        # 기어 회전
        for direction, targets in turns.items():
            for target in targets:
                if direction == -1:
                    turn_left(gears[target])
                elif direction == 1:
                    turn_right(gears[target])

    # 12시 방향에있는 S극 계산
    for i in range(1, 5):
        if gears[i][0] == 1:
            if i == 1:
                answer += 1
            elif i == 2:
                answer += 2
            elif i == 3:
                answer += 4
            elif i == 4:
                answer += 8

    return answer


gears = [list(map(int, list(str(input().split()[0])))) for _ in range(4)]
k = int(input().split()[0])
command = [list(map(int, input().split())) for _ in range(k)]

print(solution(gears, k, command))
