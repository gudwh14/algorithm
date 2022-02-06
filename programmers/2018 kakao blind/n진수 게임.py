def solution(n, t, m, p):
    n_num = []
    # 16 진수 까지 변환을 위한 해쉬 만들기
    dict = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E',
            15: 'F'}

    # 해당 숫자를 원하는 진수로 변경하는 함수
    def number_to_n(number):
        while number >= n:
            mod = number % n
            number = number // n
            n_num.insert(0, dict[mod])
        n_num.insert(0, dict[number])

    start = 0
    count = 0
    result = []
    answer = []
    while True:
        # 원하는 턴만큼 게임이 진행되면 종료
        if count >= m * t:
            break
        # 진행되는 숫자 진법으로 변환
        number_to_n(start)
        # 해당 진법을 다 출력할때까지 반복
        while n_num:
            result.append(n_num.pop(0))
            # 턴 증가
            count += 1
            # 원하는 턴만큼 게임이 진행되면 종료
            if count >= m * t:
                break
        # 숫자 증가
        start += 1

    # 원하는 턴의 출력값 뽑기
    for idx, num in enumerate(result):
        if idx % m == p - 1:
            answer.append(str(num))

    return "".join(answer)


print(solution(2, 4, 2, 1))
print(solution(16, 16, 2, 1))
print(solution(16, 16, 2, 2))
