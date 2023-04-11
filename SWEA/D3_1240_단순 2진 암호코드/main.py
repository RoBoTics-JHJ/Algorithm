# 표준 입출력 파일 설정 ####################################################
import os
import sys
os.chdir(os.path.dirname(__file__))
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
###########################################################################
case = int(input())
key_dict = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
            '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}

for c in range(case):
    num_list, cnt = map(int, input().split())
    num_list = [','.join(str(num_list))]
    N, M = map(int, input().split())

    for _ in range(N):
        key_arr = [list(map(int, input().split()))]
        pass

