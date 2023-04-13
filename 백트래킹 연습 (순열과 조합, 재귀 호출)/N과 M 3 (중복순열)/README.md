[문제보기](https://www.acmicpc.net/problem/15651)

시간 제한: 1초 (20,000,000 연산) <br/>
메모리 제한: 512MB <br/>
(1 ≤ M ≤ N ≤ 7)
## 백트레킹 (중복 순열)
### 1번 풀이 (680ms, 124MB)
```python
N, M = map(int, input().split())

tmp_stack = []


def func():
    # 백트래킹 가지치기(pruning)
    if len(tmp_stack) == M:
        print(' '.join(map(str, tmp_stack)))
        return

    for i in range(0, N):
        tmp_stack.append(i+1)

        func()

        tmp_stack.pop()


func()
```
- 중복을 허용하기 때문에 check_list를 if문과 함께 확인할 필요가 없음
- tmp_stack 길이가 M 인 모든 경우를 출력하게 됨
<br/><br/><br/>
### 2번 풀이 (596ms, 120MB)
```python
from itertools import product

N, M = map(int, input().split())

nums = [i for i in range(1, N + 1)]
product_list = product(nums, repeat=M)

for i in product_list:
    print(' '.join(map(str, i)))
```
- itertools 모듈로 구현된 중복 순열 함수 ( = product) 사용

