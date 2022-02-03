# 연결리스트를 사용하여 삽입, 삭제
def solution(n, k, cmd):
    linked_list = {i: [i - 1, i + 1] for i in range(1, n + 1)}
    delete = []
    answer = ["O" for _ in range(1, n + 1)]

    k += 1
    for command in cmd:
        if command[0] == 'D':
            # D 명령어를 만나면 X 칸 만큼 다음 원소를 가르킴
            for _ in range(int(command[2:])):
                k = linked_list[k][1]
        elif command[0] == 'U':
            # U 명령어를 만나면 X 칸 만큼 이전 원소를 가르킴
            for _ in range(int(command[2:])):
                k = linked_list[k][0]
        elif command[0] == 'C':
            prev, next = linked_list[k]
            # 이전, 다음, 현재 값을 가르키는 배열을 삭제 배열에 추가
            delete.append([prev, next, k])
            # 해당 원소 값을 X 로 변경
            answer[k - 1] = 'X'
            # 삭제하려는 원소가 마지막 값일경우
            if next == n + 1:
                k = linked_list[k][0]
            # 아닐경우 다음 원소를 가르킴
            else:
                k = linked_list[k][1]

            # 삭제하려는 원소가 두번째 원소일 경우 next 의 이전 값을 삭제하려는 값의 prev 를 참조하도록 변경
            if prev == 0:
                linked_list[next][0] = prev
            # 삭제하려는 원소가 마지막에서 -1 원소일 경우 prev 의 다음값을 삭제하려는 값의 next 를 참조하도록 변경
            elif next == n + 1:
                linked_list[prev][1] = next
            # 그 외 경우 링크 바꾸기
            else:
                linked_list[prev][1] = next
                linked_list[next][0] = prev

        # 삭제 한 원소를 스택에서 꺼내서 복원
        elif command[0] == 'Z':
            prev, next, now = delete.pop()
            answer[now - 1] = 'O'

            # 링크 복원해주기
            if prev == 0:
                linked_list[next][0] = now
            elif next == n + 1:
                linked_list[prev][1] = now
            else:
                linked_list[prev][1] = now
                linked_list[next][0] = now
    return ''.join(answer)


print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))
