import collections


def solution(clothes):
    answer = 1
    clothes_dict = collections.defaultdict(int)

    for cloth in clothes:
        clothes_dict[cloth[1]] += 1

    # 옷 종류의 개수가 n 개이면 선택지는 n + 1 개이다
    for key, value in clothes_dict.items():
        answer *= (value + 1)

    # answer 는 모든 옷을 안입은 경우도 포함이니 -1 을 하여 그 경우를 제거
    return answer - 1


print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
