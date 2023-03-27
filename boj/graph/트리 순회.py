import collections

N = int(input())

graph = collections.defaultdict(list)

for _ in range(N):
    info = list(input().split())
    graph[info[0]].extend(info[1:3])

def preorder(node):
    print(node, end= '')
    if graph[node][0] != '.':
        preorder(graph[node][0])
    if graph[node][1] != '.':
        preorder(graph[node][1])

def inorder(node):
    if graph[node][0] != '.':
        inorder(graph[node][0])
    print(node, end= '')
    if graph[node][1] != '.':
        inorder(graph[node][1])

def postorder(node):
    if graph[node][0] != '.':
        postorder(graph[node][0])
    if graph[node][1] != '.':
        postorder(graph[node][1])
    print(node, end= '')

def solution():
    preorder('A')
    print()
    inorder('A')
    print()
    postorder('A')

solution()
