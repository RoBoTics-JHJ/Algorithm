[문제보기](https://www.acmicpc.net/problem/15655)

시간 제한: 1초 (20,000,000 연산) <br/>
메모리 제한: 512MB <br/>
(1 ≤ M ≤ N ≤ 8)
## 백트레킹 (조합)
### 1번 풀이 (116ms, 113MB)
```python
N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

tmp_stack = []


def func(start):
    if len(tmp_stack) == M:
        print(' '.join(map(str, tmp_stack)))
        return

    for i in range(start, N):
        if nums[i] not in tmp_stack:
            tmp_stack.append(nums[i])

            func(i + 1)

            tmp_stack.pop()


func(0)
```
<br/><br/><br/>
### 2번 풀이 (128ms, 113MB)
```python
from itertools import combinations

N, M = map(int, input().split())

nums = list(map(int, input().split()))
nums.sort()

for i in combinations(nums, M):
    print(' '.join(map(str, i)))
```

