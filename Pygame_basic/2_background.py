import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game") # 게임이름

# 배경이미지 불러오기
background = pygame.image.load("C:/Users/user/Desktop/py_workspace/Pygame_basic/background.png")

# 이벤트 루프가 실행되고있어야 창이 꺼지지 않음
running = True # 게임이 진행중인가?
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생했는지 확인
            running = False # 게임이 진행중이 아님
    
    # screen.fill(0, 0, 255) # 참고 : 스크린 채우기
    screen.blit(background, (0, 0)) # 배경 그리기 : blit을 사용하여 이미지 좌표설정

    pygame.display.update() # 화면을 계속해서 그려주기!

# 게임 종료
pygame.quit()