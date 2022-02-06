def solution(lines):
    def str_to_time(string: str):
        hour = int(string[0:2]) * 3600
        minute = int(string[3:5]) * 60
        seconds = int(string[6:8])
        milli = int(string[9:])

        return (hour + minute + seconds) * 1000 + milli

    def get_start_time(end_time, duration: str):
        return int(end_time - float(duration[:-1]) * 1000 + 1)

    start_times = []
    end_times = []
    answer = 0

    # 시작시간, 끝나는 시간을 정수형 시간으로 변환
    for line in lines:
        start_times.append(get_start_time(str_to_time(line.split(' ')[1]), line.split(' ')[2]))
        end_times.append(str_to_time(line.split(' ')[1]))

    for i in range(len(lines)):
        count = 0

        for j in range(i, len(lines)):
            # 1000ms 구간안 개수 구하기
            # end_times 는 오름차순으로 정렬이 보장되어있음 , start_times 는 정렬 X
            # 현재 끝나는 시간을 기준으로, 다음 시작시간 에서 1000ms 을 뺀 값이 현재 끝나는 시작시간보다 작다면 1000ms 범위안에 존재하는것임
            if end_times[i] > start_times[j] - 1000:
                count += 1
        # 맥스값 지정
        answer = max(answer, count)

    return answer


print(solution([
    "2016-09-15 20:59:57.421 0.351s",
    "2016-09-15 20:59:58.233 1.181s",
    "2016-09-15 20:59:58.299 0.8s",
    "2016-09-15 20:59:58.688 1.041s",
    "2016-09-15 20:59:59.591 1.412s",
    "2016-09-15 21:00:00.464 1.466s",
    "2016-09-15 21:00:00.741 1.581s",
    "2016-09-15 21:00:00.748 2.31s",
    "2016-09-15 21:00:00.966 0.381s",
    "2016-09-15 21:00:02.066 2.62s"
]))
