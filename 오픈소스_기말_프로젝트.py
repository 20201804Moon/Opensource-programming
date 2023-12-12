#<오픈소스프로그래밍 기말 프로젝트>
#
# ● 아래의 코드를 수정 혹은 프로그래밍하여 문제를 해결하시오.
# ● 문제의 점수는 각각 표시되며, 부분점수가 존재합니다.
#
# 학번 : 20201804 이름 : 문정혜

import os
import time

# Q.1 10점
#
# 문자열 my_string과 target이 매개변수로 주어질 때,
# target이 문자열 my_string의 부분 문자열이라면 1을,
# 아니라면 0을 return 하는 solution 함수를 작성하시오.
#
# 제한사항
# 1 ≤ my_string 의 길이 ≤ 100
# my_string 은 영소문자로만 이루어져 있습니다.
# 1 ≤ target 의 길이 ≤ 100
# target 은 영소문자로만 이루어져 있습니다.

def solution(my_string, target):
    answer= 0

    if target in my_string:     #if와 in을 사용해서 target이 my_string안에 있는지 확인하고 있다면 answer = 1로
        answer = 1
    else:                       # target이 my_string안에 없으면 answer = 0으로 바꾼다.
        answer = 0

    return answer               # answer 값 리턴

my_string = input("문장을 입력하세요 (단, 1 ≤ my_string의 길이 ≤ 100이고 영소문자로만 이루어져야 합니다.): ") #사용자로부터 입력받기
target = input("문장을 입력하세요 (단, 1 ≤ target의 길이 ≤ 100이고 영소문자로만 이루어져야 합니다.): ")

print(solution(my_string, target))       # 함수 호출하고 리턴 받은 값 출력


# Q.2 10점
#
# 모스부호 해독 프로그램 만들기
# 문자열 letter 가 매개변수로 주어질 때,
# letter 영어 소문자로 바꾼 문자열을 return 하는
# solution 함수를 완성하시오.
#
# 제한사항
# 1 ≤ letter 의 길이 ≤ 1,000
# letter 의 모스부호는 공백으로 나누어져 있습니다.
# letter 에 공백은 연속으로 두 개 이상 존재하지 않습니다.
#
# letter = 여러분의 좌우명 또는 인상 깊었던 말을 쓰시오.

def solution(letter):
    morse = {                                                  # morse 딕셔너리 생성
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'}
    answer = ''           #answer는 아무 것도 없는 문자열

    a = letter.split()    #공백을 기준으로 문자열을 나눔
    
    for x in a:
        answer = answer + morse[x]
        
    return answer   

letter = input("좌우명 또는 인상 깊었던 말을 쓰시오(단, 1 ≤ letter 의 길이 ≤ 1,000, 공백 연속으로 X): ")
c= solution(letter)
print(c)


# Q.3 10점
#
# 행성의 나이를 알파벳으로 표현할 때,
# a는 0, b는 1, ..., j는 9
# 예를 들어 cd는 23살, fb는 51살입니다.
# age가 매개변수로 주어질 때
# PROGEAMMER-857식 나이를 return 하도록
# solution 함수를 완성하시오.
#
# 제한사항
# age는 자연수입니다.
# age ≤ 1,000
# PROGRAMMERS-857 행성은 알파벳 소문자만 사용합니다.

def solution(age):
    answer = ''
    transform = {'0':'a', '1':'b', '2':'c', '3':'d', '4':'e', '5':'f', '6':'g', '7':'h', '8':'i', '9':'j' } # transform 딕셔너리 생성

    for x in age:
        answer = answer + transform[x]
    
    return answer

age = input("PROGEAMMER-857식 나이를 쓰시오(단,  age≤ 1,000): ")
print(solution(age))


# Q.4 10점
#
# x축과 y축으로 이루어진 2차원 직교 좌표계에 중심이 원점인
# 서로 다른 크기의 원이 두 개 주어집니다.
# 반지름을 나타내는 두 정수 r1, r2가 매개변수로 주어질 때,
# 두 원 사이의 공간에 x좌표와 y좌표가 모두 정수인 점의 개수를
# return하도록 solution 함수를 완성해주세요.
# ※ 각 원 위의 점도 포함하여 셉니다.
#
# 제한사항
# 1 ≤ r1 < r2 ≤ 1,000,000

def solution(r1, r2):
    answer = 0
    y1 = 0
    y2 = 0
    for i in range(0, r1 + 1):     #작은 원 반지름 까지
        y1 = y1 + (int((r2**2-i**2)**(1/2))-int((r1**2-i**2)**(1/2)))  #원의 방정식 사용
    for i in range(r1, r2 + 1):    #작은 원 반지름부터 큰 원 반지름까지
        y2 = y2 + (int((r2**2-i**2)**(1/2)))

    answer = (y1 + y2) * 4         # 총 4사분면이 있으니 4를 곱해 전체 원의 값을 구함
    return answer

r1, r2 = input("r1, r2을 입력하시오. 단(1 ≤ r1 < r2 ≤ 1,000,000): ").split() #공백을 기준으로 나눔
print(solution(int(r1), int(r2)))  # 문자열이 아닌 정수로 받기


# Q.5 10점
#
# 0 또는 양의 정수가 주어졌을 때,
# 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
#
# 예를 들어, 주어진 정수가 [6, 10, 2]라면
# [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고,
# 이중 가장 큰 수는 6210입니다.
#
# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때,
# 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어
# return 하도록 solution 함수를 작성해주세요.
#
# 제한사항
# numbers의 길이는 1 이상 100,000 이하입니다.
# numbers의 원소는 0 이상 1,000 이하입니다.
# 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.
#
# numbers = [8, 30, 17, 2, 23]
 

def solution(numbers):
    answer = ''
    a = map(str, numbers) #입력받은 numbers의 각 요소에 str을 적용
    numbers = list(a)   #리스트로 만들어 numbers에 삽입

    
    def compare(nums):
        return str(nums) * 8  # 8자리 문자열 반복
    
    numbers.sort(key=compare, reverse=True) 
    #내림차순 정렬
 
    answer = ''.join(numbers)   # 문자열 합치기
        
    return answer


numbers = [8, 30, 17, 2, 23]
print(solution(numbers))
 



















