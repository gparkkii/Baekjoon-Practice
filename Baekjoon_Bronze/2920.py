#음계


nums = list(map(int,input().split()))
ascending = [1, 2, 3, 4, 5, 6, 7, 8]
descending = [8, 7, 6, 5, 4, 3, 2, 1]

if nums == ascending:
    print("ascending")
elif nums == descending:
    print("descending")
else:
    print("mixed")



#강사 풀이
a = list(map(int, input().split(" ")))

ascending = True
descending = True

for i in range(1,8):
    if a[i] > a[i-1]:
        descending = False
    elif a[i] < a[i-1]:
        ascending = False

if ascending:
    print("ascending")
elif descending:
    print("descending")
else:
    print("mixed")