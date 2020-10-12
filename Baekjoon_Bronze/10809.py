# 알파벳 찾기
# 문제 : 알파벳 소문자로만 이루어진 단어 S가 주어진다. 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.
# 입력 : 첫째 줄에 단어 S가 주어진다. 단어의 길이는 100을 넘지 않으며, 알파벳 소문자로만 이루어져 있다.
# 출력 : 각각의 알파벳에 대해서, a가 처음 등장하는 위치, b가 처음 등장하는 위치, ... z가 처음 등장하는 위치를 공백으로 구분해서 출력한다.
#       만약, 어떤 알파벳이 단어에 포함되어 있지 않다면 -1을 출력한다. 단어의 첫 번째 글자는 0번째 위치이고, 두 번째 글자는 1번째 위치이다.

# version 1.
lower_text = input()
alphabet = list(map(chr,range(97,123)))
print(alphabet)
# alphabet을 아스키코드로 표현하기
text_index = []

for word in alphabet:
    if word in lower_text:
        whatstheindex = lower_text.index(word)
        text_index.append(str(whatstheindex))
    else:
        text_index.append(str(-1))
        
print(' '.join(text_index))


# version 2. simple version
alphabet2 = list(map(chr,range(ord('a'),ord('z'))))
print(alphabet2)
my_alphabet = list(map("baekjoon".find,map(chr,range(ord('a'),ord('z')))))
print(my_alphabet)


# version 3. askey code 사용해서 문제풀기
text = input()
# text = baekjoon
alphabet3 = [-1]*26

for i in range(len(text)):
    if alphabet3[ord(text[i]) - 97] != -1:
        #ord(text[i]) = text[i]번째의 askeycode
        #ex) text[3] = k / ord(k) = 107
        continue
    else:
        alphabet3[ord(text[i]) - 97] = i
        #107 - 97 = 10 >> 'k'의 아스키코드에서 'a'의 아스키코드를 뺄셈했기 때문에 10번째 알파벳 'k'를 가르킨다.
        #alphabet3의 10번째 자리 숫자를 text의 'k'인덱스 i로 변경

for i in range(26):
     print(alphabet3[i], end=' ')