import time # timestamp가 주어졌을 때, 날짜와 시간을 알아내기 위한 API를 제공 모듈 
import os # 운영체제에서 제공되는 여러 기능을 파이썬에서 수행할 수 있게 해주는 모듈 
import platform # 현재 사용하는 시스템 환경에 대한 부분 제공하는 모듈 
import matplotlib.pyplot as plt # pyplot모듈의 ㅡ각각의 함수를 사용해서 그래프를 만들고 변화를 줄 수 있음. 그래프 영역을 만들고, 몇개의 선을 표현



def clear(): # clear() : 콘솔 함수 사라지도록 하는 사용자 함수 생성
    os_type = platform.system()
    if os_type == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

while True:
    clear()
    print("설문을 시작합니다.")

    a = 0 # a 기본값
    b = 0 # b 기본값
    time.sleep(1) #time.sleep(n) : n초간 프로세스 중지
    clear()
    print("질문1")
    print("1.")
    print("2. ")
    q1 = int(input("번호를 입력해주세요:"))

    if q1 == 1: #1번 입력시 : a + 1
        a += 1
    if q1 == 2: #2번 입력시 : b + 1
        b += 1


    clear()
    print("질문2")
    print("1.")
    print("2.")
    q2 = int(input("번호를 입력해주세요:"))

    if q2 == 1:
        a += 1
    if q2 == 2:
        b += 1
    clear()
    print("질문3")
    print("1.")
    print("2.")
    q3 = int(input("번호를 입력해주세요:"))

    if q3 == 1:
        a += 1
    if q3 == 2:
        b += 1

    clear()
    print("질문4")
    print("1.")
    print("2.")
    q4 = int(input("번호를 입력해주세요:"))


    if q4 == 1:
        a += 1
    if q4 == 2:
        b += 1
    clear()

    print("결과는")
    time.sleep(1)

    clear()
    #script_dir = os.path.dirname(os.path.abspath(__file__)) # os.path.dirname : 경로 중 디렉토리 명만 얻기
        #os.path.abspath(__file__) : 특정 경로에 대해 절대 경로 얻기

    if a > b:
        print("ㄱ")

    elif b > a:
        print("ㄴ")
        
    else:
        print("ㄷ")


    i = input('설문을 나가려면 1을 입력하세요. ')
    if i == '1':
        break
    else:
        continue


print('설문 완료')
    