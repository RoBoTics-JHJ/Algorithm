# 표준 입출력 파일 설정 ####################################################
import os
import sys
os.chdir(os.path.dirname(__file__))
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
###########################################################################
N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

tmp_stack = []


def func():
    if len(tmp_stack) == M:
        print(' '.join(map(str, tmp_stack)))
        return

    for i in nums:
        if i not in tmp_stack:
            tmp_stack.append(i)

            func()

            tmp_stack.pop()


func()
