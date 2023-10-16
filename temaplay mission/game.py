import pygame, sys
from pygame.locals import*
import random
import time
import eyed3

pygame.init()

title = "Piano Game"
pygame.display.set_caption(title)

#시작화면 만들기
def game():
    width = 400
    height = 500
    start_screen = pygame.display.set_mode((width, height))#사이즈 설정.(400 X 500)
    
    title_font = pygame.font.SysFont('Sans', 40, True, False)# sans 라는 폰트로 40포인트, 글자 기울이기를 설정함.
    title_message = "Piano Game."
    title_message_object = title_font.render(title_message, True, (0, 0, 0))# 색깔 설정
    title_message_rect = title_message_object.get_rect()
    title_message_rect.center = ((width / 2), (height / 5))#이미지 조작 설정 함수
    
    pygame.font.init()
    sub_font = pygame.font.SysFont('malgungothic', 20, False, False)
    start_message = "게임시작"
    start_message_object = sub_font.render(start_message, True, (0, 0, 0))
    start_message_rect = start_message_object.get_rect()
    start_message_rect.center = ((width / 2), (height / 2))
    
    exp_message = "설명"
    exp_message_object = sub_font.render(exp_message, True, (0, 0, 0))
    exp_message_rect = exp_message_object.get_rect()
    exp_message_rect.center = ((width / 2), (height / 1.6))
    
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_SPACE:
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.mouse.get_rel()
                mouse_pos = pygame.mouse.get_pos()
                if mouse_pos[0] > start_message_rect.left and mouse_pos[0] < start_message_rect.right and mouse_pos[1] > start_message_rect.top and mouse_pos[1] < start_message_rect.bottom:
                    sound_track()
                if mouse_pos[0] > exp_message_rect.left and mouse_pos[0] < exp_message_rect.right and mouse_pos[1] > exp_message_rect.top and mouse_pos[1] < exp_message_rect.bottom:
                    explain()# 49번: 설명 항목칸에 들어가서 

        
        start_screen.fill((255, 255, 255))
        start_screen.blit(title_message_object, title_message_rect)
        start_screen.blit(start_message_object, start_message_rect)
        start_screen.blit(exp_message_object, exp_message_rect)
        pygame.display.update()


def sound_track():
    white = (255,255,255)
    black = (0,0,0)

    screen_width = 400
    screen_height = 500
    size = [screen_width, screen_height]

    screen = pygame.display.set_mode(size)

    font = pygame.font.SysFont("malgungothic", 20, True, True)

    text = font.render("배경음악 선택", True, black)

    button1 = pygame.image.load("1.png")
    button1 = pygame.transform.scale(button1, (screen_width/2, screen_height/10))
    button2 = pygame.image.load("2.png")
    button2 = pygame.transform.scale(button2, (screen_width/2, screen_height/10))
    button1rect = button1.get_rect()
    button1rect.x = screen_width/4
    button1rect.y = screen_height*1/4
    button2rect = button2.get_rect()
    button2rect.x = screen_width/4
    button2rect.y = screen_height*2/4

    
    back = pygame.image.load("triangle.png")
    back_rect = back.get_rect()

    done = False
    clock = pygame.time.Clock()

    while not done:
        clock.tick(10)
        screen.fill(white)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pygame.mouse.get_rel()
                mouse_pos = pygame.mouse.get_pos()
                if mouse_pos[0] > button1rect.left and mouse_pos[0] < button1rect.right and mouse_pos[1] > button1rect.top and mouse_pos[1] < button1rect.bottom:
                    game_start("Bee.mp3", 220)
                if mouse_pos[0] > button2rect.left and mouse_pos[0] < button2rect.right and mouse_pos[1] > button2rect.top and mouse_pos[1] < button2rect.bottom:
                    game_start("HER.mp3", 180)  
                if mouse_pos[0] > back_rect.left and mouse_pos[0] < back_rect.right and mouse_pos[1] > back_rect.top and mouse_pos[1] < back_rect.bottom:
                    game()
        
        screen.blit(text, (screen_width/3, screen_height/100))
        screen.blit(button1, (screen_width/4, screen_height*1/4))
        screen.blit(button2, (screen_width/4, screen_height*2/4))
        screen.blit(back, (0,0))
        pygame.display.update()


def explain():
    white = (255,255,255)
    black = (0,0,0)

    screen_width = 400
    screen_height = 500
    size = [screen_width, screen_height]

    screen = pygame.display.set_mode(size)


    font = pygame.font.SysFont("malgungothic", 20, True, True)

    text = font.render("게임 플레이 방법", True, black)

    back = pygame.image.load("triangle.png")
    back_rect = back.get_rect()

    explain = pygame.image.load("explain.png")
    explain = pygame.transform.scale(explain,(screen_width, screen_height*9/10))

    done = False
    clock = pygame.time.Clock()

    while not done:
        clock.tick(10)
        screen.fill(white)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.mouse.get_rel()
                mouse_pos = pygame.mouse.get_pos()
                if mouse_pos[0] > back_rect.left and mouse_pos[0] < back_rect.right and mouse_pos[1] > back_rect.top and mouse_pos[1] < back_rect.bottom:
                    game()
            
        screen.blit(text, (screen_width/3,screen_height/100))
        screen.blit(back, (0,0))
        screen.blit(explain, (0, screen_height/10))
        pygame.display.update()

def game_start(music, music_time):
    # 화면 설정
    screen_width, screen_height = 400, 500
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("피아노 띵동띵동")
    font = pygame.font.SysFont("malgungothic", 20, True, True)

    # 홈버튼
    home = pygame.image.load("home.png")
    home_rect = home.get_rect()
    home_rect.x = screen_width -50
    home_rect.y = 0

    # 색상 정의
    white = (255, 255, 255)
    black = (0, 0, 0)

    # 시간 설정
    clock = pygame.time.Clock()

    # 피아노 타일 설정
    tile_width = 100
    tile_height = 50
    tiles = []
    speed = 5
    score = 0


    # score 확인
    
    def display_score():
        score_text = font.render(f"점수: {score}", True, white)
        screen.blit(score_text, (10, 10))

    # line
    line_width = 100
    line_height = 20

    q = pygame.image.load("line.png")
    q = pygame.transform.scale(q,(line_width-4, line_height))
    q_rect = q.get_rect()
    q_rect.x = 2
    q_rect.y = screen_height - line_height*3
    
    w = pygame.image.load("line.png")
    w = pygame.transform.scale(w,(line_width-4, line_height))
    w_rect = w.get_rect()
    w_rect.x = line_width + 2
    w_rect.y = screen_height - line_height*3
    
    e = pygame.image.load("line.png")
    e = pygame.transform.scale(e,(line_width-4, line_height))
    e_rect = e.get_rect()
    e_rect.x = line_width * 2 + 2
    e_rect.y = screen_height - line_height*3
    
    r = pygame.image.load("line.png")
    r = pygame.transform.scale(r,(line_width-4, line_height))
    r_rect = r.get_rect()
    r_rect.x = line_width * 3 + 2
    r_rect.y = screen_height - line_height*3
    
    # 화면을 4개의 세로 등분된 화면으로 나눔
    line_x_coordinates = [i * (screen_width // 4) for i in range(4)]  # 4개의 세로선

    def create_tile():
        x = random.choice(line_x_coordinates)
        y = 0
        color = white
        tile = pygame.Rect(x, y, tile_width, tile_height)
        tiles.append((tile, color))

    def move_tiles():
        for tile, _ in tiles:
            tile.move_ip(0, speed)

    def remove_tiles():
        for tile, _ in tiles:
            if tile.top > screen_height:
                tiles.remove((tile, _))

                
    # BPM 에 맞게 박자 간격 설정
    bpm = 324
    beat_interval = 1 / (bpm/60) # 밀리초 단위
    next_beat_time = time.time() + beat_interval

    tile_num = music_time * bpm/60

    running = True
    pygame.mixer.music.load( music )

    pygame.mixer.music.play()

    current_time = 0
    start_time = time.time()
    
    while running and music_time>=current_time - start_time:
        
        screen.fill(black)                   
        
        current_time = time.time()
        
        if current_time >= next_beat_time:
            
            create_tile()
            next_beat_time += beat_interval

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                    for tile in tiles:
                        if q_rect.colliderect(tile[0]) and event.key == pygame.K_q:
                            score+=1
                            tiles.remove((tile))
                        elif w_rect.colliderect(tile[0]) and event.key == pygame.K_w:
                            score+=1
                            tiles.remove((tile))
                        elif e_rect.colliderect(tile[0]) and event.key == pygame.K_e:
                            score+=1
                            tiles.remove((tile))
                        elif r_rect.colliderect(tile[0]) and event.key == pygame.K_r:
                            score+=1
                            tiles.remove((tile))
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.mouse.get_rel()
                mouse_pos = pygame.mouse.get_pos()
                if mouse_pos[0] > home_rect.left and mouse_pos[0] < home_rect.right and mouse_pos[1] > home_rect.top and mouse_pos[1] < home_rect.bottom:
                    pygame.mixer.music.pause()
                    game()
            

        move_tiles()
        remove_tiles()
        display_score()

        for tile, color in tiles:
            pygame.draw.rect(screen, color, tile)
        
        screen.blit(q, (2, screen_height - line_height*3))
        screen.blit(w, (line_width + 2, screen_height - line_height*3))
        screen.blit(e, (line_width * 2 + 2, screen_height - line_height*3))
        screen.blit(r, (line_width * 3 + 2,  screen_height - line_height*3))
        screen.blit(home, (screen_width - 50, 0))

        pygame.display.flip()
        clock.tick(60)


    pygame.mixer.music.pause()
    game_score(tile_num, score)

def game_score(tile_num, score):
    width = 400
    height = 500
    start_screen = pygame.display.set_mode((width, height))
    
    title_font = pygame.font.SysFont('malgungothic', 40, True, False)
    title_message_object = title_font.render(f"SCORE : {score}", True, (0, 0, 0))
    title_message_rect = title_message_object.get_rect()
    title_message_rect.center = ((width / 2), (height / 5))

    
    if  score >= tile_num*3/4:
        score_message = "Perfect"
    elif score >= tile_num*2/4:
        score_message = "Great"
    elif score >= tile_num*1/4:
        score_message = "Normal"
    else:
        score_message = "Bad"
    
    pygame.font.init()
    sub_font = pygame.font.SysFont('malgungothic', 20, False, False)
    score_message_object = sub_font.render(score_message, True, (0, 0, 0))
    score_message_rect = score_message_object.get_rect()
    score_message_rect.center = ((width / 2), (height * 2 / 5))
    
    home_message = "메인메뉴"
    home_message_object = sub_font.render(home_message, True, (0, 0, 0))
    home_message_rect = home_message_object.get_rect()
    home_message_rect.center = ((width / 2), (height / 1.6))
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_SPACE:
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.mouse.get_rel()
                mouse_pos = pygame.mouse.get_pos()
                if mouse_pos[0] > home_message_rect.left and mouse_pos[0] < home_message_rect.right and mouse_pos[1] > home_message_rect.top and mouse_pos[1] < home_message_rect.bottom:
                    game()

        
        start_screen.fill((255, 255, 255))
        start_screen.blit(title_message_object, title_message_rect)
        start_screen.blit(score_message_object, score_message_rect)
        start_screen.blit(home_message_object, home_message_rect)
        pygame.display.update()    
    

# 실행시 제일 먼저 실행
game()