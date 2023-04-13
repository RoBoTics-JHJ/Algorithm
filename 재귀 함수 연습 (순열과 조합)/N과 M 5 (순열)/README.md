[문제보기](https://www.acmicpc.net/problem/15654)

시간 제한: 1초 (20,000,000 연산) <br/>
메모리 제한: 512MB <br/>
(1 ≤ M ≤ N ≤ 7)
## 백트레킹 (순열)
### 1번 풀이 (228ms, 117MB)
```python
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
```
<br/><br/><br/>
### 2번 풀이 (188ms, 115MB)
```python
from itertools import permutations

N, M = map(int, input().split())

nums = list(map(int, input().split()))
nums.sort()

for i in permutations(nums, M):
    print(' '.join(map(str, i)))
```

