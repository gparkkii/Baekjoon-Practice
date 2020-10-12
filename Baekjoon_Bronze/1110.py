
#num = int(input()) ##26

#num1 = num//10 + num%10 ##2+6 
#num//10 >> num의 10의 자릿수를 구할 수 있다
#num%10 >> num의 1의 자릿수

#num2 = (num%10)*10 + num1%10 ##6+8
#(num%10)*10 >> num1의 1의 자릿수를 10의 자릿수로 변경
#num1%10 >> num의 10의 자릿수와 1의 자릿수의 합이된 num1의 1의 자릿수 구하기 

num = int(input())
real_num = num
cycle = 0

while True: 
    cycle += 1
    a = num//10
    b = num%10
    sum1 = a + b
    sum2 = (b*10) + sum1%10
    num = sum2
    if sum2 == real_num:
        break
print(cycle)
