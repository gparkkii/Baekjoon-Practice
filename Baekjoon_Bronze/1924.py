x,y = map(int,input().split())
week = ['SUN','MON','TUE','WED','THU','FRI','SAT']

def date(a,b):
    month = 0
    m_list = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    for i in range(a):
        month += m_list[i]
    return month + b

print(week[date(x,y)%7])
