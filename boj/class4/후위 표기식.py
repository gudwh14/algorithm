def solution(exp):
    op = []
    val = []
    open = 0

    for char in exp:
        if char == '(' or char == '*' or char == '/':
            if char == '(':
                open += 1
            if char == '*' or char == '/':
                while op and (op[-1] == '*' or op[-1] == '/'):
                    val.append(op.pop())
            op.append(char)
        elif char == '+' or char == '-':
            if open > 0:
                while op[-1] != '(':
                    val.append(op.pop())
            else:
                while op:
                    val.append(op.pop())

            op.append(char)
        elif char == ')':
            while op[-1] != '(':
                val.append(op.pop())
            op.pop()
            open -= 1
        else:
            val.append(char)

    while op:
        val.append(op.pop())

    return ''.join(val)


exp = input()
print(solution(exp))
