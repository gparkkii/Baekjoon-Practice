


# n,m = map(int,input().split())

# word_list = []
# cnt = 0

# for i in range(n):
#     word = input().lower()
#     word_list.append(word)

# for j in range(m):
#     text = input().lower()
#     if text in word_list:
#         cnt += 1
#     else: pass

# print(cnt)

            
import sys
n,m = map(int,sys.stdin.readline().split())

word_list = []
cnt = 0

for i in range(n):
    word = input().lower()
    word_list.append(word)

for j in range(m):
    text = input().lower()
    if text in word_list:
        cnt += 1
    else: pass

print(cnt)



#####집합 자료형으로 풀기!!!