# 10872. 팩토리얼 구하기
# 문제 : 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.
# 입력 : 첫째 줄에 정수 N(0 ≤ N ≤ 12)가 주어진다.
# 출력 : 첫째 줄에 N!을 출력한다.


#version 01. for문 이용하기

# n = int(input())

# def factorial(n):
#     nums = 1
#     for i in range(1,n+1):
#         nums = nums * i
#     return nums

# print(factorial(n))



#version 02. 재귀함수 이용하기

a = int(input()) 

def func(a):
    if a == 0: #0일 때 오류가 나지 않게 0!도 설정해주기
        return 1
    elif(a != 1): 
        return a * func(a-1) 
        # func(a-1)이 함수를 다시 호출하는 역할. 그래서 다시 func(a)로 돌아간다.
        # ex) a가 5부터 시작하면 return 5 * func(5-1)이 되기 때문에 다시 func(4) 함수를 시작.
        # 출력되지 못한 함수는 출력되기 전까지 쌓였다가 한꺼번에 출력된다. >> 5*4*3*2*1
    else:
        return 1

print(func(a))