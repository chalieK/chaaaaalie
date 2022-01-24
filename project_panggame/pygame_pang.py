import random
import pygame
############################################################
# 기본 초기화(반드시 해야하는것들)
pygame.init()

# 화면 크기 설정
screen_width = 640 # 가로 크기
screen_height = 480 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Pang Game") # 게임이름

# FPS
clock = pygame.time.Clock()
####################################################################


# 1. 사용자 게임 초기화(배경화면, 게임 이미지, 좌표, 폰트 등)

# 배경 이미지 불러오기
background = pygame.image.load("C:\\Users\\user\\Desktop\\py_workspace\\project_panggame\\background.png")

# 무대 이미지 불러오기
stage = pygame.image.load("C:\\Users\\user\\Desktop\\py_workspace\\project_panggame\\stage.png")
stage_size = stage.get_rect().size
stage_width = stage_size[0]
stage_height = stage_size[1]

# 메인 캐릭터 불러오기
character = pygame.image.load("C:\\Users\\user\\Desktop\\py_workspace\\project_panggame\\character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = (screen_height - stage_height) - character_height

# 이동할 위치
character_to_x = 0

# 캐릭터 이동속도
character_speed = 0.5

# 무기 불러오기
weapon = pygame.image.load("C:\\Users\\user\\Desktop\\py_workspace\\project_panggame\\weapon.png")
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]
weapon_height = weapon_size[1]
weapon_x_pos = character_x_pos + (character_x_pos * 1/3) # 스페이스를 누르면 나타나는 걸로 다시 만들어야함
weapon_y_pos = screen_height

# 무기 구현하기 : 캐릭터 위치에서부터 위로 올라감. 아이디어는 좋지만 작동 x

weapon_speed = 1

weapon_load = False

# 볼 불러오기
balloon1 = pygame.image.load("C:\\Users\\user\\Desktop\\py_workspace\\project_panggame\\balloon1.png")
balloon1_size = balloon1.get_rect().size
balloon1_width = balloon1_size[0]
balloon1_height = balloon1_size[1]
balloon1_x_pos = random.randrange(0, 550)
balloon1_y_pos = random.randrange(0, 100)

balloon2 = pygame.image.load("C:\\Users\\user\\Desktop\\py_workspace\\project_panggame\\balloon2.png")
balloon2_size = balloon2.get_rect().size
balloon2_width = balloon2_size[0]
balloon2_height = balloon2_size[1]
# balloon2_x_pos = none
# balloon2_y_pos = None

balloon3 = pygame.image.load("C:\\Users\\user\\Desktop\\py_workspace\\project_panggame\\balloon3.png")
balloon3_size = balloon3.get_rect().size
balloon3_width = balloon3_size[0]
balloon3_height = balloon3_size[1]
# balloon3_x_pos = None
# balloon3_y_pos = None

balloon4 = pygame.image.load("C:\\Users\\user\\Desktop\\py_workspace\\project_panggame\\balloon4.png")
balloon4_size = balloon4.get_rect().size
balloon4_width = balloon4_size[0]
balloon4_height = balloon4_size[1]
# balloon4_x_pos = None
# balloon4_y_pos = None



running = True 
while running:
    dt = clock.tick(30)

    # 2. 이벤트 처리(키보드, 마우스 등)    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 
    
    # 3. 게임 캐릭터 위치 정의
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed
            elif event.type == pygame.K_SPACE: 
                weapon_load = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0
    
    character_x_pos += character_to_x*dt
    weapon_y_pos += weapon_speed*dt
    # 볼 위치 정의
    
    # 캐릭터 경계값 
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    
    if balloon1_x_pos < 0:
        balloon1_x_pos = 0
    elif balloon1_x_pos > screen_width - balloon1_width:
        balloon1_x_pos = screen_width - balloon1_width


    # 4. 충돌 처리

    # 5. 화면에 그리기
    
    # 배경 그리기
    screen.blit(background, (0,0))
    
    # 무대 그리기
    screen.blit(stage, (0, (screen_height - stage_height)))

    # 캐릭터 그리기
    screen.blit(character, (character_x_pos, character_y_pos))

    # 무기 그리기
    if weapon_load == True:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))
        weapon_y_pos -= weapon_speed
    elif weapon_y_pos == 0:
        weapon_load = False

    # 볼 그리기
    screen.blit(balloon1, (balloon1_x_pos, balloon1_y_pos))
    # screen.blit(balloon2, (0, 0))
    # screen.blit(balloon3, (0, 0))
    # screen.blit(balloon4, (0, 0))
    
    pygame.display.update() # 화면을 계속해서 그려주기!


pygame.quit()