def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1]) # 차량 진출 기준으로 정렬
    leng = len(routes)
    checked = [0] * leng

    for i in range(leng):
        # 단속 X 일경우 카메라 갱신
        if checked[i] == 0:
            camera = routes[i][1]  # 진출 지점에 카메라를 갱신
            answer += 1
        # 해당 카메라에 단속되는 차량들 구하기
        for j in range(i + 1, leng):
            if routes[j][0] <= camera <= routes[j][1] and checked[j] == 0:
                checked[j] = 1
    return answer


def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1])  # routes를 차량이 나간 지점 (진출) 기준으로 정렬
    camera = -30001  # -30001부터 카메라 위치를 찾습니다.

    for route in routes:
        if camera < route[0]:
            answer += 1
            camera = route[1]
    return answer


print(solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3]]))
print(solution([[-11, -10], [-9, -8], [-7, -6], [-6, -5]]))
