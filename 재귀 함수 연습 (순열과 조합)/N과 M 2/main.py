# 표준 입출력 파일 설정 #######################################################
import os
import sys
os.chdir(os.path.dirname(__file__))
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
###########################################################################
N, M = map(int, input().split())

check_list = [0] * N
tmp_stack = []


def dfs():
    # 백트래킹 가지치기(pruning)
    if len(tmp_stack) == M:
        print(' '.join(map(str, tmp_stack)))
        return

    for i in range(0, N):
        if check_list[i]:
            continue

        check_list[i] = True
        tmp_stack.append(i + 1)

        dfs()

        tmp_stack.pop()
        check_list[i] = False


dfs()
