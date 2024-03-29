[문제보기](https://www.acmicpc.net/problem/15649) <br/>
시간 제한: 1초 (20,000,000 연산) <br/>
메모리 제한: 512MB <br/>
(1 ≤ M ≤ N ≤ 8)
## 백트레킹 (순열)
### 1번 풀이 (212ms, 117MB)
```python
N, M = map(int, input().split())

check_list = [0] * N 
tmp_stack = []


def func():
    # 백트래킹 가지치기(pruning)
    if len(tmp_stack) == M:
        print(' '.join(map(str, tmp_stack)))
        return

    for i in range(0, N):
        if check_list[i]:
            continue
            
        check_list[i] = True
        tmp_stack.append(i + 1)

        func()

        check_list[i] = False
        tmp_stack.pop()


func()
```
- DFS 탐색 중, **" len(tmp_stack) == M "** 일 때 출력함 (= 백트래킹 기법)
- 정석대로 푼 케이스. "2번 풀이"처럼 풀면 check_list가 필요 없음
<br/><br/><br/>
### 2번 풀이 (204ms, 117MB)
```python
N, M = map(int, input().split())

tmp_stack = []

def func():
    # 백트래킹 가지치기(pruning)
    if len(tmp_stack) == M:
        print(' '.join(map(str, tmp_stack)))
        return

    for i in range(1, N+1):
        if i not in tmp_stack:  # Containment(포함 여부 확인) => O(n)
            tmp_stack.append(i)
            
            func()
            
            tmp_stack.pop()


func()
```
<br/><br/><br/>
### 3번 풀이 (160ms, 115MB)
```python
from itertools import permutations

N, M = map(int, input().split())

nums = [i for i in range(1, N + 1)]
permutation_list = permutations(nums, M)  # tuple(int) 반환

for i in permutation_list:
    print(' '.join(map(str, i)))
```
- itertools 모듈로 구현된 순열 함수 ( = permutations) 사용

