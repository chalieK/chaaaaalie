import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game") # 게임이름

# 배경이미지 불러오기 # 탈출문자 떄문에 역슬래쉬를 슬래쉬로 바꿔줌
background = pygame.image.load("C:/Users/user/Desktop/py_workspace/Pygame_basic/background.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:/Users/user/Desktop/py_workspace/Pygame_basic/charater.png")
character_size = character.get_rect().size # 이미지 크기를 구해옴
character_width = character_size[0] # 캐릭터의 가로크기
character_height = character_size[1] # 캐릭터의 세로크기
character_x_pos = (screen_width / 2) - (character_width / 2) # 화면 가로의 절반에 해당하는 위치에 캐릭터 위치(가로)
character_y_pos = screen_height - character_height # 화면 세로크기 가장 아래에 해당하는 곳에 위치(세로)

# 이벤트 루프가 실행되고있어야 창이 꺼지지 않음
running = True # 게임이 진행중인가?
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생했는지 확인
            running = False # 게임이 진행중이 아님
    
    screen.blit(background, (0, 0)) # 배경 그리기 : blit을 사용하여 이미지 좌표설정 (0,0) 은 오른쪽 / 아래로 그려짐
    
    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기

    pygame.display.update() # 화면을 계속해서 그려주기!

# 게임 종료
pygame.quit()