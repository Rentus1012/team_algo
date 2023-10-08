import pygame, sys
from pygame.locals import*
import random
from mutagen.mp3 import MP3
#audio = MP3("Bee.mp3")
#print(audio.info.length)

pygame.init()

title = "Piano Game"
pygame.display.set_caption(title)

#시작화면 만들기
def game():
    size = (400, 500)
    start_screen = pygame.display.set_mode(size)
    
    pygame.font.init()
    title_font = pygame.font.SysFont('Sans', 40, True, False)
    title_message = "Piano Game."
    title_message_object = title_font.render(title_message, True, (0, 0, 0))
    title_message_rect = title_message_object.get_rect()
    title_message_rect.center = (250, 100)
    
    pygame.font.init()
    sub_font = pygame.font.SysFont('malgungothic', 20, False, False)
    start_message = "게임시작"
    start_message_object = sub_font.render(start_message, True, (0, 0, 0))
    start_message_rect = start_message_object.get_rect()
    start_message_rect.center = (250, 250)
    
    exp_message = "설명"
    exp_message_object = sub_font.render(exp_message, True, (0, 0, 0))
    exp_message_rect = exp_message_object.get_rect()
    exp_message_rect.center = (250, 300)
    
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
    button2 = pygame.image.load("2.png")

    button1rect = button1.get_rect()
    button2rect = button2.get_rect()
    button1rect.x = screen_width/5
    button1rect.y = screen_height/3
    button2rect.x = screen_width/5
    button2rect.y = screen_height*2/3

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
                    game_start("Bee.mp3")
                if mouse_pos[0] > button2rect.left and mouse_pos[0] < button2rect.right and mouse_pos[1] > button2rect.top and mouse_pos[1] < button2rect.bottom:
                    print("button2 클릭")
        
        
        screen.blit(text, (screen_width/3, screen_height/100))
        screen.blit(button1, (screen_width/5, screen_height*1/3))
        screen.blit(button2, (screen_width/5, screen_height*2/3))
        pygame.display.update()



def game_start(music):
    # 화면 설정
    screen_width, screen_height = 400, 500
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("피아노 띵동띵동")

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

    # 화면을 4개의 세로 등분된 화면으로 나눔
    line_x_coordinates = [i * (screen_width // 4) for i in range(4)]  # 4개의 세로선


    # BPM 162에 맞게 박자 간격 설정
    bpm = 162
    beat_interval = int((60 / bpm) * 1000)  # 밀리초 단위

    next_beat_time = pygame.time.get_ticks() + beat_interval

    def create_tile():
        x = random.choice(line_x_coordinates)
        y = 0
        color = (255, 255, 255)
        tile = pygame.Rect(x, y, tile_width, tile_height)
        tiles.append((tile, color))

    def move_tiles():
        for tile, _ in tiles:
            tile.move_ip(0, speed)

    def remove_tiles():
        global score
        for tile, _ in tiles:
            if tile.top > screen_height:
                tiles.remove((tile, _))

    running = True
    pygame.mixer.music.load( music )
    pygame.mixer.music.play()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        current_time = pygame.time.get_ticks()
        if current_time >= next_beat_time:
            create_tile()
            next_beat_time += beat_interval

        move_tiles()
        remove_tiles()

        screen.fill(black)
        for tile, color in tiles:
            pygame.draw.rect(screen, color, tile)
        
        pygame.display.flip()

        clock.tick(60)



game()