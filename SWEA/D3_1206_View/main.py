# 표준 입출력 파일 설정 ####################################################
import os
import sys

os.chdir(os.path.dirname(__file__))
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
###########################################################################
for case in range(10):
    N = int(input())
    building = list(map(int, input().split()))

    anw = 0
    for i in range(2, N - 2):
        diff_l_1 = building[i] - building[i - 1]
        diff_l_2 = building[i] - building[i - 2]
        diff_r_1 = building[i] - building[i + 1]
        diff_r_2 = building[i] - building[i + 2]

        if diff_l_1 > 0 and diff_l_2 > 0 and diff_r_1 > 0 and diff_r_2 > 0:
            anw += min(diff_l_1, diff_l_2, diff_r_1, diff_r_2)

    print(f'#{case + 1} {anw}')
