# 문자열 시간을 정수형 시간으로 변경하는 함수
def time_to_number(time: str):
    time = time.split(':')
    hour = int(time[0]) * 3600
    minute = int(time[1]) * 60
    seconds = int(time[2])

    return hour + minute + seconds


# 정수형 시간을 문자열 시간으로 변경하는 함수
def number_to_time(number: int):
    hour = number // 3600
    minute = (number - 3600 * hour) // 60
    seconds = (number - 3600 * hour - 60 * minute)

    hour = '0' + str(hour) if hour < 10 else str(hour)
    minute = '0' + str(minute) if minute < 10 else str(minute)
    seconds = '0' + str(seconds) if seconds < 10 else str(seconds)
    return hour + ':' + minute + ':' + seconds


def solution(play_time, adv_time, logs):
    # 총 플레이 시간을 정수형으로 변환
    play_time = time_to_number(play_time)
    # 광고 길이를 정수형으로 변환
    adv_time = time_to_number(adv_time)
    # logs 의 시청 시작 시간들을 담아둔 변수
    start = []
    # logs 의 시청 종료 시간들을 담아둔 변수
    end = []
    # 총 시간에대한 누적 시청자수를 저장 하는 변수 최대 360000개의 시간이 나온다
    total_time = [0 for _ in range(play_time + 1)]

    if play_time == adv_time:
        return '00:00:00'

    # 시작, 끝을 정수형으로 바꿔 저장
    for log in logs:
        log = log.split('-')
        # 1
        start.append(time_to_number(log[0]))
        # 2
        end.append(time_to_number(log[1]))

    # 3
    # i 시간에 시청중인 시청자수를 계산
    # start 시간이면 + 1
    # end 시간이면 - 1
    for i in range(len(logs)):
        total_time[start[i]] += 1
        total_time[end[i]] -= 1

    # 4
    # 구간별 시청자수 구하기
    for i in range(1, play_time):
        total_time[i] = total_time[i] + total_time[i - 1]

    # 5
    # 모든 구간별 시청자수 구하기
    for i in range(1, play_time):
        total_time[i] = total_time[i] + total_time[i - 1]

    # 6
    # 누적된 시청자수를 통하여, 가장 시청자수가 많은 구간 탐색하기
    most_view = 0
    max_time = 0
    # 광고 길이 - 1 부터 탐색 시작,
    # 현재 i의 누적 시청자수에서 i-adv_time의 누적 시청자수를 빼면 해당 구간의 시청자수 값을 얻을 수 있습니다
    for i in range(adv_time - 1, play_time):
        if i >= adv_time:
            if most_view < total_time[i] - total_time[i - adv_time]:
                most_view = total_time[i] - total_time[i - adv_time]
                max_time = i - adv_time + 1
        else:
            if most_view < total_time[i]:
                most_view = total_time[i]
                max_time = i - adv_time + 1

    return number_to_time(max_time)


print(solution("99:59:59", "25:00:00",
               ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))
