# 표준 입출력 파일 설정 ####################################################
import os
import sys

os.chdir(os.path.dirname(__file__))
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
###########################################################################
while True:
    line = input()
    if line == '.':
        break

    left_open = '('
    right_open = ')'
    left_close = '['
    right_close = ']'

    tmp_que = []

    for l in line:
        if l == left_open or l == right_open or l == left_close or l == right_close:
            tmp_que.append(l)

    for t in tmp_que:
        if t ==




    print(tmp_que)



