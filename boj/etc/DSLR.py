import collections
import sys


def solution(A, B):
    Q = collections.deque()
    visit = [False for _ in range(10000)]
    Q.append((A, ''))
    visit[int(A)] = True

    while Q:
        num, commands = Q.popleft()
        if num == B:
            print(commands)
            break

        for cmd in ['D', 'S', 'L', 'R']:
            if cmd == 'D':
                next_num = (num * 2) % 10000
            elif cmd == 'S':
                if num == 0:
                    next_num = 9999
                else:
                    next_num = num - 1
            # 숫자를 한칸씩 밀때 연산을 통해서 밀 수 있음
            elif cmd == 'L':
                next_num = 10 * (num % 1000) + num // 1000
            elif cmd == 'R':
                next_num = 1000 * (num % 10) + num // 10

            if not visit[next_num]:
                Q.append((next_num, commands + cmd))
                visit[next_num] = True


T = int(input())
for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    solution(A, B)
