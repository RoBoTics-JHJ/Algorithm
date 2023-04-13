[문제보기](https://www.acmicpc.net/problem/15650)

시간 제한: 1초 (20,000,000 연산) <br/>
메모리 제한: 512MB <br/>
(1 ≤ M ≤ N ≤ 8)
## 백트레킹 (조합)
### 1번 풀이 (120ms, 114MB)
```python
N, M = map(int, input().split())

check_list = [False] * N
tmp_stack = []


def func():
    # 백트래킹 가지치기(pruning)
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
```
<br/><br/><br/>
### 2번 풀이 (124ms, 113MB)
```python
N, M = map(int, input().split())

tmp_stack = []


def func(start):
    # 백트래킹 가지치기(pruning)
    if len(tmp_stack) == M:
        print(' '.join(map(str, tmp_stack)))
        return

    for i in range(start, N + 1):
        if i not in tmp_stack:  # Containment(포함 여부 확인) => O(n)
            tmp_stack.append(i)
            
            func(i + 1)
            
            tmp_stack.pop()


func(1)

```
- 함수 func()에 매개변수를 주지 않으면, 모든 경우가 출력됨 ( = "N과 M 1" 문제)
- **start** 매개변수 >> for문 range와 func(i + 1) 주목 ( = 오름차순 )
<br/><br/>
<p align="center"><img width="95%" height="95%" src="img.png"></p>
<br/><br/><br/>

### 3번 풀이 (120ms, 113MB)
```python
from itertools import combinations

N, M = map(int, input().split())

nums = [i for i in range(1, N + 1)]
combination_list = combinations(nums, M)  # tuple(int) 반환

for i in combination_list:
    print(' '.join(map(str, i)))
```
- itertools 모듈로 구현된 조합 함수 (=combinations) 사용

