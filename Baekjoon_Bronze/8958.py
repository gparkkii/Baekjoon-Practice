# 8958번 OX퀴즈
# 문제 : "OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다. O는 문제를 맞은 것이고, X는 문제를 틀린 것이다. 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다. 예를 들어, 10번 문제의 점수는 3이 된다.
#       "OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.
#        OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.
# 입력 : 첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 길이가 0보다 크고 80보다 작은 문자열이 주어진다. 문자열은 O와 X만으로 이루어져 있다.
# 출력 : 각 테스트 케이스마다 점수를 출력한다.

#version 01
test_case = int(input())
test = [input() for i in range(test_case)] #['OOXXOXXOOO', 'OOXXOOXXOO', 'OXOXOXOXOXOXOX', 'OOOOOOOOOO', 'OOOOXOOOOXOOOOX']
for i in range(len(test)):
    test_num = test[i]
    test_cnt = 0
    test_sum = 0
    for j in range(len(test_num)):
        if test_num[j] == 'O':
            test_cnt += 1
            test_sum += test_cnt
        else:
            test_cnt = 0
    print(test_sum)

#version 02
test_case2 = int(input())
test2 = [input() for i in range(test_case2)] #['OOXXOXXOOO', 'OOXXOOXXOO', 'OXOXOXOXOXOXOX', 'OOOOOOOOOO', 'OOOOXOOOOXOOOOX']
test_sum2 = 0
for i in range(len(test2)):
    test_num2 = test2[i]
    test_num2 = test_num2.split('X')
    for j in range(len(test_num2)):
        test_cnt2 = test_num2[j].count('O')
        test_sum2 += int((test_cnt2 * (test_cnt2 + 1))/2)
    print(test_sum2)
    test_sum2 = 0



    
    