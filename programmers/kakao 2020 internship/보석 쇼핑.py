import collections


def solution(gems):
    answer = []
    shortest = len(gems) + 1  # 현재 최단 길이

    left = right = 0  # 투포인터 초기화
    number_of_kind = len(set(gems))  # 보석의 총 종류 개수
    contained = collections.defaultdict(int)

    while right < len(gems):
        # dict 에 보석 추가
        contained[gems[right]] += 1
        right += 1

        # 현재 dict 에 보석 종류가 총 보석 종류 개수와 같아지면
        if len(contained) == number_of_kind:
            # 왼쪽 포인터를 오른쪽 포인터 까지 이동
            while left < right:
                # 왼쪽 포인터가 가르키는 보석이 1개 보다 많으면
                # 왼쪽 포인터 이동
                if contained[gems[left]] > 1:
                    contained[gems[left]] -= 1
                    left += 1
                # 1개 보다 적으면 최단 거리 갱신 및 answer 갱신
                elif right - left < shortest:
                    shortest = right - left
                    answer = [left + 1, right]
                    break
                # 최단거리 보다 길면 break
                else:
                    break

    return answer


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
