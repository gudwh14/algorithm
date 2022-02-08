def solution(s):
    answer = 0

    # 문자열 자를 개수 문자열의 길이의 절반만큼 반복
    for i in range(1, len(s) // 2 + 1):
        idx = 0
        count = 1
        temp = ''
        reduce_count = 0

        # 문자열 반복
        while idx <= len(s):
            # 템프에 첫문자열 넣기
            if not temp:
                temp = s[idx:idx + i]
            else:
                # 반복되는 문자를 찾으면 카운트 증가
                if temp == s[idx:idx + i]:
                    count += 1
                else:
                    # 반복되는 문자열이 아닌 다른 문자열을 만났을때 카운트를 체크
                    # 카운트가 1 보다 크면, 반복되는 문자가 있다는 의미, 감소되는 문자 개수 구하기
                    if count > 1:
                        reduce_count += (count * i) - i - 1
                        # 카운트가 10 이상이면 감소되는 문자개수를 1개 뺴줘야함 10a 일경우 1자리를 더 차지하기 때문
                        if count >= 10:
                            reduce_count -= 1
                        count = 1
                    # 템프 교체하기
                    temp = s[idx:idx + i]
            # 인덱스는 자르는 개수만큼 증가해야함
            idx += i

        # 문자열 탐색이 끝나고 카운터가 1보다 클경우 처리
        if count > 1:
            reduce_count += (count * i) - i - 1
            if count >= 10:
                reduce_count -= 1

        # 감소되는 문자열중 가장 많이 감소되는 값 찾기
        answer = max(answer, reduce_count)

    # 문자열 길이에서 감소되는 문자 개수 뺴주기
    return len(s) - answer


print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("xxxxxxxxxxyyy"))
