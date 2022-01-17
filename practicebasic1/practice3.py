#표준입출력
# sep 쉼표 등 추가 , end 뒷 부분을 연달아 출력
# import sys
# print("Python", "Java", file=sys.stdout) 
# print("Python", "Java", file=sys.stderr)

#시험성적
# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items():
#     # print(subject, score)
#     print(subject.ljust(8), str(score).rjust(4), sep=":") # ljust() 왼쪽 정렬, rjust() 오른쪽정렬(공간확보)

# 은행 대기순번표
# 001, 002, 003, ...
# for num in range(1,21):
#     print("대기번호 :" + str(num).zfill(3)) # zfill() ()의 크기만큼 공간확보하고 0을 채운다

# answer = input("아무값이나 입력하세요 : ") 
# print(type(answer)) # 보통 문자열로 타입이 저장되나, 숫자도 가능
# print("입력하신 값은 " + answer + "입니다.")

# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
# print("{0: >10}".format(500))
# 양수일 땐 +로 표시, 음수일 땐 -로 표시
# print("{0: >+10}".format(-500))
# 왼쪽 정렬하고, 빈칸을 _로 채움
# print("{0:_<+10}".format(500))
# 3자리마다 콤마를 찍어주기
# print("{0:,}".format(10000000000))
# 3자리마다 콤마를 찍어주기 +,- 부호 붙이기
# print("{0:+,}".format(10000000000))
# print("{0:+,}".format(-10000000000))
# 3자리마다 콤마 찍고, 부호 붙이고, 자릿수 확보, 빈자리 ^채우기
# print("{0:^<+30,}".format(10000000000))
# 소수점 출력
# print("{0:f}".format(5/3))
# 소수점 특정 자리수 까지 표시 (소수점 3쨰에서 반올림)
# print("{0:.2f}".format(5/3))

# 파일 입출력

# score_file = open("score.txt", "w", encoding="utf8")
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8")
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline(), end="") # 줄별로 읽기동작 수행, 한 줄 읽고 커서는 다음줄로
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# score_file.close()

# 위 방법 몇줄인지 모를때 
# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

# 다른 방법 list활용
# score_file = open("score.txt", "r", encoding="utf8")
# lines = score_file.readlines() # readlines list 형태로 저장
# for line in lines:
#     print(line, end="")
# score_file.close()

#pickle 파일형태로 저장

# import pickle
# profile_file = open("prifile.pickle", "wb") #w는 쓰기, b는 바이너리
# profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) # profile  에 있는 정보를 file에 저장
# profile_file.close()

# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file) # pickle에 있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()

# with 파일 작업 동일하게 가능

# import pickle

# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))
    
# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")

# with open("study.txt", "r", encoding="utf8") as study_file: 
#     print(study_file.read()) #read 함수를 활용해야 불러올수 있음

# Quiz 보고서
''' 
- X 주차 주간보고 -
부서 : 
이름 : 
업무요약 :

1주차 ~ 50주차 보고서 파일을 만드는 프로그램 작성
조건 : 파일명은 '1주차.txt', ... 와같이
'''
# 내가 쓴 답
# import pickle

# for report in range(1, 51):
#     with open("{0}주차.txt".format(report), "w", encoding="utf8") as report_file:
#         report_file.write(" - {0} 주차 주간보고 - \n부서 : \n이름 : \n업무 요약 : ".format(report))

# for report in range(1, 51):
#     with open("{0}주차.txt".format(report), "r", encoding="utf8") as report_file:
#         print(report_file.read())

# 답 기본적인 골자는 같으나 보기에 깔끔하다. 특히 str(i)로 format()부분을 제외한게 눈에 띈다.

# for report in range(1, 51):
#     with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
#         report_file.write("- {0} 주차 주간보고 -".format(i))
#         report_file.write("\n부서 :")
#         report_file.write("\n이름 :")
#         report_file.write("\n업무요약 :")

# 혼자 해보고 싶은것 : 위 퀴즈에 input을 사용해 파일을 불러오면 terminal에서 내용을 입력하는 프로그램 추가

# Class 하나의 틀. 연관이된 변수와 함수의 집합
# 스타크래프트 예제
# 마린 : 공격유닛, 군인, 총 쏨

# name = "마린"
# hp = 40
# damage = 5

# print("{0} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# # 탱크 : 공격유닛, 탱크, 포를 쏨, 일반/시즈모드.

# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# print("{0} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

# tank2_name = "탱크2"
# tank2_hp = 150
# tank2_damage = 35

# print("{0} 유닛이 생성되었습니다.".format(tank2_name))
# print("체력 {0}, 공격력 {1}\n".format(tank2_hp, tank2_damage))

# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력{2}]".format(\
#         name, location, damage))

# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)
# attack(tank2_name, "1시", tank2_damage)

# 탱크 하나 추가

# 클래스 활용 + __init__(객체:클래스로 부터 만들어지는것. 생성자\
# self를 제외하고 정보갯수를 동일하게 넣어야함) 사용

# 일반유닛
# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage 
#         print("{0} 유닛이 생성되었습니다.".format(self.name))
#         print("체력 : {0}, 공격력 : {1}".format(self.hp, self.damage))

# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)

# 멤버 변수 self.xxx : 클래스 내에 정의된 변수

# 레이스 : 공중 유닛, 비행기. 클로킹

# wraith1 = Unit("레이스", 80, 5)
# print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# # 마인드 컨트롤 :  상대방 유닛을 뺏는것

# wraith2 = Unit("빼앗은 레이스", 80, 5)
# wraith2.cloking = True

# if wraith2.cloking == True:
#     print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name)) 
# \외부에서 변수를 추가로 할당

# 메소드 함수 추가로 만들기.
# 공격유닛

# class AttackUnit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
        
#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 : {2}]"\
#             .format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))

# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")

# firebat1.damaged(25)
# firebat1.damaged(25)

# 상속 Unit.__init__을 통해 부모 클래스와의 교집합 부분을 상속받음(damage부분은 삭제)
# 메딕 : 공격력 없음.

# class Unit:
#     def __init__(self, name, hp):
#         self.name = name
#         self.hp = hp

# class AttackUnit(Unit):
#     def __init__(self, name, hp, damage):
#         Unit.__init__(self, name, hp)
#         self.damage = damage

#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 : {2}]"\
#             .format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))

# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")

# firebat1.damaged(25)
# firebat1.damaged(25)

# 다중상속 부모클래스가 둘이상
# 드랍쉽 : 수송기, 공중유닛. 공격 불가
# class Unit:
#     def __init__(self, name, hp):
#         self.name = name
#         self.hp = hp

# class AttackUnit(Unit):
#     def __init__(self, name, hp, damage):
#         Unit.__init__(self, name, hp)
#         self.damage = damage

#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 : {2}]"\
#             .format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))

# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
#             .format(name, location, self.flying_speed))

# # 공중 공격 유닛 클래스

# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, damage)
#         Flyable.__init__(self, flying_speed)

# 발키리 : 공중 공격 유닛. 한번에 14발 미사일 발사

# valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
# valkyrie.fly(valkyrie.name, "3시")

# 정리 : Unit 클래스와 Flyable 클래스 두개를 상속받음.

# 메소드 오버라이딩 (speed 추가)

class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
    
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
            .format(self.name, location, self.speed))

class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 : {2}]"\
            .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0,  damage) # 지상 스피드 0처리
        Flyable.__init__(self, flying_speed)
    
    def move(self, location): # 같은 함수를 재정의함
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# # 벌쳐 : 지상유닛, 기동성이 좋음
# vulture = AttackUnit("벌쳐", 80, 10, 20)

# # 배틀크루저 : 공중유닛, 체력 좋음, 공격력 좋음
# battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

# vulture.move("11시")
# # battlecruiser.fly(battlecruiser.name, "9시")
# # 매번 지상, 공중 유닛 확인해서 다른 함수를 써야함 오버라이딩 사용하여 새로 정의
# battlecruiser.move("9시")

# pass 아무것도 안하고 일단은 넘어간다.
# 건물

# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         pass # 일단은 __init__함수 내에서 완성된것 처럼 넘어간다.

# # 서플라이 디폿 : 건물, 1개 건물 = 8 유닛.
# supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")
    
# def game_over():
#     pass

# game_start()
# game_over()

# super 

class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        super.__init__(name, hp, 0) # = Unit.__init__(self, name, hp, 0)
        self.location = location
        
# practice_class 파일에서 이어짐.