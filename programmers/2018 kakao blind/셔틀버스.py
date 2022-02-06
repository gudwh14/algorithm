def solution(n, t, m, timetable):
    now = [9, 0]
    # 시간 역순으로 정렬
    timetable.sort(reverse=True)

    # 제일 늦는 도착시간을 구하기 위해서 마지막 버스 시간을 탑승해야 함
    # 마지막 버스시간에 탑승할수있는 크루만 남겨 놓기
    while n > 1:
        n -= 1

        for _ in range(m):
            if (int(timetable[-1][:2]) * 60 + int(timetable[-1][-2:])) <= (now[0] * 60 + now[1]):
                timetable.pop()
        now[0], now[1] = now[0] + (now[1] + t) // 60, (now[1] + t) % 60

    # 마지막 탑승시간에 타기 위해서 한자리가 남아있어야함으로
    # m - 1 개 만큼 pop하기
    for _ in range(m - 1):
        if (int(timetable[-1][:2]) * 60 + int(timetable[-1][-2:])) <= (now[0] * 60 + now[1]):
            timetable.pop()

    # 자리가 없으면 맨뒤에 위치한 사람이 도착시간보다 일찍 왔다면 그사람 보다 1분 일찍 도착해야함
    if (len(timetable) > 0) and (int(timetable[-1][:2]) * 60 + int(timetable[-1][-2:])) <= (now[0] * 60 + now[1]):
        answer = timetable[-1]
        # 0 분이면 시간 - 1, 분을 59로 변경
        if answer[-2:] == "00":
            answer = str(int(answer.split(":")[0]) - 1).zfill(2) + ":59"
        # 아니면 분 - 1
        else:
            answer = answer.split(":")[0].zfill(2) + ":" + str(int(answer.split(":")[1]) - 1).zfill(2)
    # 자리가 있으면 마지막 탑승시간에 도착하면 됨
    else:
        answer = str(now[0]).zfill(2) + ":" + str(now[1]).zfill(2)

    return answer


# print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))
print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))
