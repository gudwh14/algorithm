def solution(s):
    _s = []
    temp = []
    answer = []
    num = ''
    # 스트링 튜플을 배열로 변환
    for char in s:
        if char.isdigit():
            num = num + char
        elif char == ',' and num:
            temp.append(int(num))
            num = ''
        elif char == '}' and num:
            temp.append(int(num))
            num = ''
            _s.append(temp)
            temp = []

    # key : 길이 로 정렬
    _s.sort(key=lambda x: len(x))
    # result 구하기
    for item in _s:
        for number in item:
            if number not in answer:
                answer.append(number)

    return answer


print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))
# print(solution("{{20,111},{111}}"))
