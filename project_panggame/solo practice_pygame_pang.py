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


# 무기 구현하기 : 작동 x 스페이스바 입력이 안되는것같음
weapons = [] # 여러발 발사
weapon_speed = 15



# 볼 불러오기
ball_images = [
    pygame.image.load("C:\\Users\\user\\Desktop\\py_workspace\\project_panggame\\balloon1.png"),
    pygame.image.load("C:\\Users\\user\\Desktop\\py_workspace\\project_panggame\\balloon2.png"),
    pygame.image.load("C:\\Users\\user\\Desktop\\py_workspace\\project_panggame\\balloon3.png"),
    pygame.image.load("C:\\Users\\user\\Desktop\\py_workspace\\project_panggame\\balloon4.png")
]

ball_speed_y = [-18, -15, -12, -9]
balls = []

balls.append({
    "pos_x":50,
    "pos_y":50,
    "img_idx":0,
    "to_x":3,
    "to_y":-6,
    "init_spd_y":ball_speed_y[0]
})

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
            elif event.key == pygame.K_SPACE: 
                weapon_x_pos = character_x_pos + (character_width / 2) - (weapon_width / 2) # 스페이스를 누르면 나타나는 걸로 다시 만들어야함
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0
    
    character_x_pos += character_to_x*dt
        
    # 무기 위치 조정
    weapons = [[w[0], w[1] - weapon_speed] for w in weapons] # 무기 위치 갱신
    weapons = [[w[0], w[1]] for w in weapons if w[1] > 0] # 천장에 닿은 무기 없애기

    # 볼 위치 정의
    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]

    # 캐릭터 경계값 
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    
    # 볼 경계값
    if ball_pos_x < 0 or ball_pos_x > screen_width - ball_width:
        ball_val["to_x"] = ball_val["to_x"]*-1 # 벽에 부딪히면 반대로 튀게끔
    
    if ball_pos_y >= screen_height - stage_height - ball_height:
        ball_val["to_y"] = ball_val["init_spd_y"]
    else: 
        ball_val["to_y"] += 0.5
    
        ball_val["pos_x"] += ball_val["to_x"]
        ball_val["pos_y"] += ball_val["to_y"]


    # 4. 충돌 처리

    # 5. 화면에 그리기
    
    # 배경 그리기
    screen.blit(background, (0,0))
    
    # 무대 그리기
    screen.blit(stage, (0, (screen_height - stage_height)))

    # 캐릭터 그리기
    screen.blit(character, (character_x_pos, character_y_pos))

    # 무기 그리기
    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

    # 볼 그리기
    for idx, val in enumerate(balls):
        ball_pos_x = val["pos_x"]
        ball_pos_y = val["pos_y"]
        ball_img_idx = val["img_idx"]
        screen.blit(ball_images[ball_img_idx], (ball_pos_x, ball_pos_y))

    pygame.display.update() # 화면을 계속해서 그려주기!


pygame.quit()

# 무기 구현과 공 작동에서 혼자 하기 실패