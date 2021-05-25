'''사용 모듈'''
import time
import os
import platform
import matplotlib.pyplot as plt
from PIL import Image


def clear():
    '''콘솔창 비워주는 함수'''
    os_type = platform.system()
    if os_type == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


clear()
while True:
    print("내가 만약 산타라면?")

    AA = 0
    BB = 0

    time.sleep(1)
    clear()
    print("선물 배달이 끝난 12월 26일!")
    print("1. 이불 밖은 위험해!")
    print("2. 나가서 놀자! 약속 잡아!")
    q1 = int(input("번호를 입력해주세요:"))

    if q1 == 1:
        AA += 1
    if q1 == 2:
        BB += 1

    clear()
    print("배달 도중 헷갈리는 길이 나왔다면?")
    print("1. 길은 역시 큰길")
    print("2. 지도를 찾아봐야지")
    q2 = int(input("번호를 입력해주세요:"))

    if q2 == 1:
        AA += 1
    if q2 == 2:
        BB += 1
    clear()
    print("아이들에게 줄 선물 어떻게 고를까?")
    print("1. 빅데이터 분석으로 선호도 파악")
    print("2. 선물은 느낌이지!")
    q3 = int(input("번호를 입력해주세요:"))

    if q3 == 1:
        AA += 1
    if q3 == 2:
        BB += 1

    clear()
    print("크리스마스 영화를 추천해달라고 하면")
    print("1. 넷플릭스 vs 왓챠 뭘 사용하는지 먼저 물어본다.")
    print("2. 영화 취향을 먼저 물어본다.")
    q4 = int(input("번호를 입력해주세요:"))

    if q4 == 1:
        AA += 1
    if q4 == 2:
        BB += 1
    clear()

    print("결과는")
    clear()
    script_dir = os.path.dirname(os.path.abspath(__file__))

    if AA > BB:
        print("카리스마 산타")
        image = Image.open(os.path.join(script_dir, 'a_1.png'))
        plt.imshow(image)
        plt.show()
        image = Image.open(os.path.join(script_dir, 'a_2.png'))
        plt.imshow(image)
        plt.show()

    elif BB > AA:
        print("천사 산타")
        image = Image.open(os.path.join(script_dir, 'b_1.png'))
        plt.imshow(image)
        plt.show()
        image = Image.open(os.path.join(script_dir, 'b_2.png'))
        plt.imshow(image)
        plt.show()

    else:
        print("감동쟁이 산타")
        image = Image.open(os.path.join(script_dir, 'c_1.png'))
        plt.imshow(image)
        plt.show()
        image = Image.open(os.path.join(script_dir, 'c_2.png'))
        plt.imshow(image)
        plt.show()


    n = int(input("1을 입력하면 설문이 끝납니다. 다시 시작하고싶다면 다른 숫자를 입력하세요."))

    if n == 1:
        break
