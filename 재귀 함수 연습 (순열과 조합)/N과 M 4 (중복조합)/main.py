# 표준 입출력 파일 설정 ####################################################
import os
import sys
os.chdir(os.path.dirname(__file__))
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
###########################################################################
N, M = map(int, input().split())

tmp_stack = []


def func():
    if len(tmp_stack) == M:
        print(' '.join(map(str, tmp_stack)))
        return

    for i in range(0, N):
        if len(tmp_stack) == 0 or tmp_stack[-1] <= (i + 1):
            tmp_stack.append(i + 1)

            func()

            tmp_stack.pop()


func()
