# 표준 입출력 파일 설정 #######################################################
import os
import sys

os.chdir(os.path.dirname(__file__))
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
###########################################################################
# N, M = map(int, input().split())
#
# tmp_stack = []
#
#
# def func(start):
#     if len(tmp_stack) == M:
#         print(' '.join(map(str, tmp_stack)))
#         return
#
#     for i in range(start, N + 1):
#         if i not in tmp_stack:
#             tmp_stack.append(i)
#
#             func(i + 1)
#
#             tmp_stack.pop()
#
#
# func(1)


from itertools import combinations

N, M = map(int, input().split())

nums = [i for i in range(1, N + 1)]
combination_list = combinations(nums, M)  # tuple(int) 반환

for i in combination_list:
    print(' '.join(map(str, i)))
