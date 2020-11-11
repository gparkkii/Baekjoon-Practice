# (column : 열  row : 행)   , 열은 세로줄, 행은 가로줄
# 2차원 배열 만드는 법 (1): array = [[0 for col in range(11)] for row in range(10)]
# 2차원 배열 만드는 법 (2): array = [[0]*11]*10
# 2차원 배열 인덱스 찾는 법 :   array[row][col]
# 2차원 배열 인덱스에 값 입력 : array[row][col] = '값'

test = int(input())

dx = (0,0,1,-1)
dy = (1,-1,0,0)





for testCase in range(test):
    r, c, n = map(int,input().split())
    cnt = 0
    Map = [[0]*r for _ in range(c)]
    visit = [[False]*r for _ in range(c)]
    for test in range(n):
        location = list(map(int,input().split()))
        Map[location[1]][location[0]] = 1

    def dfs(x,y):
        visit[y][x]=True
        for i in range(4):
            next_x = x+dx[i]
            next_y = y+dy[i]
            if 0 <= next_x < r and 0<= next_y < c  and Map[next_y][next_x] == 1 and (visit[next_y][next_x] == False):
                dfs(next_x,next_y)
    for y1 in range(c):
        for x1 in range(r):
            if(visit[y1][x1]==False and Map[y1][x1]==1):
                cnt+=1
                dfs(x1,y1)
    print(cnt)