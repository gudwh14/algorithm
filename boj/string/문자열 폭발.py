def solution(string, bomb):
    n = len(bomb)
    Q = []

    for char in string:
        Q.append(char)

        is_bomb = True
        for i in range(n):
            if len(Q) <= i or Q[-(1 + i)] != bomb[-(1 + i)]:
                is_bomb = False
                break
        if is_bomb:
            for _ in range(n):
                Q.pop()

    if Q:
        return ''.join(Q)
    else:
        return 'FRULA'


string = input()
bomb = input()
print(solution(string, bomb))