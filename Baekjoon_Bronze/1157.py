# 단어 공부
# 문제: 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.
# 입력: 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.
# 출력: 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.


text = list(input().lower())
set_text = list(set(text))
count_list = []

for i in set_text:
    count_text = text.count(i)
    count_list.append(count_text)


if count_list.count(max(count_list)) >= 2:
    print('?')
else:
    print(set_text[count_list.index(max(count_list))].upper())



#딕셔너리로 풀어보기
text2 = list(input().lower())
my_dict = {}

for i in text2:
    if i in my_dict:
        my_dict[i] += 1
    else:
        my_dict[i] = 1

cur_max = [0, 0]
on = False

for key, value in my_dict.items():
    if value > cur_max[1]:
        cur_max[0] = key
        cur_max[1] = value
        on = False
    elif value == cur_max[1]:
        on = True

if(on):
    print("?")
else:
    print(cur_max[0])
