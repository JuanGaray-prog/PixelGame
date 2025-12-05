import pygame, random

#function to get score
def score(score1, score2):
    score = game_font.render(f"Player 1: {score1}", True, "white")
    score_rect = score.get_rect(topleft = (0,0))
    screen.blit(score, (0,0))
    score_p2 = game_font.render(f"Player 2: {score2}", True, "white")
    score_rect = score_p2.get_rect(topright = (cells_size*cells_number,0))
    screen.blit(score_p2, score_rect)

#GRID
cells_size = 40
cells_number = 20
tick=5
pygame.init()
screen = pygame.display.set_mode((cells_size*cells_number,cells_size*cells_number))
pygame.display.set_caption("Game Name")
clock = pygame.time.Clock()

#light green
light_green = (168,210,62)

#Player Position
number_x = random.randint(1,cells_number-1)
number_y = random.randint(1,cells_number-1)

number_x1 = random.randint(1,cells_number-1)
number_y1 = random.randint(1,cells_number-1)

if number_x == number_x1:
    number_x1 += 1

x = number_x *cells_size
y = number_y *cells_size

x1 = number_x1 *cells_size
y1 = number_y1 *cells_size

#Apple Position and Logic
def apple_position():
    apple_x = random.randint(1,cells_number-1)
    apple_y = random.randint(1,cells_number-1)

    apx = apple_x * cells_size
    apy = apple_y * cells_size
    return apx, apy

apx, apy = apple_position()

#Font
game_font = pygame.font.Font(None, 60)
score_player1 = 0
score_player2 = 0

#Import images
winner_screen = pygame.image.load("Winner.png").convert_alpha()
winner_screen = pygame.transform.scale(winner_screen, (cells_size*cells_number, cells_size*cells_number))
winner_screen_rect = winner_screen.get_rect(center = (cells_size*cells_number//2, cells_size*cells_number//2))

apple = pygame.image.load("Manzana.png").convert_alpha()
apple_screen = pygame.transform.scale(apple, (cells_size,cells_size))

menu = pygame.image.load("Menu.png").convert_alpha()
menu_screen = pygame.transform.scale(menu, (cells_size*cells_number, cells_size*cells_number))
menu_rect = menu_screen.get_rect(center = (cells_size*cells_number//2, cells_size*cells_number//2))

play = pygame.image.load("Play.png").convert_alpha()
play = pygame.transform.scale(play, (cells_size*10, cells_size*3))
play_rect = play.get_rect(center = (cells_size*cells_number//2, cells_size*cells_number//2.5))

exit = pygame.image.load("Salir.png")
exit = pygame.transform.scale(exit, (cells_size*10, cells_size*3))
exit_rect = exit.get_rect(center = (cells_size*cells_number//2, cells_size*cells_number//1.5))

#Difficulty
easy = pygame.image.load("Easy.jpeg").convert_alpha()
easy = pygame.transform.scale(easy, (cells_size*10, cells_size*3))
easy_rect = easy.get_rect(center = (cells_size*cells_number//2, cells_size*cells_number//3))

medium = pygame.image.load("Medium.jpeg").convert_alpha()
medium = pygame.transform.scale(medium, (cells_size*10, cells_size*3))
medium_rect = medium.get_rect(center = (cells_size*cells_number//2, cells_size*cells_number//2.0))

hard = pygame.image.load("Hard.jpeg").convert_alpha()
hard = pygame.transform.scale(hard,(cells_size*10, cells_size*3))
hard_rect = hard.get_rect(center = (cells_size*cells_number//2, cells_size*cells_number//1.5))

    

running = True

#Desplazamiento
x_movement = 0
y_movement = 0
x1_movement = 0
y1_movement = 0

#Timming
#timer_1 = pygame.USEREVENT
#pygame.time.set_timer(timer_1,300)
#start_time = pygame.time.get_ticks()

#GameStates
menu = True
gamestate = "" 

#Snake Body
snake = [[x,y]]
snake1 = [[x1,y1]]

while running:
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if menu:
            screen.blit(menu_screen, menu_rect)
            screen.blit(play, play_rect)
            screen.blit(exit, exit_rect)

            if event.type == pygame.MOUSEBUTTONUP:
                if play_rect.collidepoint(mouse_pos):
                    menu = False
                    gamestate = "option"
                    
                if exit_rect.collidepoint(mouse_pos):
                    running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y_movement = 0
                y_movement = -1
                x_movement = 0
            if event.key == pygame.K_DOWN:
                y_movement = 0
                y_movement = 1
                x_movement = 0
            if event.key == pygame.K_LEFT:
                x_movement = 0
                x_movement = -1
                y_movement = 0
            if event.key == pygame.K_RIGHT:
                x_movement = 0
                x_movement = 1
                y_movement = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                y1_movement = 0
                y1_movement = -1
                x1_movement = 0
            if event.key == pygame.K_s:
                y1_movement = 0
                y1_movement = 1
                x1_movement = 0
            if event.key == pygame.K_a:
                x1_movement = 0
                x1_movement = -1
                y1_movement = 0
            if event.key == pygame.K_d:
                x1_movement = 0
                x1_movement = 1
                y1_movement = 0


    if gamestate == "running":
        number_x += x_movement
        number_y += y_movement

        if number_x < 0:
            number_x = 20
        elif number_x > 20:
            number_x = 0
        if number_y < 0:
            number_y = 20   
        elif number_y > 20:
            number_y = 0

        x = number_x*cells_size
        y = number_y*cells_size


        number_x1 += x1_movement
        number_y1 += y1_movement
        
        if number_x1 < 0:
            number_x1 = 20
        elif number_x1 > 20:
            number_x1 = 0
        if number_y1 < 0:
            number_y1 = 20
        elif number_y1 > 20:
            number_y1 = 0

        x1= number_x1 *cells_size
        y1= number_y1 *cells_size
        
        snake1.append([x1,y1])
        snake.append([x,y])

        screen.fill((20, 230, 70))

        for rows in range(cells_number):
            if not rows%2:
                for columns in range(cells_number):
                    if not columns%2:
                        pasto_rect = pygame.Rect(columns * cells_size, rows*cells_size, cells_size, cells_size)
                        pygame.draw.rect(screen, "green", pasto_rect)
            else:
                for columns in range(cells_number):
                    if columns%2:
                        pasto_rect = pygame.Rect(columns * cells_size, rows*cells_size, cells_size, cells_size)
                        pygame.draw.rect(screen, "green", pasto_rect)                    


        #PLAYER 1
        for segmento in snake:
            pygame.draw.rect(screen, "blue", (segmento[0], segmento[1], cells_size, cells_size))
        #PLAYER 2
        for segmento in snake1:
            pygame.draw.rect(screen, "red", (segmento[0],segmento[1], cells_size, cells_size))

        #Apple
        if x == apx and y == apy:
            apx, apy = apple_position()
            score_player1 += 1
        elif x1 == apx and y1 == apy:
            apx, apy = apple_position()
            score_player2 += 1
        else:
            apple_rect = apple_screen.get_rect(topleft = (apx, apy))
            screen.blit(apple_screen,apple_rect)

        if len(snake) > score_player1+1:
            del snake[0]
        if len(snake1) > score_player2+1:
            del snake1[0]

        #Score
        score(score_player1, score_player2)

        if score_player1 == 5:
            gamestate = "win_player1"
        elif score_player2 == 5:
            gamestate = "win_player2"

    elif gamestate == "win_player1":
        screen.fill("black")
        screen.blit(winner_screen, winner_screen_rect)
    
    elif gamestate == "win_player2":
        screen.fill("black")
        screen.blit(winner_screen, winner_screen_rect)

    elif gamestate == "option":

        screen.blit(menu_screen, menu_rect)
        screen.blit(easy, easy_rect)
        screen.blit(medium, medium_rect)
        screen.blit(hard, hard_rect)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if easy_rect.collidepoint(mouse_pos):
                tick = 5
                gamestate = "running"

            elif medium_rect.collidepoint(mouse_pos):
                tick = 10
                gamestate = "running"
                
            elif hard_rect.collidepoint(mouse_pos):
                tick = 15
                gamestate = "running"

    pygame.display.update()
    clock.tick(tick)

