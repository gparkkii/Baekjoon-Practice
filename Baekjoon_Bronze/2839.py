n = int(input())

for i in range(0,int(n/3)+1):
    if (n - 3*i)%5 == 0:
        print(int((n - 3*i)/5+i))
        exit() #not only exit for() but also quit all lines

print(-1)
