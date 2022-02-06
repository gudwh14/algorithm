from functools import cmp_to_key


def solution(files):
    def compare(x: str, y: str):
        # 문자열을 , 문자 배열로 변환
        _x = list(x)
        _y = list(y)

        x_head = ''
        y_head = ''
        x_num = ''
        y_num = ''
        # 각각 HEAD 구하기, HEAD : 숫자가아닌 문자로만 이루어짐
        for char in _x:
            if char.isdigit():
                break
            x_head += char
        for char in _y:
            if char.isdigit():
                break
            y_head += char

        # NUMBER 구하기, NUMBER : 연속된 숫자로만 이루어짐, 최대 5자리
        for i in range(len(x_head), len(_x)):
            if len(x_num) == 5:
                break
            if _x[i].isdigit():
                x_num += _x[i]
            else:
                break
        for i in range(len(y_head), len(_y)):
            if len(y_num) == 5:
                break
            if _y[i].isdigit():
                y_num += _y[i]
            else:
                break

        # HEAD 는 대소문자 비교 X
        x_head = x_head.lower()
        y_head = y_head.lower()

        # HEAD 가 같을경우 NUMBER 숫자 크기순으로 정렬
        if x_head == y_head:
            return int(x_num) - int(y_num)
        # 아닐경우 사전순으로 정렬
        else:
            if x_head > y_head:
                return 1
            elif x_head < y_head:
                return -1

    files.sort(key=cmp_to_key(compare))
    return files


print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))