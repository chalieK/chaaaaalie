# class Unit:
#     def __init__(self):
#         print("Unit 생성자")

# class Flyable:
#     def __init__(self):
#         print("Flyable 생성자")

# class FlyableUnit(Unit, Flyable):
#     def __init__(self):
#         # super().__init__() 
#         Unit.__init__(self)
#         Flyable.__init__(self) # 다중상속의 경우 이 방식으로 해야함.
    
# # 드랍쉽 : 수송기 

# dropship = FlyableUnit()

# super를 쓸 경우, 다중상속에서 문제가 생김. 맨처음 상속받는 클래스만 __init__ 함수가 상속 된다.

# Quiz) 주어진 코드를 활용 , 부동산 프로그램 작성

'''(출력 예제)
총 3대의 매물
강남 아파트 매매 10억 2010년
마포 오피스텔 전세 5억 2007년
송파 빌라 월세 500/50 2000년

[코드]
class House:
    # 매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        pass
    
    # 매물 정보 표시
    def show_detail(self):
        pass
      '''
# 내가 쓴 답

# class House:
#     # 매물 초기화
#     def __init__(self, location, house_type, deal_type, price, completion_year):
#         self.location = location
#         self.house_type = house_type
#         self.deal_type = deal_type
#         self.price = price
#         self.completion_year = completion_year
#         # print("아파트가 등록되었습니다.")
#     # 매물 정보 표시
#     def show_detail(self):
#         for House in house_list:
#             print("{0} {1} {2} {3} {4}".format(self.location, self.house_type, self.deal_type, self.price, self.completion_year))
#             return

# class A(House):
#     def __init__(self):
#         House.__init__(self, "강남", "아파트", "매매", "10억", "2010년")
       
# class B(House):
#     def __init__(self):
#         House.__init__(self, "마포", "오피스텔", "전세", "5억", "2007년")
       
# class C(House):
#     def __init__(self):
#         House.__init__(self, "송파", "빌라", "월세", "500/50", "2010년")
      

# A1 = A()
# A2 = B()
# A3 = C()

# house_list = []
# house_list.append(A1)
# house_list.append(A2)
# house_list.append(A3)

# for House in house_list:
#     House.show_detail()

# 정답 : 훨씬 간소화 되어있다. for 문이나, class등 번거로운 작업이 적다. 
# 또한 총 3대의 매물이 있습니다. 구문에서 len를 통해 house리스트에 들어있는 각 수를 구하는 방법이 눈에띄었다.

# class House:
#     # 매물 초기화
#     def __init__(self, location, house_type, deal_type, price, completion_year):
#         self.location = location
#         self.house_type = house_type
#         self.deal_type = deal_type
#         self.price = price
#         self.completion_year = completion_year
        
#     # 매물 정보 표시
#     def show_detail(self):
#         print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)

# houses = []
# houses1 = House("강남", "아파트", "매매", "10억", "2010년")
# houses2 = House("마포", "오피스텔", "전세", "5억", "2007년")
# houses3 = House("송파", "빌라", "월세", "500/50", "2010년")

# houses.append(houses1)
# houses.append(houses2)
# houses.append(houses3)

# print("총 {0}대의 매물이 있습니다.".format(len(houses)))
# for House in houses:
#     House.show_detail()

# 예외처리 에러가 생긴걸 예외로 처리하는것

# try:
#     # print("나누기 전용 계산기 입니다.")
#     # num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     # num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     # print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2))
#     print("나누기 전용 계산기 입니다.")
#     nums = []
#     nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
#     nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
#     # nums.append(int(nums[0] / nums[1]))
#     print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
# except ValueError:
#     print("에러! 잘못된 값을 입력하였습니다.")
# except ZeroDivisionError as err:
#     print(err)
# # except:
# #     print("알 수 없는 에러가 발생하였습니다.")
# except Exception as err:
#     print("알 수 없는 에러가 발생하였습니다.")
#     print(err)

# try:
#     print("한 자리 숫자 나누기 전용 계산기 입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >=10: # 의도적으로 필요한 에러를 발생시켜 except 구문을 불러올수 있다.
#         raise ValueError
#     print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")

# 사용자 정의 예외처리
# class BigNumberError(Exception): # 클래스에서 exception함수 상속
#     pass
# class BigNumberError(Exception):
#     def __init__(self, msg):
#         self.msg = msg

#     def __str__(self):
#         return self.msg

# try:
#     print("한 자리 숫자 나누기 전용 계산기 입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >=10: # 의도적으로 필요한 에러를 발생시켜 except 구문을 불러올수 있다.
#         raise BigNumberError("입력값 : {0}, {1}".format(num1, num2)) # raise ValureError를 사용하여 지정된 에러를 출력할 수 있다.
    
#     print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
# except ValueError: # 파이썬 내에 지정된 에러
#     print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
# except BigNumberError as err: # 사용자가 따로 정의한 에러
#     print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요")
#     print(err)
# finally:
#     print("계산기를 이용해 주셔서 감사합니다.")
# finally 예외처리 구문 내 정상/오류 상관 없이 출력

# Quiz 치킨집, 자동주문 시스템. 시스템 코드를 보고 예외처리 구문 넣기
'''
조건1 : 1보다 작거나 숫자가 아닌 입력값이 들어올 때는 ValueError로 처리
        출력 메세지 : "잘못된 값을 입력하였습니다."
조건2 : 대기 손님이 주문할 수 있는 총 치킨량은 10마리로 한정
        치킨 소신 시 사용자 정의 에러[SoldOutError]를 발생시키고 프로그램 종료
        출력 메세지 : "재고가 소진되어 더 이상 주문을 받지 않습니다."
'''
# 내가 쓴 답

# class SoldOutError(Exception):
#     def __init__(self, msg):
#         self.msg = msg

#     def __str__(self):
#         return self.msg

# try:
#     chicken = 20 
#     waiting = 1 # 홀은 현재 만석, 대기번호 1부터 시작
#     while(True):
#         print("[남은 치킨 : {0}]".format(chicken))
#         order = int(input("치킨 몇 마리 주문하시겠습니까?"))
#         if order > chicken and chicken > 0: # 남은 치킨보다 주문량이 많을 떄
#            print("재료가 부족합니다.")
#         elif chicken == 0: # 남은 치킨이 없을 때       
#             raise SoldOutError("재료가 소진되었습니다.")
#         elif order > 10:
#             print("10마리 이상은 시킬 수 없습니다.")
#         else:
#             print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다.".\
#                 format(waiting, order))
#             waiting += 1
#             chicken -= order
# except ValueError:
#     print("잘못된 값을 입력하였습니다.")
# except SoldOutError as err:
#     print("재고가 소진되어 더 이상 주문을 받지 않습니다.")

# 정답 탈출구문을 생각하지 못했었다. 또한 class에 대한 이해도가 떨어져 어떨 때 pass를 쓰는지를 알지 못한다.
# 그리고, 사용자 정의한 에러구문 뒤에 ()를 붙여 사용하는지도 모르겠다.

# class SoldOutError(Exception):
#     pass

# chicken = 10 
# waiting = 1 # 홀은 현재 만석, 대기번호 1부터 시작
# while(True):
#     try:
#     print("[남은 치킨 : {0}]".format(chicken))
#         order = int(input("치킨 몇 마리 주문하시겠습니까?"))
#         if order > chicken and chicken > 0: # 남은 치킨보다 주문량이 많을 떄
#             print("재료가 부족합니다.")
#         else:
#             print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다.".\
#                 format(waiting, order))
#             waiting += 1
#             chicken -= order
        
#         if chicken == 0:
#             raise SoldOutError

#     except ValueError:
#         print("잘못된 값을 입력하였습니다.")
#     except SoldOutError as err:
#         print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
#         break

# 모듈 파일을 따로 만들어서 사용.

# 잔돈을 안바꿔주는 극장 예제
# import theater_module
# theater_module.price(3) # 3명이서 영화 보러 왔을 때 가격
# theater_module.price_morning(4) # 4명 조조할인
# theater_module.price_soldier(5) # 5명 군인

# import theater_module as mv # as 뒤에 별명 지정
# mv.price(3) 
# mv.price_morning(4)
# mv.price_soldier(5)

# from theater_module import * # 함수로 다 쓸수있음
# # from random import *
# price(3)
# price_morning(4)
# price_soldier(5)

# from theater_module import price, price_morning # 필요한 함수만 씀
# price(3)
# price_morning(4)
# # price_soldier(5)

# from theater_module import price_soldier as price # 별명 지정.(군인 할인의 결과값)
# price(4)

# 패키지 모듈을 모아놓은 집합
# 신규 여행사 프로젝트(태국-베트남 패키지 상품)
# travel 폴더에서 하위 파일 만들어 진행

# import Travel.thailand # import 형태에서는 3번째 부분엔 모듈만 가능. 클래스 불가능.
# trip_to = Travel.thailand.ThailandPackage()
# trip_to.detail()

# 반면 from import 구문에서는 클래스 가능
# from Travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

# from Travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# __all__ #__init 폴더에 
# from Travel import * # 개발자가 이렇게 쓰면 공개범위 설정 따로 해야함(랜덤모듈과는 달리)
# trip_to = thailand.ThailandPackage()
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# 모듈 직접 실행

# 모듈, 패키지 위치 다른 프로젝트에서 똑같이 사용가능

# import inspect
# import random
# print(inspect.getfile(random))
# print(inspect.getfile(thailand))

# pypi 패키지 설치 pypi사이트에서 browser project -> topic 선택하여 필요한것 설치
# 패키지 코드를 복사하면 터미널에서 실행

#beautiful soup 설치 후 삭제 완료
# from bs4 import BeautifulSoup
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())

# 내장함수
# input
# language = input("무슨 언어를 좋아하세요?")
# print("{0}은 아주 좋은 언어입니다!".format(language))

#dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 갖고 있는지 표시
# print(dir())
# import random # 외장 함수
# print(dir())
# import pickle # 외장 함수
# print(dir())

# print(dir(random))

# lst = [1, 2, 3]
# print(dir(lst))

# name = "Jim"
# print(dir(name))

# 내장 함수 -> google 에서 list of python builtins

# 외장 함수 -> list of python modules

# glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우의 dir)
# import glob
# print(glob.glob("*.py")) # 확장자가 py인 모든 파일

# os : 운영체제에서 제공하는 기본 기능
# import os
# print(os.getcwd()) # 현재 디렉토리

# folder = "sample_dir"

# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder)
#     print(folder, "폴더를 삭제하였습니다.")
# else:
#     os.makedirs(folder) # 폴더 생성
#     print(folder, "폴더를 생성하였습니다.")

# print(os.listdir()) # glob과 비슷

# time : 시간 관련 함수
# import time
# print(time.localtime())
# print(time.strftime("%Y-%M-%d %H:%M:%S"))

# import datetime
# # print("오늘 날짜는 ", datetime.date.today())
# # timedelta : 두 날짜 사이의 간격
# today = datetime.date.today() # 오늘 날짜 저장
# td = datetime.timedelta(days=100) # 100일 저장
# print("우리가 만난지 100일은", today + td) # 오늘부터 100일 후

# Quiz 프로젝트 내에 나만의 시그니처를 남기는 모듈을 만드시오
''' 조건 : 모듈 파일명은 byme.py로 작성
(모듈 사용 예제)
import byme
byme.sign()

(출력 예제)
이 프로그램은 나도코딩에 의해 만들어졌습니다.
유튜브 : http://youtube.com
이메일 : nadocoding@gmail.com'''

# import byme
# byme.sign()