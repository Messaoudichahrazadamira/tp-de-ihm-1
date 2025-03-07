
import pygame
import time
import random


pygame.init()


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
OUTER_COLOR = (50, 50, 50)
python_orange = (255, 102, 0) 
green_color = (51, 140, 0) 
DARK_GRAY = (30, 30, 30)
DARK_GRAY_2 = (56, 56, 56) 
LIGHT_GRAY = (200, 200, 200)


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 440
FRAME_WIDTH = 600
FRAME_HEIGHT = 400
FRAME_X = 0
FRAME_Y = 40
GRID_SIZE = 20



square_x = 0
square_y = 0
square_width = 600
square_height = 40



# font_style = pygame.font.Font("LilitaOne-Regular.ttf", 40)  
font_style = pygame.font.Font("LilitaOne-Regular.ttf", 40)  
score_font= pygame.font.Font("LilitaOne-Regular.ttf", 25) 


font_path = "LilitaOne-Regular.ttf"  
font_large = pygame.font.Font(font_path, 50)
font_medium = pygame.font.Font(font_path, 35)


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake Game')


clock = pygame.time.Clock()



def display_score(score):
    score_text = "Score: " + str(score)
    
    
    button_x = FRAME_X + 10
    button_y = FRAME_Y - 38
    button_width = 200
    button_height = 36

    
    
    draw_button(score_text, button_x, button_y, button_width, button_height, WHITE, (255, 255, 255))

def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.circle(screen, python_orange, (x[0] + snake_block // 2, x[1] + snake_block // 2), snake_block // 2)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [FRAME_X + 200, FRAME_Y + 100])  
    
def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))    

def draw_button(text, x, y, width, height, color, hover_color, border_radius=20):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(screen, hover_color, (x, y, width, height), border_radius=border_radius)  
        if click[0] == 1:  
            return True
    else:
        pygame.draw.rect(screen, color, (x, y, width, height), border_radius=border_radius)  

    
    font= pygame.font.Font("LilitaOne-Regular.ttf", 25) 
    text_surface = font.render(text, True, BLACK)
    screen.blit(text_surface, (x + (width - text_surface.get_width()) // 2, y + (height - text_surface.get_height()) // 2))
    
    return False



def game_loop():
    game_over = False
    game_close = False

    x1 = FRAME_X + FRAME_WIDTH / 2
    y1 = FRAME_Y + FRAME_HEIGHT / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(FRAME_X, FRAME_X + FRAME_WIDTH - GRID_SIZE) / GRID_SIZE) * GRID_SIZE
    foody = round(random.randrange(FRAME_Y, FRAME_Y + FRAME_HEIGHT - GRID_SIZE) / GRID_SIZE) * GRID_SIZE

    while not game_over:

        while game_close == True:
            screen.fill(DARK_GRAY_2)
            pygame.draw.rect(screen, DARK_GRAY, (FRAME_X, FRAME_Y, FRAME_WIDTH, FRAME_HEIGHT))
            message("game over", RED)
            if draw_button("play again", FRAME_X + 50, FRAME_Y + 200, 200, 50, WHITE, (0, 200, 0)):
                game_loop()  
            if draw_button("close", FRAME_X + 350, FRAME_Y + 200, 200, 50, WHITE, (200, 0, 0)):
                pygame.quit()  
                game_over = True 

            display_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -GRID_SIZE
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = GRID_SIZE
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -GRID_SIZE
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = GRID_SIZE
                    x1_change = 0
        
        x1 += x1_change
        y1 += y1_change

        if x1 < FRAME_X or x1 >= FRAME_X + FRAME_WIDTH or y1 < FRAME_Y or y1 >= FRAME_Y + FRAME_HEIGHT:
            snake_list.clear()
            game_close = True  

        pygame.draw.rect(screen, DARK_GRAY, (FRAME_X, FRAME_Y, FRAME_WIDTH, FRAME_HEIGHT))
        pygame.draw.rect(screen, BLACK, (FRAME_X, FRAME_Y, FRAME_WIDTH, FRAME_HEIGHT), 1)
        pygame.draw.circle(screen, green_color, (foodx + GRID_SIZE // 2, foody + GRID_SIZE // 2), GRID_SIZE // 2)

        snake_head = [x1, y1]
        snake_list.append(snake_head)
        
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(GRID_SIZE, snake_list)
        pygame.draw.rect(screen, DARK_GRAY_2, (square_x, square_y, square_width, square_height))

        display_score(length_of_snake - 1)
        pygame.display.update()

        if abs(x1 - foodx) < GRID_SIZE and abs(y1 - foody) < GRID_SIZE:
            foodx = round(random.randrange(FRAME_X, FRAME_X + FRAME_WIDTH - GRID_SIZE) / GRID_SIZE) * GRID_SIZE
            foody = round(random.randrange(FRAME_Y, FRAME_Y + FRAME_HEIGHT - GRID_SIZE) / GRID_SIZE) * GRID_SIZE
            length_of_snake += 1

        clock.tick(7)
        screen.fill(OUTER_COLOR)

    pygame.quit()
    quit()
    



def main_menu():
    running = True  
    small_image = pygame.image.load("small_image.png")
    small_image = pygame.transform.scale(small_image, (226, 111.25)) 

    while running:
        screen.fill(DARK_GRAY_2)

        
        draw_text("Snake Game", font_large, WHITE, SCREEN_WIDTH // 2 - 130, 50)

        if draw_button("New Game", 200, 130, 200, 50, LIGHT_GRAY, GREEN):
            running = False 
            game_loop() 
        if draw_button("Exit", 200, 200, 200, 50, LIGHT_GRAY, RED):
            pygame.quit()   
            sys.exit()
            
        small_image_rect = small_image.get_rect(center=(SCREEN_WIDTH // 2, 320))  
        screen.blit(small_image, small_image_rect)
            
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main_menu() 
    game_loop()  