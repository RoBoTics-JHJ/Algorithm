# 표준 입출력 파일 설정 #######################################################
import os
import sys
os.chdir(os.path.dirname(__file__))
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
###########################################################################
N, M = map(int, input().split())

check_list = [False] * N
tmp_stack = []


def func():
    if len(tmp_stack) == M:
        print(' '.join(map(str, tmp_stack)))
        return

    for i in range(0, N):
        if check_list[i] is False and (len(tmp_stack) == 0 or tmp_stack[-1] < (i + 1)):
            check_list[i] = True
            tmp_stack.append(i + 1)

            func()

            check_list[i] = False
            tmp_stack.pop()


func()
