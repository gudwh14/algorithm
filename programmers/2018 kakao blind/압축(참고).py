def solution(msg):
    answer = []
    dic = {}

    # 반복문으로 알파벳 dic 만들기
    for i in range(26):
        dic[chr(65+i)] = i+1
    # w, c index
    w, c = 0, 0

    while True:
        # c 인덱스 증가
        c += 1
        # c 인덱스가 마지막을 가리키면 탈출
        if c == len(msg):
            answer.append(dic[msg[w:c]])
            break
        # 해당 문자열이 dic 에 없으면 dic 을 만들고, 해당 되는값을 출력
        # w 인덱스를 c 인덱스로 교체
        if msg[w:c+1] not in dic:
            dic[msg[w:c+1]] = len(dic) + 1
            answer.append(dic[msg[w:c]])
            w = c

    return answer


print(solution('KAKAO'))
# print(solution("TOBEORNOTTOBEORTOBEORNOT"))
