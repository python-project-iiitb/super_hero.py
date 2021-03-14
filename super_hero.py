import pygame
import math
import functions

class super_hero:
    def __init__(self):

        # initialising pygame
        pygame.init()                                
        pygame.display.set_caption("SUPER HERO")

        # displaying the screen
        self.screen = pygame.display.set_mode((1200, 920))
        self.bg_color = (170, 255, 255)
        self.lost = 0
        self.score = 0
        self.start = 0
    def run_sh(self):
        run = True

        # dictionary of lines containing its coordinates and moving speed
        lines = {
            'l1': [200, 820, 1000, 820, 1, 1], 'l2': [100, 720, 500, 720, 1, 1],
            'l3': [600, 720, 1100, 720, 1, 1], 'l4': [100, 620, 350, 620, 1, 1],
            'l5': [450, 620, 700, 620, 1, 1], 'l6': [800, 620, 1050, 620, 1, 1],
            'p1': [200, 100, 1000, 100, 1, 1], 'p2': [100, 200, 500, 200, 1, 1],
            'p3': [600, 200, 1100, 200, 1, 1], 'p4': [100, 300, 350, 300, 1, 1],
            'p5': [450, 300, 700, 300, 1, 1], 'p6': [800, 300, 1050, 300, 1, 1]
        }

        # dictionary of coins with their coordinates as value to the keys
        coins = {
            'c1': [300, 785], 'c2': [600, 785], 'c3': [900, 785], 'c4': [300, 685], 'c5': [550, 685], 'c6': [800, 685], 'c7': [225, 585], 'c8': [575, 585],
            'c9': [925, 585], 'c10': [300, 65], 'c11': [600, 65], 'c12': [900, 65], 'c13': [300, 165], 'c14': [550, 165], 'c15': [800, 165], 'c16': [225, 265],
            'c17': [575, 265], 'c18': [925, 265], 'c19': [25, 785], 'c20': [1140, 785], 'c21': [1140, 685], 'c22': [27, 705], 'c23': [1140, 165],
            'c24': [30, 165], 'c25': [1140, 65], 'c26': [25, 65]
        }

        # loading all the required images(superhero,dragon,fire,cactus,coin)
        sh_img = pygame.image.load("sh2.png")
        drg_img = pygame.image.load("dragon.png")
        fire_img = pygame.image.load("fire.png")
        cactus_img = pygame.image.load("cactus.png")
        c_img = pygame.image.load("cn.png")

        # setting the coodinates of all required images and planks
        sh_img_x = 25
        sh_img_y = 880
        sh_img_ch_x = 0
        sh_img_ch_y = 0
        fire_img_x = 1050

        # SCORE
        font = pygame.font.Font('game_over.ttf',65)
        textX = 50
        textY = 35
        def show_score(x, y):
            score = font.render("Score :" + " " + str(self.score), True, (0, 0, 0))
            self.screen.blit(score, (x, y)) 
                   


        # an infinite loop to keep the screeen active
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        sh_img_ch_y = -1
                    if event.key == pygame.K_DOWN:
                        sh_img_ch_y = +1
                    if event.key == pygame.K_LEFT:
                        sh_img_ch_x = -1
                    if event.key == pygame.K_RIGHT:
                        sh_img_ch_x = +1
                if event.type == pygame.KEYUP:
                    if (
                            event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT
                       ):
                        sh_img_ch_x = 0
                        sh_img_ch_y = 0
            self.screen.fill(self.bg_color)

            sh_img_x += sh_img_ch_x
            sh_img_y += sh_img_ch_y
            functions.sh(sh_img_x, sh_img_y, sh_img,self.screen)

            # keeping super_hero within screen limits
            if (sh_img_x <= 0):
                sh_img_x = 0
            elif (sh_img_x >= 1160):
                sh_img_x = 1160
            elif (sh_img_y <= 8):
                sh_img_y = 8
            elif (sh_img_y >= 870):
                sh_img_y = 870

            # losing the game when touched by cactus
            if (functions.cactus_out(sh_img_x,sh_img_y)):
                print("lost")
                self.lost += 1
                run=False
            
            # making all the planks move
            for i in lines.values():
                pygame.draw.line(self.screen, (0, 0, 0), [i[0], i[1]], [i[2], i[3]], 5)
                i[0] += i[4]
                i[2] += i[5]
                if (i[2] == 1200):
                    i[4] = -1
                    i[5] = -1
                if (i[0] == 0):
                    i[4] = 1
                    i[5] = 1

            #collecting coins
            for i in coins.values():
                x = functions.collect(i[0], i[1], sh_img_x, sh_img_y)
                if x:
                    self.score += 1
                    i[0] = 2000
                    i[1] = 2000

            #displaying all coins
            for i in coins.values():
                functions.coin(i[0], i[1], c_img,self.screen)

            # losing the game when touched by planks
            for i in lines.values():
                if functions.line_out(i[0], i[1], i[2], i[3], sh_img_x, sh_img_y):
                    self.lost += 1
                    run=False


            # displaying the images of dragon and cactus
            self.screen.blit(drg_img, (1050, 460))
            self.screen.blit(drg_img, (1050, 360))
            for i in range(0, 920, 40):
                self.screen.blit(cactus_img, (3, i))
                self.screen.blit(cactus_img, (1170, i))

            # fire by dragon
            fire_img_x -= 1
            functions.fire(fire_img_x, 490, fire_img,self.screen)
            functions.fire(fire_img_x, 390, fire_img,self.screen)

            # bringing fire back to the dragon mouth once reaches end of the screen
            if (fire_img_x == 0):
                fire_img_x = 1050

            # losing the game when burnt due to fire    
            if (functions.fire_out(sh_img_x, sh_img_y, fire_img_x, 490)):
                print("you are lost")
                self.lost += 1
                run=False
            if (functions.fire_out(sh_img_x, sh_img_y, fire_img_x, 390)):
                print("you are lost")
                self.lost += 1
                run=False

            # losing the game when super_hero touches dragon    
            if (functions.drag_out(sh_img_x, sh_img_y, 1050, 460) and sh_img_y > 440 and sh_img_y < 560):
                print("you are lost")
                self.lost += 1
                run=False
            if (functions.drag_out(sh_img_x, sh_img_y, 1050, 360) and sh_img_y > 340 and sh_img_y < 440):
                print("you are lost")
                self.lost += 1
                run=False

            show_score(textX,textY)

            pygame.display.update()

    def lost_screen(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            #print("you are lost")
            #print("score = ",self.score)
            self.screen.fill(self.bg_color)
            font = pygame.font.Font('game_over.ttf', 235)
            textX = 250
            textY = 200

            def show_score(x, y):
                sorry = font.render("SORRRYYY!!! ",True, (0, 0, 0))
                lost = font.render("YOU ARE LOST",True, (0, 0, 0))
                score = font.render("YOUR SCORE IS : "+ str(self.score),True, (0, 0, 0))
                self.screen.blit(score, (x, y+200))
                self.screen.blit(lost, (x, y))
                self.screen.blit(sorry,(x, y-200))
            show_score(250, 200)
            cry_img = pygame.image.load("cry.png")
            self.screen.blit(cry_img, (300,500))
            pygame.display.update()

    def front_screen(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.start = 1
                        run = False
            self.screen.fill(self.bg_color)
            font = pygame.font.Font('game_over.ttf', 150)

            textX = 250
            textY = 200

            def show_details(x, y):
                welcome = font.render("Welcome to Super Hero ", True, (0, 0, 0))
                self.screen.blit(welcome, (x, y - 200))
            show_details(300,350)
            pygame.display.update()

if __name__ == "__main__":
    sh = super_hero()
    sh.front_screen()
    if (sh.start == 1):
        sh.run_sh()
    if (sh.lost != 0):
        sh.lost_screen()

