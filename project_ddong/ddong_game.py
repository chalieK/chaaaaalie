import pygame
import random

pygame.init()

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("똥 피하기 Game") # 게임이름

# FPS
clock = pygame.time.Clock()

score = 0

# 1. 사용자 게임 초기화(배경화면, 게임 이미지, 좌표, 폰트 등)

# 배경이미지 불러오기

background = pygame.image.load("C:\\Users\\user\\Desktop\\py_workspace\\project_ddong\\background.png")

# 이동할 좌표
to_x = 0

# 캐릭터 불러오기

character = pygame.image.load("C:\\Users\\user\\Desktop\\py_workspace\\project_ddong\\character.png")
character_size = character.get_rect().size 
character_height = character_size[0]
character_width = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

character_speed = 0.5

# 적 캐릭터
enemy = pygame.image.load("C:\\Users\\user\\Desktop\\py_workspace\\project_ddong\\enemy.png")
enemy_size = enemy.get_rect().size 
enemy_height = enemy_size[0]
enemy_width = enemy_size[1]
enemy_x_pos = random.randrange(10, 440) 
enemy_y_pos = 0

enemy_speed = 20

game_font = pygame.font.Font(None, 40)

total_time = 10

start_ticks = pygame.time.get_ticks()

running = True 
while running:
    dt = clock.tick(30)

    # 2. 이벤트 처리(키보드, 마우스 등)    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 

    if event.type == pygame.KEYDOWN: #pygame.KEYDOWN 은 키 입력
        if event.key == pygame.K_LEFT:
            to_x -= character_speed    
        elif event.key == pygame.K_RIGHT:
            to_x += character_speed

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            to_x = 0

    # 3. 게임 캐릭터 위치 정의

    character_x_pos += to_x*dt

    
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    enemy_y_pos += enemy_speed
    if enemy_y_pos > screen_height:
        enemy_y_pos = random.randrange(0, 100)
        enemy_x_pos = random.randrange(0, 440) 
        score += 10

    if enemy_x_pos < 0: 
        enemy_x_pos = random.randrange(0, 100)
    elif enemy_x_pos > screen_width - enemy_width:
        enemy_x_pos = random.randrange(0, 440)

    # 4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
    
    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("게임 오버")
        running = False


    # 5. 화면에 그리기
    
    # 배경 그리기
    
    screen.blit(background, (0, 0))

    # 캐릭터 그리기
    screen.blit(character, (character_x_pos, character_y_pos))

    # 적 그리기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))
    
    # 타이머 넣기
    elapsed_time = ((pygame.time.get_ticks()) - start_ticks) / 1000
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255))
    screen.blit(timer, (10,10))
    
        
    # 점수판 넣기
    scores = game_font.render(str(int(score)), True, (255, 255, 255))
    screen.blit(scores, (400,10))

    # 타이머 0 이하
    if total_time - elapsed_time <=0:
        print("승리! 점수 : ", str(score), "점")
        running = False


    pygame.display.update() # 화면을 계속해서 그려주기!

pygame.time.delay(500)

pygame.quit()