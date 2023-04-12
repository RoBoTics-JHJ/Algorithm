# 표준 입출력 파일 설정 ####################################################
import os
import sys

os.chdir(os.path.dirname(__file__))
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
###########################################################################
# N, M = map(int, input().split())
#
# check_list = [0] * N
# tmp_stack = []
#
#
# def dfs():
#     if len(tmp_stack) == M:
#         print(' '.join(map(str, tmp_stack)))
#
#     for i in range(0, N):
#         if check_list[i]:
#             continue
#
#         check_list[i] = True
#         tmp_stack.append(i + 1)
#
#         dfs()
#
#         tmp_stack.pop()
#         check_list[i] = False
#
#
# dfs()


from itertools import permutations

N, M = map(int, input().split())

nums = [i for i in range(1, N + 1)]
permutated_list = permutations(nums, M)  # tuple(int) 반환

for i in permutations(nums, M):
    print(*i)