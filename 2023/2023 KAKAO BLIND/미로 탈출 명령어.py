def solution(n, m, x, y, r, c, k):
    answer = ''
    distance = abs(r - x) + abs(c - y)
    # k -= distance : 실제로 이동 할 수 있는 거리를 뺀 dlru 커맨드를 채울 수 있는 거리
    k -= distance
    if k < 0 or k % 2 != 0:
        return 'impossible'

    counts = {'d': 0, 'l': 0, 'r': 0, 'u': 0}

    if x > r:
        counts['u'] += (x - r)
    else:
        counts['d'] += (r - x)

    if y > c:
        counts['l'] += (y - c)
    else:
        counts['r'] += (c - y)

    # d, l, r, u 순으로 커맨드 채우기

    # d
    answer += counts['d'] * 'd'
    # (more_command_d, y)에서 다시 up커맨드를 할 수 있는 거리 구하기
    more_command_d = min(int(k / 2), n - (x + counts['d']))  # min(쓸수 있는 커맨드, 격자크기에서 down할 수 있는 최대 거리)
    answer += more_command_d * 'd'
    counts['u'] += more_command_d
    k -= (more_command_d * 2)

    # l
    answer += counts['l'] * 'l'
    # (more_command_d, more_command_l)에서 다시 right커맨드 할 수 있는 거리 구하기
    more_command_l = min(int(k / 2), y - counts['l'] - 1)
    answer += more_command_l * 'l'
    counts['r'] += more_command_l
    k -= (more_command_l * 2)

    # rl
    answer += 'rl' * int(k / 2)

    # r
    answer += 'r' * counts['r']

    # u
    answer += 'u' * counts['u']
    return answer