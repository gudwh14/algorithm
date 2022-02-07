def solution(record):
    users = {}
    answer = []

    # uid 에 해당하는 유저 이름 변경
    for log in record:
        text = log.split(' ')
        if text[0] == 'Enter':
            users[text[1]] = text[2]
        elif text[0] == 'Change':
            users[text[1]] = text[2]

    # 유저 입장, 퇴장 출력 찍기
    for log in record:
        text = log.split(' ')
        if text[0] == 'Enter':
            user = users[text[1]]
            answer.append(user + '님이 들어왔습니다.')
        elif text[0] == 'Leave':
            user = users[text[1]]
            answer.append(user + '님이 나갔습니다.')

    return answer
