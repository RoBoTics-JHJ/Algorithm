[문제보기](https://www.acmicpc.net/problem/15652)

시간 제한: 1초 (20,000,000 연산) <br/>
메모리 제한: 512MB <br/>
(1 ≤ M ≤ N ≤ 7)
## 백트레킹 (중복 조합)
### 1번 풀이 (152ms, 115MB)
```python
N, M = map(int, input().split())

tmp_stack = []


def func():
    # 백트래킹 가지치기(pruning)
    if len(tmp_stack) == M:
        print(' '.join(map(str, tmp_stack)))
        return

    for i in range(0, N):
        if len(tmp_stack) == 0 or tmp_stack[-1] <= (i + 1):
            tmp_stack.append(i + 1)

            func()

            tmp_stack.pop()


func()
```
- 핵심코드: **"if len(tmp_stack) == 0 or tmp_stack[-1] <= (i + 1):"**
<br/><br/><br/>
### 2번 풀이 (180ms, 115MB)
```python
from itertools import combinations_with_replacement

N, M = map(int, input().split())

nums = [i for i in range(1, N + 1)]
combinations_with_replacement_list = combinations_with_replacement(nums, M)

for i in combinations_with_replacement_list:
    print(' '.join(map(str, i)))
```
- itertools 모듈로 구현된 중복 조합 함수 ( = combinations_with_replacement) 사용

