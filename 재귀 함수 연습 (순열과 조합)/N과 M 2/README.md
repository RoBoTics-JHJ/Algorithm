[문제보기](https://www.acmicpc.net/problem/15650)


## 백트레킹 (순열 구현)

### 1번 풀이
```python
N, M = map(int, input().split())

check_list = [0] * N 
tmp_stack = []


def dfs():
    # 백트래킹 가지치기(pruning)
    if len(tmp_stack) == M:
        print(' '.join(map(str, tmp_stack)))

    for i in range(0, N):
        if check_list[i]:
            continue
            
        check_list[i] = True
        tmp_stack.append(i + 1)

        dfs()

        tmp_stack.pop()
        check_list[i] = False


dfs()
```
- DFS 탐색하여, **len(tmp_stack) == M** 일 때 출력함 (= 백트래킹 기법)
<br/><br/><br/>

### 2번 풀이
```python
from itertools import permutations

N, M = map(int, input().split())

nums = [i for i in range(1, N + 1)]
permutated_list = permutations(nums, M)  # tuple(int) 반환

for i in permutated_list:
    print(' '.join(map(str, i)))
```
- itertools 모듈로 구현된 순열 함수 (=permutations) 사용

