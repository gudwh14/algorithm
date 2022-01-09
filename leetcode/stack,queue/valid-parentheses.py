class Solution:
    def isValid(self, s: str) -> bool:
        # 왼쪽 브라켓들을 저장하는 스택
        left_list = []
        # 왼쪽 브라켓 key 로 매칭되는 브라켓들을 딕셔너리로 생성
        brackets = {'(': ')', '[': ']', '{': '}'}

        # 왼쪽 기호 브라켓을 만나면 left_list 에 저장하고 오른쪽 기호 브라켓을 만나면 left_list 에서 pop하여 비교한다
        for i in s:
            if i in ['(', '[', '{']:
                left_list.append(i)
            elif i in [')', ']', '}']:
                # 오른쪽 브라켓을 만났는데 왼쪽 브라켓 리스트가 없을경우 false
                if not left_list:
                    return False
                # 왼쪽 기호 브라켓과 일치하지않을경우 false
                if brackets[left_list.pop()] != i:
                    return False

        # 아직 리스트가 남아있으면 짝이 안맞는 경우 false
        if left_list:
            return False

        return True


s = Solution()
print(s.isValid("()[]{}"))
