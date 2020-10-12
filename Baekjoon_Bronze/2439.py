#첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
#하지만, 오른쪽을 기준으로 정렬한 별(예제 참고)을 출력하시오.

star = int(input())

for i in range(1,star+1):
    space = star - i
    print(' ' * space + '*' * i)


# 오답 : print(' '*space,'*'*i)
#',' 를 넣으면 자동공백이 생기기 때문에 문자열을 이어줄 수 있는 +로 사용하기