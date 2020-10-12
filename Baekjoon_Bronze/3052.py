# 두 자연수 A와 B가 있을 때, A%B는 A를 B로 나눈 나머지 이다. 예를 들어, 7, 14, 27, 38을 3으로 나눈 나머지는 1, 2, 0, 2이다.
# 수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.

# 입력: 첫째 줄부터 열번째 줄 까지 숫자가 한 줄에 하나씩 주어진다. 이 숫자는 1,000보다 작거나 같고, 음이 아닌 정수이다.
# 출력: 첫째 줄에, 42로 나누었을 때, 서로 다른 나머지가 몇 개 있는지 출력한다.

#version1
arr = []
for i in range(10):
    nums = int(input())
    arr.append(nums % 42)

arr = set(arr)
#set기능을 이용하는 문제!
#1. set()은 중복을 허용하지 않는다.
#2. set()은 순서가 없고 반환값이 {}로 출력된다. 그렇기때문에 index값을 얻을 수 없다.
#3. index값을 얻기 위해선 리스트나 튜플 자료형으로 변환해야한다.
print(len(arr))


#version2

import sys
B=[]
for i in range(10):
    A=int(sys.stdin.readline())
    if A%42 in B:
        continue
    else:
        B.append(A%42)
print(len(B))
