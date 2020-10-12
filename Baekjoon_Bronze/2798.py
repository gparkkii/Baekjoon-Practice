a, b = map(int,input().split())
nums = list(map(int,input().split()))
sums = 0

for i in range(0,a):
    c = nums[i]
    for j in range(i+1,a):
        d = nums[j]
        for k in range(j+1,a):
            e = nums[k]
            add = c + d + e
            if add <= b and add > sums:
                sums = add
print(sums)    
