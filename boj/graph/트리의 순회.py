# POSTORDER 의 마지막값은 항상 ROOT
# ROOT를 이용하여 INORDER에서 ROOT INDEX를 이용하여 LEFT, RIGHT 분할
# 분할정복

# INDEX 찾을때 index 함수 말고 index 배열을 따로 저장하여 시간 줄이기

import sys

sys.setrecursionlimit(10**6)
n = int(input())

inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
index = [-1 for _ in range(100001)]

for idx, value in enumerate(inorder):
    index[value] = idx 

def getPreOrder(inStart, inEnd, postStart, postEnd):
    if inEnd < inStart or postEnd < postStart:
        return

    root = postorder[postEnd]
    inRootIndex = index[root]
    print(root, end=' ')

    getPreOrder(inStart, inRootIndex - 1, postStart, postEnd - (inEnd - inRootIndex) - 1)
    getPreOrder(inRootIndex + 1, inEnd, postEnd - (inEnd - inRootIndex), postEnd - 1)

def solution():
    getPreOrder(0, n - 1, 0, n -1)

solution()
