import collections
import itertools


def solution(orders, course):
    menus = collections.defaultdict(list)
    answer = []

    # 코스 요리 구하기
    for count in course:
        # 모든 주문을 확인
        for order in orders:
            # 문자열을, 배열로 변환
            list_order = list(order)
            # 오름차순으로 정렬
            list_order.sort()
            # 코스 요리 개수만큼 조합 만들기
            itertools.combinations(list_order, count)
            # 만들어진 조합을 dict 에 추가
            comb = [''.join(list(ele)) for ele in (itertools.combinations(list_order, count))]
            menus[count].extend(comb)

        # 코스 요리 개수에 해당하는 조합 꺼내서, 카운팅 한후 배열로 변경
        menu_count = collections.Counter(menus[count]).most_common()
        # 존재하면 실행
        if menu_count:
            most_value = menu_count[0][1]
            # 최소 2명 이상 손님이 주문했을 경우에만
            if most_value > 1:
                # 코스요리에 추가
                answer.append(menu_count[0][0])
                # 같은 횟수만큼 나올수 있으므로, 같은 횟수이면 추가
                for i in range(1, len(menu_count)):
                    if most_value == menu_count[i][1]:
                        answer.append(menu_count[i][0])
                    else:
                        break

    # 오름차순으로 정렬
    answer.sort()
    return answer


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))
