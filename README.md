<h3>MBTI<h3>
MBTI 기본 코드 이용해 나만의 MBTI 만들기 <br>

기본 뼈대<br>

``` <br>
import time <br>
import os  <br>
import platform <br>
import matplotlib.pyplot as plt <br>
<br>
def clear():  <br>
    os_type = platform.system() <br>
    if os_type == 'Windows': <br>
        os.system('cls') <br>
    else: <br>
        os.system('clear') <br>
 <br>
i = print('검사에서 나가려면 1을 눌러주세요: ', input()) <br>
 <br>
clear()  <br>
print("무료 성격 유형 검사 입니다.") <br>
a = 0 # a 기본값 <br>
b = 0 # b 기본값 <br>
<br>
time.sleep(1)  <br>
<br>
clear() <br>
print("1번 문항")  <br>
print("1.을 입력") <br>
print("2.을 입력") <br>
q1 = int(input("번호를 입력해주세요:"))  <br>
<br>
if q1 == 1: #입력값 1 : a+1 <br>
    a += 1 <br>
if q1 == 2: #입력값 2 : b+1 <br>
    b += 1 <br>
else: <br>
    print('다시 입력해주세요') <br>
<br>
clear() <br>
print("2번 문항?") <br>
print("1.을 입력") <br>
print("2.을 입력") <br>
q2 = int(input("번호를 입력해주세요:")) <br>
 <br>
if q2 == 1: #입력값 1 : a+1 <br>
    a += 1 <br>
if q2 == 2: #입력값 2 : b+1 <br>
    b += 1 <br>
clear() <br>
print("3번 문항?") <br>
print("1.을 입력") <br>
print("2.을 입력") <br>
q3 = int(input("번호를 입력해주세요:")) <br>
 <br>
if q3 == 1: #입력값 1 : a+1 <br>
    a += 1 <br>
if q3 == 2: #입력값 2 : b+1 <br>
    b += 1 <br>
 <br>
clear() <br>
print("4번 문항?") <br>
print("1.을 입력") <br>
print("2.을 입력") <br>
q4 = int(input("번호를 입력해주세요:")) <br>

 <br>
if q4 == 1: <br>
    a += 1 <br>
if q4 == 2: <br>
    b += 1 <br>
clear() <br>

 <br>
print("결과는") <br>
clear() <br>
script_dir = os.path.dirname(os.path.abspath(__file__)) <br>

 <br>
if a > b: <br>
    print("q결과") <br>
    <br>
elif b > a: <br>
    print("w결과") <br>
    
else: <br>
    print("ㄷ결과") <br>
```
  
  <hr>
  
  <strong>while 문을 이용해서 검사 후 다시 처음부터 검사 할 수 있도록 기능 추가</strong>
  >while 문과 if문을 넣어서 기능 구현 <br>
 
``` <br>
  def clear(): <br>
    os_type = platform.system() <br>
    if os_type == 'Windows': <br>
        os.system('cls') <br>
    else: <br>
        os.system('clear') <br>
 <br>
while True: <br>
    clear() <br>
    print("설문을 시작합니다.") <br>
 <br>
    a = 0 # a 기본값 <br>
    b = 0 # b 기본값 <br>
    clear() <br>
    print("질문1") <br>
    print("1.") <br>
    print("2. ") <br>
    q1 = int(input("번호를 입력해주세요:")) <br>
 <br>
    if q1 == 1: #1번 입력시 : a + 1 <br>
        a += 1 <br>
    if q1 == 2: #2번 입력시 : b + 1 <br>
        b += 1 <br>
 <br>
    clear() <br>
    print("질문2") <br>
    print("1.") <br>
    print("2.") <br>
    q2 = int(input("번호를 입력해주세요:")) <br>
 <br>
    if q2 == 1: <br>
        a += 1 <br>
    if q2 == 2: <br>
        b += 1 <br>
   <br>  
  clear() <br>
    print("질문3") <br>
    print("1.") <br>
    print("2.") <br>
    q3 = int(input("번호를 입력해주세요:")) <br>
    if q3 == 1: <br>
        a += 1 <br>
    if q3 == 2: <br>
        b += 1 <br>
 <br>
    clear() <br>
    print("질문4") <br>
    print("1.") <br> 
    print("2.") <br>
    q4 = int(input("번호를 입력해주세요:")) <br>
 <br>
    if q4 == 1: <br>
        a += 1 <br>
    if q4 == 2: <br>
        b += 1 <br>
    clear() <br>
    print("결과는") <br>
 <br>
    clear() <br>
    if a > b: <br>
        print("ㄱ") <br>
    elif b > a: <br>
        print("ㄴ") <br>
    else: <br>
        print("ㄷ") <br>
 <br>
    i = input('설문을 나가려면 1을 입력하세요. ') <br>
    if i == '1': <br>
        break <br>
    else: <br>
        continue <br>
   <br>
print('설문 완료') <br>
```
  
  
 
