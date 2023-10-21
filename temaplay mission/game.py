import pygame, sys
from pygame.locals import*
import random
import time
import eyed3

pygame.init()

title = "Piano Game"
pygame.display.set_caption(title)

#시작화면 만들기
def game():#메인 화면
    width = 400
    height = 500
    start_screen = pygame.display.set_mode((width, height))#사이즈 설정.(400 X 500)
    
    title_font = pygame.font.SysFont('Sans', 40, True, False)# sans 라는 폰트로 40포인트, 글자 기울이기를 설정함.
    title_message = "Piano Game."
    title_message_object = title_font.render(title_message, True, (0, 0, 0))#색상 설정
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
                mouse_pos = pygame.mouse.get_pos()# 마우스 클릭 함수
                if mouse_pos[0] > start_message_rect.left and mouse_pos[0] < start_message_rect.right and mouse_pos[1] > start_message_rect.top and mouse_pos[1] < start_message_rect.bottom:
                    sound_track()# 똑같음.
                if mouse_pos[0] > exp_message_rect.left and mouse_pos[0] < exp_message_rect.right and mouse_pos[1] > exp_message_rect.top and mouse_pos[1] < exp_message_rect.bottom:
                    explain()# 49번: 마우스 포인터가 '설명' 이라는 항목 범위내에 들어가서 마우스 클릭하면 explain 함수로 들어감.

        
        start_screen.fill((255, 255, 255))#이거는 배경화면
        start_screen.blit(title_message_object, title_message_rect)#출력
        start_screen.blit(start_message_object, start_message_rect)#출력
        start_screen.blit(exp_message_object, exp_message_rect)#출력
        pygame.display.update()#업데이트

def sound_track():# 노래 선택 화면
    white = (255,255,255)
    black = (0,0,0)

    screen_width = 400
    screen_height = 500
    size = [screen_width, screen_height]#  사이즈를 400x500으로 지정.

    screen = pygame.display.set_mode(size)# 똑같음.

    font = pygame.font.SysFont("malgungothic", 20, True, True)

    text = font.render("배경음악 선택", True, black)

    button1 = pygame.image.load("1.png")# 이미지 불러오기
    button1 = pygame.transform.scale(button1, (screen_width/2, screen_height/10))#이미지 크기
    button2 = pygame.image.load("2.png")# 이미지 불러오기
    button2 = pygame.transform.scale(button2, (screen_width/2, screen_height/10))#이미지 크기
    
    button1rect = button1.get_rect()#1.png의 위치를 지정함.
    button1rect.x = screen_width/4#위치 설정(가로)
    button1rect.y = screen_height*1/4#(세로)

    button2rect = button2.get_rect()#2,png
    button2rect.x = screen_width/4#가로
    button2rect.y = screen_height*2/4#세로

    
    back = pygame.image.load("triangle.png")
    back_rect = back.get_rect()#back의 우치를 지정할 함수를

    done = False
    clock = pygame.time.Clock()

    while not done:
        clock.tick(10)
        screen.fill(white)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                # 화면 x를 누르면 다시 메인메뉴로 넘어감.
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pygame.mouse.get_rel()
                mouse_pos = pygame.mouse.get_pos()
                if mouse_pos[0] > button1rect.left and mouse_pos[0] < button1rect.right and mouse_pos[1] > button1rect.top and mouse_pos[1] < button1rect.bottom:
                    game_start("Bee.mp3", 220)#뮤직 이름, 타임
                if mouse_pos[0] > button2rect.left and mouse_pos[0] < button2rect.right and mouse_pos[1] > button2rect.top and mouse_pos[1] < button2rect.bottom:
                    game_start("HER.mp3", 180)#뮤직 이름, 타임
                if mouse_pos[0] > back_rect.left and mouse_pos[0] < back_rect.right and mouse_pos[1] > back_rect.top and mouse_pos[1] < back_rect.bottom:
                    game()
        
        screen.blit(text, (screen_width/3, screen_height/100))
        screen.blit(button1, (screen_width/4, screen_height*1/4))#button1 의 위치를 정해주고 출력.
        screen.blit(button2, (screen_width/4, screen_height*2/4))#button2의 위치를 설정, 출력.
        screen.blit(back, (0,0))#back의 위치를 전해주고 출력함. 
        pygame.display.update()

def explain():# 설명을 위한 화면
    white = (255,255,255)
    black = (0,0,0)

    screen_width = 400
    screen_height = 500
    size = [screen_width, screen_height]

    screen = pygame.display.set_mode(size)


    font = pygame.font.SysFont("malgungothic", 20, True, True)# 텍스트 기울이기를 True(2)로, malgungothic 이라는 폰트를 불러와서 True(1)로. 

    text = font.render("게임 플레이 방법", True, black)# 텍스트 색상 지정. 그리고 True를 해줌으로써 검은색으로 지정.

    back = pygame.image.load("triangle.png")
    back_rect = back.get_rect()

    explain = pygame.image.load("explain.png")
    explain = pygame.transform.scale(explain,(screen_width, screen_height*9/10))

    done = False
    clock = pygame.time.Clock()

    while not done:# false 가 아닌 True로.
        clock.tick(10)# 프레임 레이트 지정.
        screen.fill(white)# 화면을 화이트로 지정.
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.mouse.get_rel()#마우스의 위치를 받음
                mouse_pos = pygame.mouse.get_pos()#그 다음 pos에 저장하고 그걸 또 mouse_pos라고 함. 그 다음 줄에서 만약에 pos가 그 위치에 있으면 그 함수로 감.
                if mouse_pos[0] > back_rect.left and mouse_pos[0] < back_rect.right and mouse_pos[1] > back_rect.top and mouse_pos[1] < back_rect.bottom:
                    game()#똑같음.
            
        screen.blit(text, (screen_width/3,screen_height/100))#'게임 플레이 방법'의 위치를 설정함.
        screen.blit(back, (0,0))#'triangle' 의 위치를 설정. 하지만 맨 윗칸에 있어야 하기 때문에 0,0으로.
        screen.blit(explain, (0, screen_height/10))#width에서 더 추가하면 이상해짐. 그래서 0으로 두고, 높이만 살짝 조작.
        pygame.display.update()#화면 새로고침

def game_start(music, music_time):# 게임 시작
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
    tiles = []# 타일의 색상을 정해주기 전, 빈칸, 또는 문자, 숫자로 하면 안됨.
    speed = 5
    score = 0


    # score 확인
    
    def display_score():
        score_text = font.render(f"점수: {score}", True, white)
        screen.blit(score_text, (10, 10)) #점수 항목을 10,10위 위치로 변경.

    # line
    line_width = 100 # 라인의 크기를 말하는거.그리고 4등분해서 출력함.(Line 255)
    line_height = 20 # 높이

    q = pygame.image.load("line.png")
    q = pygame.transform.scale(q,(line_width-4, line_height))
    q_rect = q.get_rect()#위치를 정해줌.
    q_rect.x = 2# q버튼의 위치를 정해줌
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
            tile.move_ip(0, speed)# x,y 축으로 얼마나 움직일꺼냐.
            #y축은 speed(5) 만큼

    def remove_tiles():
        for tile, _ in tiles:
            if tile.top > screen_height:# 만약 타일을 치지 않고 바닥에 닿으면 타일이 없어진다.
                
                tiles.remove((tile, _))#ip.move 함수는 for 루프에서 큐플의 구조를 만족시켜야함. 하지만 그 값을 사용하지 않는다고 해서 _를 빼면 안됨. 
                #그래서 ,_ 를 해줌으로써 그 값을 사용하지 않겠다는 것을 나타냄.
                # 그런데 _에 원래 들어가야할 항목은 

                
    # BPM 에 맞게 박자 간격 설정
    bpm = 324# 왜??
    beat_interval = 1 / (bpm/60) # 밀리초 단위
    next_beat_time = time.time() + beat_interval # 음악 시작 타이밍

    tile_num = music_time * bpm/60# 타일의 개수가 음악의 시간에 비례함.

    running = True
    pygame.mixer.music.load( music )#music 을 불러옴

    pygame.mixer.music.play()#재생

    current_time = 0
    start_time = time.time()
    
    while running and music_time>=current_time - start_time:
        
        screen.fill(black)
        
        current_time = time.time()#지금 노래가 실행된 시간
        
        if current_time >= next_beat_time: #노래의 남은 시간이 아직 있다면
            
            create_tile()
            next_beat_time += beat_interval

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False #x 표시를 누른다면 중단함.
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
                            tiles.remove((tile))# q,w,e,r 의 타일을 누를때 점수가 오름.
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.mouse.get_rel()
                mouse_pos = pygame.mouse.get_pos()
                if mouse_pos[0] > home_rect.left and mouse_pos[0] < home_rect.right and mouse_pos[1] > home_rect.top and mouse_pos[1] < home_rect.bottom:
                    pygame.mixer.music.pause()
                    game() # 만약 마우스의 위치가 홈으로 되어있다면 홈으로 돌아감.
            

        move_tiles()
        remove_tiles()
        display_score()

        for tile, color in tiles:
            pygame.draw.rect(screen, color, tile)
        
        screen.blit(q, (2, screen_height - line_height*3)) #높이는 쪽같고, q,w,e,r에 대한 라인의 위치를 맞춘다.
        screen.blit(w, (line_width + 2, screen_height - line_height*3))
        screen.blit(e, (line_width * 2 + 2, screen_height - line_height*3))
        screen.blit(r, (line_width * 3 + 2,  screen_height - line_height*3))
        screen.blit(home, (screen_width - 50, 0))#홈의 위치

        pygame.display.flip()#update와 똑같이 새로고침 함.
        clock.tick(60) # 60프레임


    pygame.mixer.music.pause()#음악이 끝나면 점수 화면으로.
    game_score(tile_num, score)

def game_score(tile_num, score):# 게임 점수

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