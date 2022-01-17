# 집합(set) : 중복 안됨, 순서 없음
# my_set = {1,2,3,3,3} # 중복값 무시
# print(my_set)

# java = {"유재석", "김태호", "양세형"}
# python = set(["유재석", "박명수"])

# # #교집합 (java와 python을 모두 할 수 있는 개발자)
# print(java & python)
# print(java.intersection(python))

# # 합집합(java 도 할 수 있거나 python 할 수 있는 개발자)
# print(java | python)
# print(java.union(python))

# # 차집합(java는 할 줄 알지만, python은 할 줄 모르는 개발자)
# print(java - python)
# print(java.difference(python))

# # python 할 줄 아는 사람 늘어남.
# python.add("김태호")
# print(java - python)
# print(java.difference(python))
# print(python)

# # java를 까먹음
# java.remove("김태호")
# print(java)

# 자료구조의 변경
# 커피숍
# menu = {"커피", "우유", "주스"}
# print(menu, type(menu))

# menu = list(menu)
# print(menu, type(menu))

# menu = tuple(menu)
# print(menu, type(menu))

# menu = set(menu)
# print(menu, type(menu))

# Quiz 파이썬 코딩대회 댓글 이벤트 1명은 치킨, 3명은 커피 쿠폰/ 추첨프로그램 작성
#조건 1 : 편의상 댓글은 20명이 작성, 아이디는 1~20
#조건 2 : 댓글 내용과 상관없이 무작위로 추첨하되 중복 불가
#조건 3 : random 모듈의 shuffle과 sample을 활용

# 출력 예제
''' 당첨자 발표
치킨 당첨자 : 1
커피 당첨자 : [2, 3, 4]
-- 축하합니다 -- 
'''
# (활용예제)
# from random import *
# lst = [1,2,3,4,5]
# # print(lst)
# # shuffle(lst)
# # print(lst)
# print(sample(lst, 1))

# 내 정답
# from random import *
# lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] 
# # print(lst) 
# print("당첨자 발표\n치킨 당첨자 : " + str(sample(lst, 1)))
# print("커피 당첨자 : " + str(sample(lst, 3)))
# print("-- 축하합니다 --")

# "나도코드"정답 
# from random import * 
# users = range(1, 21) 
# # print(type(users)) # range 상태로는 list 사용 불가능 -> 변환
# users = list(users)
# # print(type(users))
# print(users)
# shuffle(users)
# print(users)

# # 중복이 불가해서 한번에 4명을 뽑아 변수로 작성
# winners = sample(users, 4)

# print("-- 당첨자 발표 -- ")
# print("치킨 당첨자 : {0}".format(winners[0]))
# print("커피 당첨자 : {0}".format(winners[1:]))
# print(" -- 축하합니다 -- ")

# 후기.. format을 떠올리지도 못함. 외워야지

# if 문

# weather = input("오늘 날씨는 어때요? ")
# # if/elif/else 조건 : 
# #    실핼 명령문
# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else: 
#     print("준비물 필요 없어요")

# temp = int(input("기온은 어때요? "))
# if 30 <= temp:
#     print("너무 더워요. 나가지 마세요")
# elif 10<= temp and temp < 30:
#     print("괜찮은 날씨에요")

# elif 0<= temp < 10:
#     print("쌀쌀할 수 있어요. 외투를 챙기세요")
# else:
#     print("너무 추워요. 나가지 마세요.")

# for 문 (반복문)
# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")

# for waiting_no in [0,1,2,3,4]:
#     print("대기번호 : {0}".format(waiting_no))

# for waiting_no in range(5): #위와 같지만 더 편함(1번부터 시작하고 싶으면 = (1, 6))
#     print("대기번호 : {0}".format(waiting_no))

# starbucks = ["아이언맨", "토르", "그루트"]
# for customer in starbucks:
#     print("{0}손님, 커피가 준비되었습니다.".format(customer))

# while(반복문)
# customer = "토르"
# index = 5
# while index >= 1 :
#     print("{0}, 커피가 준비 되었습니다. {1}번 남았어요.".format(customer, index))
#     index -= 1 #한번씩 줄여나감
#     if index == 0:
#         print("커피는 폐기처분되었습니다.")

# customer = "아이언맨"
# index = 1
# while True:
#     print("{0}, 커피가 준비 되었습니다. 호출 {1} 회".format(customer, index))
#     index += 1 
# 무한루프에 빠짐, 강제종료는 ctrl + c

# customer = "토르"
# person = "Unkown"

# while person != customer:
#     print("{0}, 커피가 준비 되었습니다".format(customer))
#     person = input("이름이 어떻게 되세요? ")

# continue 와 break

# absent = [2, 5] # 결석
# no_book = [7]  # 책없음
# for student in range(1, 11): # 1~10 출석번호
#     if student in absent: 
#         continue # 다음 반복으로 진행
#     elif student in no_book:
#         print("오늘 수업 여기까지. {0}는 교무실로 따라와.".format(student))
#         break
#     print("{0}, 책을 읽어봐".format(student))

# 한줄 for 문
# 출석번호 1,2,3,4 앞에 100을 붙이기로 함 -> 101,102,103,104
# students = [1,2,3,4,5]
# print(students)
# students = [i+100 for i in students]
# print(students)

# 학생 이름을 길이로 변환
# students = ["Iron man", "Thor", "I am Groot"]
# students = [len(i) for i in students]
# print(students)

# 학생 이름을 대문자로 변환
# students = ["Iron man", "Thor", "I am Groot"]
# students = [i.upper() for i in students]
# print(students)

# Quiz) 카카오 서비스 택시기사, 50명의 승객과 매칭 기회, 총 탑승 승객 수를 구하는 프로그램
# 조건 1 : 승객별 운행 소요시간은 5 ~ 50분 사이의 난수
# 조건 2 : 기사는 소요시간, 5 ~ 15분 사이의 승객만 매칭해야합니다. 
'''(출력문 예제)
[o] 1번째 손님 (소요시간 : 15분)
[ ] 2번째 손님 (소요시간 : 50분)
[o] 3번째 손님 (소요시간 : 5분)
...
[ ] 50번째 손님 (소요시간 : 16분)

총 탑승 승객 : 2분 '''


# 정답 (count라는 변수를 만들어 한번작업이 끝날때마다 세어주는 +=의 활용이 눈에 띄었고, 연산자다음에=을 써야 조건문에 오류없이 작동됨을 알게됨) 
# from random import * 
# cnt = 0
# for i in range(1, 51):
#     time = randrange(5,51)
#     if 5 <= time <= 15 :
#         print("[o]{0}번째 손님 (소요시간 : {1}분)".format(i, time))
#         cnt += 1
#     else :
#         print("[ ]{0}번째 손님 (소요시간 : {1}분)".format(i, time))

# print("총 탑승 승객 : {}분".format(cnt))

'''고통의 흔적... 

passinger = range(1, 51)
passinger = list(passinger)
time = range(1, 51)
notpassinger = range(15, 51)
num = range(1, 16)
elif time == notpassinger:
   print("[ ]{0}번째 손님 (소요시간 : {1}분)".format(passinger.index(2), time)

    time > 15
    print("[ ]{0}번째 손님 (소요시간 : {1}분".format(passinger, time))
    
5 ~ 50 사이의 난수 먼저 각각의 난수가 passinger, list인 passinger가 숫자로 인식이 되지않음
리스트 중에서 하나만, 순서대로 출력해야함
방법 1 해당하는 난수 탑승으로 프로그램짜고 탑승의 수를 세는것.
너무 어렵게 생각하여 zip 함수까지 가져왔지만, 실상은 넘나 심플한것.. '''

#함수

# def open_account():
#     print("새로운 계좌가 생성되었습니다.")
    
# # open_account()

# def deposit(balance, money): # 입금
#     print("입금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance + money))
#     return balance + money

# def withdraw(balance, money): # 출금
#     if balance >= money: # 잔액이 출금보다 많으면
#        print ("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance - money))
#        return balance - money
#     else:
#         print ("출금이 완료되지 않았습니다. 잔액은 {0}원입니다.".format(balance))
#         return balance

# def withdraw_night(balance, money): # 저녁에 출금
#     commission = 100 # 수수료 100원
#     return commission, balance - money - commission

# balance = 0 # 잔액
# balance = deposit(balance, 1000)
# # balance = withdraw(balance, 2000)
# # balance = withdraw(balance, 500)
# commission, balance = withdraw_night(balance, 500)
# print("수수료 {0}원이며, 잔액은 {1}원입니다.".format(commission, balance))

# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}"\
#         .format(name, age, main_lang))
        
# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")

# 같은 학교 같은 학년 같은 반 같은 수업 _불필요한 값 매번 적을 필요없음

# def profile(name, age = 17, main_lang = "파이썬"):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}"\
#         .format(name, age, main_lang))

# profile("유재석")
# profile("김태호")

# 키워드값을 이용한 함수 호출

# def profile(name, age, main_lang):
#     print(name, age, main_lang)

# profile(name = "유재석", main_lang="파이썬", age=20)
# profile(main_lang="자바", age=25, name="김태호")

# 가변인자를 이용한 함수 호출
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {0}\t".format(name, age), end=" ") # 끝에 end=을 사용하면, 줄바꿈없이 다음 내용 쭉 이어서 나옴
#     print(lang1, lang2, lang3, lang4, lang5)

# def profile(name, age, *language):
#     print("이름 : {0}\t나이 : {0}\t".format(name, age), end=" ") # 끝에 end=을 사용하면, 줄바꿈없이 다음 내용 쭉 이어서 나옴
#     for lang in language:
#         print(lang, end=" ")
#     print()

# profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JS") #새로운언어추가 등
# profile("김태호", 25, "Kotlin", "swift") #매번 "", "", ..이렇게 쓰기 귀찮음

# 지역변수(함수 내에서만 쓸수 있는것), 전역변수(프로그램 모든공간에서 사용가능)
# gun = 10

# def checkpoint(soldiers): # 경계근무
#     # gun = 20 지역변수 함수내에만 사용가능
#     global gun # 전역 공간에 있는 gun 사용
#     gun = gun -soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))

# def checkpoint_ret(gun, soldiers):
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
#     return gun

# print("전체 총 : {0}".format(gun))
# # checkpoint(2) # 2명이 경계 근무
# gun = checkpoint_ret(gun, 2)
# print("남은 총 : {0}".format(gun))

# Quiz) 표준 체중을 구하는 프로그램을 작성
''' (성별에 따른 공식)
 남자 : 키(m) * 키(m) * 22
 여자 : 키(m) * 키(m) * 21

 조건1 : 표준 체중은 별도의 함수 내에서 계산
        * 함수명 : std_weight
        * 전달값 : 키(height), 성별(gender)
 조건2 : 표준 체중은 소수점 둘째 자리까지 표시

 (출력 예제)
 키 175cm 남자의 표준 체중은 67.38kg 입니다. '''
 
# 내가 쓴 답

# def std_weight(height, gender):
#     if gender == "남자":
#         std_weight = (height*0.01) * (height*0.01) * 22
#     else:
#         std_weight = (height*0.01) * (height*0.01) * 21
#         print("[함수 내] : 표준체중 = {0}kg".format(round(std_weight, 2)))
#     return round(std_weight, 2)

# height = 160
# gender = "여자"
# # print(type(height))
# print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, std_weight(height, gender)))

# print("[함수 내] 표준체중 : " +  str(round((175*0.01)*(175*0.01)*22, 2))) #이것과 같은 모양이 되야함 소수점 둘째자리는 round(a, 2)

# 정답 # 내 답에서 쓴 방식이 훨씬 간결하게 나와있다. 바로 return을 쓰고, weight 변수를 만들어 함수를 출력하는 방식으로 
# 깔끔하게 보인다.
# def std_weight(height, gender):
#     if gender == "남자":
#         return height * height *22
#     else:
#         return height * height *21

# height = 175
# gender = "남자"
# weight = round(std_weight(height / 100, gender), 2)
# print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))

#표준입출력
# sep 쉼표 등 추가 , end 뒷 부분을 연달아 출력
import sys
print("Python", "Java", file=sys.stdout) 
print("Python", "Java", file=sys.stderr)