#숫자열
# print(5)
# print(-10)
# print(3.14)
# print(1000)
# print(5+3)
# print(2*8)
# print(3*(3+1))
# #문자열
# print('풍선')
# print("나비")
# print("ㅋㅋㅋㅋㅋ")
# print("ㅋ"*9)
# #불리함 참 / 거짓
# print(5>10)
# print(5<10)
# print(True)
# print(False)
# print(not True)
# print(not False)
# print(not (5>10))
# #변수
# #애완동물을 소개해 주세요~
# #_part1
# print("우리집 강아지의 이름은 연탄이에요")
# print("연탄이는 4살이며, 산책을 아주 좋아해요")
# print("연탄이는 어른일까요? true")
# #_part2
# animal = "강아지"
# name = "연탄이"
# age =  4
# hobby = "산책"
# is_adult = age >=3
# print("우리집 "+ animal +"의 이름은 " + name + "에요")
# print(name + "는 "+ str(age) +"살이며," +hobby+ "을 아주 좋아해요")
# print(name + "는 어른일까요?" + str(is_adult))
# #_part3
# animal = "고양이"
# name = "해피"
# age =  4
# hobby = "낮잠"
# is_adult = age >=3
# print("우리집 "+ animal +"의 이름은 " + name + "에요")
# hobby = "공놀이"
# #print(name + "는 "+ str(age) +"살이며," +hobby+ "을 아주 좋아해요")
# print(name, "는 ", age, "살이며,", hobby, "을 아주 좋아해요")
# print(name + "는 어른일까요?" + str(is_adult))
#주석
#으로 문장 시작 
# 또는 ''' 이렇게 하면 여러문장이 주석처리 됩니다''' 
# 또는 ctrl + /

#quiz) 
# station = "사당"
# print(station + "행 열차가 들어오고 있습니다.")
# station = "신도림"
# print(station + "행 열차가 들어오고 있습니다.")
# station = "인천공항"
# print(station + "행 열차가 들어오고 있습니다.")

# #연산자
# print(2**3) #2^3 = 8
# print(5%3) # 나머지 구하기 2
# print(10%3) # 1
# print(5//3) # 몫 구하기 1
# print(10>=3) # true
# print(10 == 1) # 앞뒤가 같다 false
# print(3 + 4 == 7) # true
# print(1 != 3) #같지않다. true
# print(not 1 != 3) #true의 반대 false
# print((3>0) and (3<5)) # 두 조건 모두 충족 true
# print((3>0) & (3<5)) # true
# print((3>0) or (3 < 1)) # true
# print((3>0) | (3>5)) # true

# print(2 + 3 * 4) # 14
# print((2+3)*4) # 20
# number = 2+3*4 
# print(number)
# number = number +2
# print(number)
# number += 2
# print(number)
# number *= 2
# print(number)
# number /= 2 
# print(number)
# number -= 2
# print(number)
# number %= 2
# print(number)

#숫자처리함수
# print(abs(-5))#절대값 5
# print(pow(4, 2))#4^2 = 4*4 = 16
# print(max(5, 12))#최대값 12
# print(min(5, 12))#최소값 5
# print(round(3.14))#반올림 3

# from math import * # math library안의 모든것을 이용하겠다라는 의미
# print(floor(4.99)) # 내림 4
# print(ceil(3.14)) # 올림 4
# print(sqrt(16)) # 제곱근 4

#랜덤함수
# from random import * # random library안의 모든것을 이용하겠다라는 의미
# print(random()) # 랜덤함수를 통해 0.0 ~1.0 미만의 임의의 값 생성
# print(random()*10)
# print(int(random()*10)) #int 소수점 삭제
# print(int(random()*10+1)) #1 ~ 10 

# print(int(random()*45)+1) # 1~45이하의 임의의 값 생성
# print(int(random()*45)+1) # 1~45이하의 임의의 값 생성
# print(int(random()*45)+1) # 1~45이하의 임의의 값 생성
# print(int(random()*45)+1) # 1~45이하의 임의의 값 생성
# print(int(random()*45)+1) # 1~45이하의 임의의 값 생성

# print(randrange(1, 46))# 1~46미만의 임의의 값 생성
# print(randrange(1, 46))# 1~46미만의 임의의 값 생성
# print(randrange(1, 46))# 1~46미만의 임의의 값 생성
# print(randrange(1, 46))# 1~46미만의 임의의 값 생성
# print(randrange(1, 46))# 1~46미만의 임의의 값 생성

# print(randint(1, 45)) # 1~45이하의 임의의 값 생성

# quiz 코딩스터디모임 월 4회 3번은 온라인 1번 오프라인, 
#조건 1 랜덤날짜생성
#조건 2 월별날짜가 달라 28일 이내
#조건 3 매월 1~3일은 스터디 준비로 제외

# from random import *
# print("오프라인 스터디 모임 날짜는 매월" , str(randint(4,28)) ,"일로 선정되었습니다.")

#문자열

# sentence = '나는 소년입니다.'
# print(sentence)
# sentence2 = "파이썬은 쉬워요"
# print(sentence2)
# sentence3 = """
# 나는 소년이고, 
# 파이썬은 쉬워요
# """
# print(sentence3)

#슬라이싱 : 필요한정보만 잘라서 사용 (엑셀의 left나 vlookup함수와 유사 but 012345순서임)

# jumin =  "990120-1234567"
# print("성별 : " + jumin[7])
# print("연 : " + jumin[0:2]) # 0 ~ 2 직전까지 (0,1)
# print("월 : " + jumin[2:4])
# print("일 : " + jumin[4:6])
# print("생년월일 : " + jumin[:6]) # 처음부터 6직전까지
# print("뒤 7자리 : " + jumin[7:]) # 7부터 끝까지
# print("뒤 7자리 (뒤에부터) :" + jumin[-7:]) # 맨 뒤에서 7번째부터 끝까지

#문자열 처리함수

# python = "Python is Amazing"
# print(python.lower()) # 문장 모두 소문자
# print(python.upper()) # 문장 모두 대문자
# print(python[0].isupper()) # 문자 중 0번째가 대문자인가? true
# print(len(python)) # 문자 길이알려줌 lenth
# print(python.replace("Python", "Java")) # 바꾸고싶은 문자를 바꾸는것
# index = python.index("n") # 해당글자안에 n이 몇번째에 있는지
# print(index)
# index = python.index("n", index + 1 ) #해당글자 보다 1만큼 이후에 서 n의 위치를 찾는다
# print(index)
# print(python.find("n")) # 비슷한함수
# print(python.find("Java")) # 원하는 값이 이 이 문자에 포함 x될경우 -1반환 프로그램 굴러감
# # print(python.index("Java")) # 오류 -> 프로그램 종료
# print(python.count("n")) # n이 해당 문자안에 몇 번 들어있는지

#문자열 포맷
# print("a" + "b")
# print("a", "b")
#포맷 방법1 %
# print("나는 %d살 입니다." % 20)
# print("나는 %s를 좋아해요" % "파이썬") # 범용적임
# print("Apple 은 %c로 시작해요" % "A") #한 단어만 함
# print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간")) #순서대로 입력됨
#포맷 방법2 {}
# print("나는 {}살 입니다." .format(20))
# print("나는 {}색과 {}색을 좋아해요." .format("파란", "빨간"))
# print("나는 {1}색과 {0}색을 좋아해요." .format("파란", "빨간"))
#포맷 방법3 
# print("나는 {age}살이며, {color}색을 좋아해요." .format(age = 20, color = "빨간"))
# print("나는 {age}살이며, {color}색을 좋아해요." .format(color = "빨간", age = 20))
#포맷 방법4 f 변수의 값을 활용
# age = 20 
# color = "빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해요.")

#탈출 문자 \(역슬러쉬활용)
# print("백문이 불여일견\n백견이 불여일타") # \n : 줄바꿈
# print("저는 '나도코딩' 입니다.") # ''로 표기가능
# print('저는 "나도코딩" 입니다.')  
# print("저는 \"나도코딩\" 입니다.") #"""" 큰따옴표 안에 큰따옴표

# \\ : 문장 내에서 하나의 \로 출력
# print("C:\\Users\\user\\Desktop\\py_workspace>")
# \r : 커서를 맨 앞으로 이동
# print("Red Apple\rPine") #Red 가 지워지고 그자리에 Pine이 들어감
# \b : 백스페이스 (한 글자 삭제)
# print("Redd\bApple") 
# \t : 탭
# print("Redd\tApple")

#Quiz 사이트별 비밀번호를 만들어주는 프로그램
# 예 http://naver.com
# 규칙1 : http://부분은 제외 => naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e'갯수 +"!"로 구성

# 예) 생성된 비밀번호 : nav51!

# 내 답 : site = "http://google.co.kr"
# A = len(site) - (7 + len(site) - site.index("."))
# print("생성된 비밀번호 : " + site[7:10] + str(A) + str(site.count("e")) + "!")

# # print(len(site) - (7+4)) 실패
# print(str(site.count("e")) + "!") 실패
# # print(f"생성된 비밀번호 : {A}{B}!") 실패
# # print(site[7:10], site.count("e")) 아이디어만 차용
# print("!") 아이디어만 차용

# brainstorming
# 1. 선택적으로 앞 7자리와 뒤 4자리를 지울 수 있어야한다.
# 2. print함수 안에 예제의 내용이 모두 들어갈 수 있어야한다. (len, count("e") 등 모두 변수화?)
# 3. 절반해결 print("생성된 비밀번호 : " + site[7:10] + str(len(site)-11) + str(site.count("e")) + "!") 이 방식의 오류는 .co.kr 등의 도메인에는 적용이 안된다는 것. 해결방법필요.
# 4. 형태변환을 먼저 한 후 작업한다면 훨씬 수월할 것이라 판단.
# 5. 앞 쪽 http://부분은 고정된 위치이므로 처음 세자리를 끌어오는 슬라이싱 사용. 점 이후의 글자 수는 전체 글자 수 - 점 이전까지의 글자 수로 지정. 전체 글자수 - (앞의 고정된 글자 수 + 점 이후의 글자 수) = 가운데 글자 수

# 정답 : replace, index 를 활용하여 형태를 미리 변환 
# url = "http://google.co.kr"
# my_str = url.replace("http://", "") #규칙 1 # print(my_str)
# my_str = my_str[:my_str.index(".")] #규칙 2 # my_str[0:5] -> 0 ~ 5 직전까지. (0,1,2,3,4) # print(my_str)
# password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
# print("{0}의 비밀번호는 {1} 입니다.".format(url, password))

# 정답에서 사용한 논리는 쉬우면서도 세련됨...

# 리스트 [] 순서를 가지는 객체의 집합
# 지하철 칸 별로 10명, 20명, 30명
# subway1 = 10
# subway2 = 20
# subway3 = 30

# subway = [10, 20, 30]
# print(subway)

# subway = ["유재석", "조세호", "박명수"]
# print(subway)

# #조세호가 몇 번쨰 칸?
# print(subway.index("조세호"))

# #하하가 다음 정류장에서 다음 칸에 탐
# subway.append("하하") # 맨 뒤에 추가
# print(subway)

# # 정형돈이 유재석과 조세호 사이에 탐
# subway.insert(1, "정형돈")
# print(subway)

# # 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
# print(subway.pop())
# print(subway)

# # print(subway.pop())
# # print(subway)

# # print(subway.pop())
# # print(subway)

# # 같은 이름의 사람이 몇 명 있는지 확인
# subway.append("유재석")
# print(subway.count("유재석"))

# 정렬도 가능
# num_list = [5,2,4,3,1]
# num_list.sort()
# print(num_list)

# # 순서 뒤집기 가능
# num_list.reverse()
# print(num_list)

# # 모두 지우기
# num_list.clear()
# print(num_list)

# 다양한 자료형 함께 사용
# num_list = [5,2,4,3,1]
# mix_list = ["조세호", 20, True]
# print(mix_list)

# # 리스트 확장
# num_list.extend(mix_list)
# print(num_list)

# 사전(Dictionary)
