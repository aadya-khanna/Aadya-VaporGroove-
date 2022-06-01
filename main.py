import pygame
import random
import time

from playsound import playsound

pygame.init()

# my variables being defined
screen = pygame.display.set_mode([875, 900])

quality = ""

start = 0

score = 0

quality_cords = [120,240,460,680]

spawncords = [180,400,620,840]

position_praise = 400

image_up = pygame.image.load("/Users/aadya/Desktop/Code/python/rg/button1.png")
image_down = pygame.image.load("/Users/aadya/Desktop/Code/python/rg/button3.png")
image_right = pygame.image.load("/Users/aadya/Desktop/Code/python/rg/button2.png")
image_left = pygame.image.load("/Users/aadya/Desktop/Code/python/rg/button4.png")

image_bg = pygame.image.load("/Users/aadya/Desktop/Code/python/rg/bg.png")

image_ball = pygame.image.load("ball.png")

imagerect_up = image_up.get_rect()
imagerect_down = image_down.get_rect()
imagerect_right = image_right.get_rect()
imagerect_left = image_left.get_rect()

imagerect_up.right = 210
imagerect_up.top = 570

imagerect_down.right = 430
imagerect_down.top = 570

imagerect_right.right = 650
imagerect_right.top = 570

imagerect_left.right = 870
imagerect_left.top = 570


pygame.mixer.music.load("track"+ str(random.randint(1,5))+ ".mp3")

difficultyspeed = 1

myfont = pygame.font.SysFont("Cookies", 85)

# defining functions

def game_menu():

    pygame.display.set_caption('POPstefanija')
    pygame.display.flip()

def spawn_ball():
    global imagerect_ball
    imagerect_ball = image_ball.get_rect()
    imagerect_ball.right = random.choice(spawncords)
    imagerect_ball.top = 100

running = True

spawn_ball()
game_menu()

#game loop


pygame.mixer.music.play(loops = -1)

while running:
    screen.blit(image_bg, (0, 0))

    screen.blit(image_up, imagerect_up)
    screen.blit(image_down, imagerect_down)
    screen.blit(image_right, imagerect_right)
    screen.blit(image_left, imagerect_left)

    streak = myfont.render("streak: " + str(score) + "!",1, (176,67,33))
    screen.blit(streak,(0,0))

    praises = myfont.render( quality ,1, (176,67,33))
    screen.blit(praises,(position_praise,120))

    #pygame.mixer.Sound("/Users/aadya/Desktop/theme.mp3").play()
    #pygame

    try:
        imagerect_ball = imagerect_ball.move(0,difficultyspeed)
        screen.blit(image_ball, imagerect_ball)
    except:
        pass

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Whenever a key is pressed down
        elif event.type == pygame.KEYDOWN:

            pygame.mixer.Sound("/Users/aadya/Desktop/Code/python/rg/pop.mp3").play()
            pygame
            position_praise = random.choice(quality_cords)

            start = time.time()
            # W -> Up; S -> Down; A -> Left; D -> Right
            if (event.key == pygame.K_UP or event.key == ord('w')) and imagerect_ball.right == 180:
                if imagerect_ball.bottom > 590 and imagerect_ball.bottom < 760:
                    imagerect_ball = None
                    quality = ("good!")
                    difficultyspeed += 0.5
                    score = score + 1
                else:
                    imagerect_ball = None
                    print("Bad!")
                    quality = ("bad!")
                    score = 0
                print("Streak:", score)
                spawn_ball()

            if (event.key == pygame.K_DOWN or event.key == ord('s')) and imagerect_ball.right == 400:
                if imagerect_ball.bottom > 590 and imagerect_ball.bottom < 760:
                    imagerect_ball = None
                    quality = ("good!")
                    difficultyspeed += 0.5
                    score = score + 1
                else:
                    imagerect_ball = None
                    quality = ("bad!")
                    difficultyspeed = 1
                    score = 0

                print("Streak:", score)
                spawn_ball()

            if (event.key == pygame.K_RIGHT or event.key == ord('d')) and imagerect_ball.right == 620:
                if imagerect_ball.bottom > 590 and imagerect_ball.bottom < 760:
                    imagerect_ball = None
                    quality = ("good!")
                    difficultyspeed += 0.5
                    score = score + 1
                else:
                    imagerect_ball = None
                    quality = ("bad!")
                    difficultyspeed = 1
                    score = 0
                print("Streak:", score)
                spawn_ball()

            if (event.key == pygame.K_LEFT or event.key == ord('a')) and imagerect_ball.right == 840:
                if imagerect_ball.bottom > 590 and imagerect_ball.bottom < 760:
                    imagerect_ball = None
                    quality = ("good!")
                    difficultyspeed += 0.5
                    score = score + 1
                else:
                    imagerect_ball = None
                    quality = ("bad!")
                    difficultyspeed = 1
                    score = 0
                print("Streak:", score)
                spawn_ball()

            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    if time.time() - start >= 0.2:
        quality = ""
    pygame.display.update()


    if imagerect_ball.top > 900:
        pygame.quit()
        print ("GAME OVER!")
        break

#end of while loop

#end of code
