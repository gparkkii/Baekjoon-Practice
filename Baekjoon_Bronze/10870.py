# 문제. 10870 피보나치의 수
# 피보나치 수는 0과 1로 시작한다. 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다. 그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합이 된다.

# 입력 : 첫째 줄에 n이 주어진다. n은 20보다 작거나 같은 자연수 또는 0이다.
# 출력 : 첫째 줄에 n번째 피보나치 수를 출력한다.

# 숏코딩

# n = int(input())
# fibo = [0,1]
# for i in range(n):
#     sums = fibo[i] + fibo[i+1]
#     fibo.append(sums)
# print(fibo[n])


# 일반함수
# def fibo(n):
#     a = 0
#     b = 1
#     cnt = 1
#     if n > 1:
#         while n != cnt:
#             sums = a + b
#             a = b
#             b = sums
#             cnt += 1
#     else:
#         sums = n
#     return sums

# n = int(input())
# print(fibo(n))



#재귀함수
def fibo(n):
    if n<=0:
        return 0
    if(n==1):
        return 1
    return fibo(n-1)+fibo(n-2) 

print(fibo(3))

