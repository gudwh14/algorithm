def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    answer = n - len(lost)
    remove = []

    # 여벌 체육복을 가져온 학생이 , 도난당했을 경우 체크
    for i in range(0, len(reserve)):
        if reserve[i] in lost:
            remove.append(reserve[i])

    # 다른학행에게 빌려줄수 없음
    for item in remove:
        lost.remove(item)
        reserve.remove(item)
        answer += 1

    # 여벌 체육복 빌려줄수 있는지 체크
    for res in reserve:
        if answer >= n:
            return n

        if res - 1 in lost or res + 1 in lost:
            answer += 1

    return answer


print(solution(5, [2, 4], [1, 3, 5]))
print(solution(4, [1, 3], [1, 4]))
