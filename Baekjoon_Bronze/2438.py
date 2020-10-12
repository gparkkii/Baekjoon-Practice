#첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

star = int(input())

for i in range(1,star+1):
    print('*'*i)