import sys

# 재귀 반복문 회수 제한을 풀어야함!
sys.setrecursionlimit(10**6)

# 노드 클래스 정의
class Node:
    # key: 값 , x: x좌표
    def __init__(self, key, x):
        self.key = key
        self.x = x
        self.left, self.right = None, None


# 트리 클래스 정의
class Tree:
    def __init__(self, head, x):
        # 헤드 값, x값
        self.head = Node(head, x)

    # 트리 노드 삽입하기
    def insert(self, key, x):
        # 현재 노드는 루트 노드로 초기화
        cur_node = self.head
        while True:
            # 루트의 x 보다 작으면 left에 추가
            if cur_node.x > x:
                if cur_node.left == None:
                    cur_node.left = Node(key, x)
                    break
                else:
                    cur_node = cur_node.left
            # 루트의 x 보다 크면 right에 추가
            elif cur_node.x < x:
                if cur_node.right == None:
                    cur_node.right = Node(key, x)
                    break
                else:
                    cur_node = cur_node.right

    # 전위 순회
    def pre_order(self):
        result = []

        def order(node):
            result.append(node.key)
            if node.left != None:
                order(node.left)
            if node.right != None:
                order(node.right)

        order(self.head)
        return result

    # 후위 순회
    def post_order(self):
        result = []

        def order(node):
            if node.left != None:
                order(node.left)
            if node.right != None:
                order(node.right)
            result.append(node.key)

        order(self.head)
        return result


def solution(nodeinfo):
    answer = []
    for i in range(len(nodeinfo)):
        nodeinfo[i] = [i + 1] + nodeinfo[i]
    nodeinfo.sort(key=lambda x: x[2], reverse=True)
    tree = Tree(nodeinfo[0][0], nodeinfo[0][1])

    for i in range(1, len(nodeinfo)):
        tree.insert(nodeinfo[i][0], nodeinfo[i][1])

    answer.append(tree.pre_order())
    answer.append(tree.post_order())
    return answer


print(solution([[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]))
print(solution([[5, 3]]))
