import pygame
import random
from colors import *
from screen import *
pygame.init()






clock = pygame.time.Clock()

font = pygame.font.SysFont(None,55)

def text_screen(text,color,x,y):
    screen_text = font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])

#### snake length
def plot_snake(gameWindow,color,snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x,y, snake_size, snake_size])



## Game Loop  game runs in the game loop, every events occurs here.
def gameloop():
    exit_game = False  ## exit_game remains false until user presses a button to exit.
    game_over = False  ### game_over remains false until snake crashes.
    snake_x = 45  ## x position of the snake
    snake_y = 55  #### y position of the snake
    velocity_x = 0  ### velocity at x direction of the snake
    velocity_y = 0  ### velocity at y direction of the snake

    snk_list = []
    snk_length = 1

    innit_velocity = 5
    snake_size = 10  ### size of the snake
    fps = 30  ### frame per second of the screen
    ###### creating food
    food_x = random.randint(20, screenWidth / 2)
    food_y = random.randint(20, screenHeight / 2)
    appleSize = 10
    score = 0

    while not exit_game:
        if game_over:
            gameWindow.fill(white)
            text_screen("Game Over !!! Press enter to continue",black,100,200)

            for event in pygame.event.get(): #### event stores all the possible events.
                if event.type == pygame.QUIT:  ### pressing the exit button.
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN: ### entering 'Return' key
                        gameloop()
        else:
            for event in pygame.event.get(): #### event stores all the possible events.
                if event.type == pygame.QUIT:  ### pressing the exit button.
                    exit_game = True

                if event.type == pygame.KEYDOWN: ### if the key is pressed
                    if event.key == pygame.K_RIGHT: ### if the key is right key
                        velocity_x = innit_velocity
                        velocity_y = 0
                    elif event.key == pygame.K_LEFT:
                        velocity_x = -innit_velocity
                        velocity_y = 0
                    elif event.key == pygame.K_UP:
                        velocity_y = -innit_velocity
                        velocity_x = 0
                    elif event.key == pygame.K_DOWN:
                        velocity_y = innit_velocity
                        velocity_x = 0
            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y
            if abs(snake_x - food_x) < 6 and abs(snake_y - food_y) < 6 : ### game over when crashes at the borders
                score += 1
                food_x = random.randint(20, screenWidth / 2)
                food_y = random.randint(20, screenHeight / 2)
                snk_length += 5



            gameWindow.fill(white)

            pygame.draw.rect(gameWindow, red, [food_x, food_y, appleSize, appleSize]) ### creating an apple !!!

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list) > snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True

            if snake_x < 0 or snake_x > screenWidth or snake_y < 0 or snake_y > screenHeight:
                game_over = True
                print("Game Over")
           ### pygame.draw.rect(gameWindow,green,[snake_x,snake_y,snake_size,snake_size]) ### creating a snake !!!
            plot_snake(gameWindow,green,snk_list,snake_size)
        pygame.display.update()

        clock.tick(fps)

        pygame.display.set_caption(f"Snake game score:  {score}") ### Build in function of pygame, giving a title to the screen.
        pygame.display.update()

    pygame.quit()
    quit()

gameloop()