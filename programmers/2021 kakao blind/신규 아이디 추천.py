def is_correct_id(id):
    n = len(id)
    dot_count = 0
    if not (3 <= n <= 15):
        return False

    if id[0] == '.' or id[-1] == '.':
        return False

    for i in range(n):
        if not (id[i].islower() or id[i].isdigit() or id[i] == '-' or id[i] == '_' or id[i] == '.'):
            return False
        if id[i] == '.':
            dot_count += 1
            if dot_count > 1:
                return False
        else:
            dot_count = 0
    return True


def solution(new_id):
    if is_correct_id(new_id):
        return new_id
    else:
        # 소문자로 변환
        new_id = new_id.lower()
        # 문자 배열로 변환
        new_id = list(new_id)
        n = len(new_id)
        i = 0
        # 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거
        while i < n:
            if not (new_id[i].islower() or new_id[i].isdigit() or new_id[i] == '-' or new_id[i] == '_' or new_id[
                i] == '.'):
                del new_id[i]
                n -= 1
                continue
            i += 1

        dot_count = 0
        n = len(new_id)
        i = 0
        # 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환
        while i < n:
            if new_id[i] == '.':
                dot_count += 1
            else:
                if dot_count > 1:
                    find = i
                    for j in range(dot_count - 1):
                        del new_id[find - 1 - j]
                        i -= 1
                        n -= 1
                    dot_count = 0
                else:
                    dot_count = 0
            i += 1
        new_id = ''.join(new_id)
        new_id = new_id.strip('.')
        if not new_id:
            new_id += 'a'

        if len(new_id) >= 16:
            new_id = new_id[:15]
            if new_id[-1] == '.':
                new_id = new_id[:14]

        if len(new_id) <= 2:
            while len(new_id) < 3:
                new_id += new_id[-1]
    return new_id


print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("a...a"))
print(solution("......a......a......a....."))
