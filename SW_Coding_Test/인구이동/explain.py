N, L, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]


# (a, b) 나라 기준으로 연합이 가능한 나라를 BFS로 탐색
def bfs(a, b):
    # tmp: 연합할 수 있는 나라 모음
    tmp = []
    tmp.append((a, b))
    # que: BFS에 사용될 큐
    que = []
    que.append((a, b))
    while que:
        x, y = que.pop(0)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 땅 밖으로 나가지 않고 탐색전이며 인구수의 조건도 맞는 경우
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 and L <= abs(A[nx][ny] - A[x][y]) <= R:
                    visited[nx][ny] = 1
                    tmp.append((nx, ny))
                    que.append((nx, ny))
    return tmp


anw = 0
while True:
    visited = [[0] * (N + 1) for _ in range(N + 1)]
    # move가 1일 경우, 연합 지역 인구수 계산함.
    move = 0
    for i in range(N):
        for j in range(N):
            # 탐색하지 않은 곳을 기준으로(단순 for문과 if문으로 찾음)
            # 연합 지역을 찾은 뒤에(bfs)
            # 연합 지역 인구수 계산 (문제 조건에 맞게 계산 후, A 업데이트)
            # * 연합이 여러개일 경우까지 고려됨
            if visited[i][j] == 0:
                visited[i][j] = 1

                country = bfs(i, j)

                if len(country) > 1:
                    move = 1
                    num = sum([A[a][b] for a, b in country]) // len(country)
                    for a, b in country:
                        A[a][b] = num

    # 더 이상 이동할 조건이 아닌 경우, while문 종료
    if move == 0:
        break

    # 연합 지역끼리 인구 이동을 완료하면 anw + 1
    anw += 1


print(anw)
