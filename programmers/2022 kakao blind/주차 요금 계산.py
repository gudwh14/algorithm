import collections
import math


# 시간을 정수형 시간으로 변경하는 함수
def convert_to_num(time: str):
    times = time.split(':')
    hour = int(times[0]) * 60
    minute = int(times[1])
    return hour + minute


def solution(fees, records):
    last = 23 * 60 + 59
    # 주차된 시간을 저장하는 해쉬
    cars = collections.defaultdict(list)
    # 총 주차 시간을 저장하는 해쉬
    times = collections.defaultdict(int)
    answer = []

    # 입차, 출차 기준으로 총 주차 시간 구하기
    for record in records:
        record = record.split(' ')
        if record[2] == 'IN':
            cars[record[1]].append(convert_to_num(record[0]))
        elif record[2] == 'OUT':
            in_time = cars[record[1]].pop(0)
            out_time = convert_to_num(record[0])

            times[record[1]] += out_time - in_time

    # 아직 입차된 차가 남이있으면 마지막시간에 출차로 계산
    for key, value in cars.items():
        if value:
            times[key] += last - value.pop(0)

    # 총 주차시간으로 주차금액 계산하기
    for key, value in times.items():
        if value - fees[0] > 0:
            value = fees[1] + math.ceil((value - fees[0]) / fees[2]) * fees[3]
        else:
            value = fees[1]
        times[key] = value

    # 차량번호판 기준으로 오름차순 정렬하여 정답 도출
    for key, value in sorted(times.items()):
        answer.append(value)
    return answer


print(solution([180, 5000, 10, 600],
               ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN",
                "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
