# u, v 로 나눠주는 함수
# u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며 -> 최소길이의 균형잡힌 괄호 문자열이라는 뜻
def divide_u_v(brackets):
    left = 0
    right = 0

    for i in range(len(brackets)):
        if brackets[i] == '(':
            left += 1
        elif brackets[i] == ')':
            right += 1
        if left == right:
            break
    u = brackets[0:i + 1]
    v = brackets[i + 1:] if i + 1 < len(brackets) else ""
    return u, v


# 올바른 괄호인지 체크하는 함수
def is_right_bracket(brackets):
    q = []
    for bracket in brackets:
        if bracket == '(':
            q.append(bracket)
        else:
            if q and q[-1] == '(':
                q.pop()
            else:
                return False
    if q:
        return False
    return True


# 변환 함수
def change(brackets):
    result = ""
    # 입력이 빈 문자열이면 빈 문자열 반환
    if not brackets:
        return ""

    # u, v 구하기
    u, v = divide_u_v(brackets)
    # u 가 올바른 괄호문자열이면, v 를 변환 수행후 u 에 붙힌후 반환
    if is_right_bracket(u):
        result = u + change(v)
    # u 가 올바른 괄호문자열이 아니면
    else:
        temp = "("
        temp += change(v)
        temp += ")"

        u = u[1:-1]
        for bracket in u:
            if bracket == '(':
                temp += ')'
            else:
                temp += '('
        result += temp
    return result


# 재귀함수를 이용하여 풀어야함!
def solution(p):
    answer = ''
    if is_right_bracket(p):
        return p

    answer = change(p)
    return answer


print(solution("()))((()"))
