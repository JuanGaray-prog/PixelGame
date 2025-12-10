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

#light blue
light_blue = (168,210,62)
Blue1 = (10, 10, 80)
Blue2 = (30, 30, 100)

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

#Import Images players
# 1.head
img_head = pygame.image.load("Head.png").convert_alpha()
img_head = pygame.transform.scale(img_head, (cells_size, cells_size))
img_head1 = pygame.image.load("Head_red.png").convert_alpha()
img_head1 = pygame.transform.scale(img_head1, (cells_size, cells_size))

# 2.body
img_body = pygame.image.load("Body.jpg").convert_alpha()
img_body = pygame.transform.scale(img_body, (cells_size, cells_size))
img_body1 = pygame.image.load("Body_red.jpg").convert_alpha()
img_body1 = pygame.transform.scale(img_body1, (cells_size, cells_size))

# 3.body curve
img_corner = pygame.image.load("Body_curve.png").convert_alpha()
img_corner = pygame.transform.scale(img_corner, (cells_size, cells_size))
img_corner1 = pygame.image.load("Body_curve_red.png").convert_alpha()
img_corner1 = pygame.transform.scale(img_corner1, (cells_size, cells_size))

# 4.tail
img_tail = pygame.image.load("Tail.png").convert_alpha()
img_tail = pygame.transform.scale(img_tail, (cells_size, cells_size))
img_tail1 = pygame.image.load("Tail_red.png").convert_alpha()
img_tail1 = pygame.transform.scale(img_tail1, (cells_size, cells_size))

# Import images (Menú y Manzana)
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

def draw_snake(surface, snake_list, img_head, img_body, img_corner, img_tail):
    if len(snake_list) < 2:
        return

    def get_vector(b_origin, b_destination):
        dx = b_destination[0] - b_origin[0]
        dy = b_destination[1] - b_origin[1]
        
        if dx > cells_size: dx = -cells_size
        elif dx < -cells_size: dx = cells_size
        if dy > cells_size: dy = -cells_size
        elif dy < -cells_size: dy = cells_size
        return dx, dy

    for index, block in enumerate(snake_list):
        x = block[0]
        y = block[1]
        block_rect = pygame.Rect(x, y, cells_size, cells_size)

        # 1. head(Último elemento)
        if index == len(snake_list) - 1:
            prev_block = snake_list[index - 1]
            dx, dy = get_vector(prev_block, block)

            if dx > 0:   img = pygame.transform.rotate(img_head, 90)  
            elif dx < 0: img = pygame.transform.rotate(img_head, 270) 
            elif dy > 0: img = pygame.transform.rotate(img_head, 0)
            elif dy < 0: img = pygame.transform.rotate(img_head, 180)  
            else: img = img_head        
            surface.blit(img, block_rect)

        # 2. tail (Primer elemento)
        elif index == 0:
            next_block = snake_list[index + 1] 
            dx, dy = get_vector(block, next_block) 

            if dx > 0: img = pygame.transform.rotate(img_tail, 180) 
            elif dx < 0: img = pygame.transform.rotate(img_tail, 0)   
            elif dy > 0: img = pygame.transform.rotate(img_tail, 90) 
            elif dy < 0: img = pygame.transform.rotate(img_tail, 270)  
            else: img = img_tail         
            surface.blit(img, block_rect)

        #3. body and corner
        else:
            prev_block = snake_list[index - 1]
            next_block = snake_list[index + 1]          
            
            #vector
            dx_prev, dy_prev = get_vector(block, prev_block)
            dx_next, dy_next = get_vector(block, next_block)
            #1. horizontal straight line
            if dx_prev != 0 and dx_next != 0:
                surface.blit(img_body, block_rect)
            
            #2. vertical straight line
            elif dy_prev != 0 and dy_next != 0:
                surface.blit(pygame.transform.rotate(img_body, 90), block_rect)

            # corner
            else:
                # From LEFT to UP (or UP to LEFT)
                if (dx_prev == -cells_size and dy_next == -cells_size) or (dx_next == -cells_size and dy_prev == -cells_size):
                    surface.blit(pygame.transform.rotate(img_corner, 180), block_rect)
                # From LEFT to DOWN (or DOWN to LEFT)
                elif (dx_prev == -cells_size and dy_next == cells_size) or (dx_next == -cells_size and dy_prev == cells_size):
                    surface.blit(pygame.transform.rotate(img_corner, 270), block_rect)
                # From RIGHT to UP (or UP to RIGHT)
                elif (dx_prev == cells_size and dy_next == -cells_size) or (dx_next == cells_size and dy_prev == -cells_size):
                    surface.blit(pygame.transform.rotate(img_corner, 90), block_rect)
                # From RIGHT to DOWN (or DOWN to RIGHT)
                elif (dx_prev == cells_size and dy_next == cells_size) or (dx_next == cells_size and dy_prev == cells_size):
                    surface.blit(pygame.transform.rotate(img_corner, 0), block_rect)

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

        screen.fill((Blue1))

        for rows in range(cells_number):
            if not rows%2:
                for columns in range(cells_number):
                    if not columns%2:
                        pasto_rect = pygame.Rect(columns * cells_size, rows*cells_size, cells_size, cells_size)
                        pygame.draw.rect(screen, Blue2, pasto_rect)
            else:
                for columns in range(cells_number):
                    if columns%2:
                        pasto_rect = pygame.Rect(columns * cells_size, rows*cells_size, cells_size, cells_size)
                        pygame.draw.rect(screen, Blue2, pasto_rect)                    

        #draw player 1
        draw_snake(screen, snake, img_head, img_body, img_corner, img_tail)

        #draw player 2
        draw_snake(screen, snake1, img_head1, img_body1, img_corner1, img_tail1)


        #Apple
        if x == apx and y == apy:
            apx, apy = apple_position()
            score_player1 += 1
            tick += 1
        elif x1 == apx and y1 == apy:
            apx, apy = apple_position()
            score_player2 += 1
            tick += 1
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
        #message win
        win_text = game_font.render("¡Jugador 1!", True, (0, 255, 0)) 
        #center text
        win_text_rect = win_text.get_rect(center = (cells_size*cells_number//2, cells_size*cells_number//1.1))
        screen.blit(win_text, win_text_rect)
    
    elif gamestate == "win_player2":
        screen.fill("black")
        screen.blit(winner_screen, winner_screen_rect)
        #message win
        win_text = game_font.render("¡Jugador 2!", True, (255, 0, 0)) 
        #center text
        win_text_rect = win_text.get_rect(center = (cells_size*cells_number//2, cells_size*cells_number//1.1))
        screen.blit(win_text, win_text_rect)

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


