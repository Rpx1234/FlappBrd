import pygame as pg

gravity = .2
LEFT = 1
RIGHT = 3
white = (255,255,255)
Score = 0

class Bird(pg.sprite.Sprite):

    def __init__(self):
        super().__init__()
        pos = pg.mouse.get_pos()
        gameDisplay =  pg.display.set_mode((800, 454))
        
        self.gameDisplay = gameDisplay
        self.image = (pg.image.load('flapp1.png'))

        self.rect = self.image.get_rect(center=pos)
        self.pos_y = pos[1]
        mouse_x = pos[0]
        self.velocity_y = 0

    def update(self, gravity, Score):
        print(Score)
        pos = pg.mouse.get_pos()
        mouse_x = pos[0]
        
        self.velocity_y += gravity
        self.pos_y += self.velocity_y

        self.rect.y = self.pos_y
        self.rect.x = mouse_x
        
        self.gameDisplay.blit(self.image, (mouse_x,self.rect.y))

        if self.pos_y > self.gameDisplay.get_height():
            
            self.kill()  # Remove off-screen birds.
            deathScreen(Score)
            
            

    def jump(self):
        pos = pg.mouse.get_pos()
        mouse_x = pos[0]
        self.rect.y = self.pos_y

        #self.pos_y += self.velocity_y
        self.velocity_y = -5
        self.gameDisplay.blit(self.image, (mouse_x,self.rect.y))

        


def startScreen():
    gameDisplay =  pg.display.set_mode((800, 454))
    irashai = (pg.image.load('irashai.png'))
    star = False
    gameExit = False
    while star == False and gameExit == False:
        gameDisplay.blit(irashai, (0,0))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                gameExit = True
                pg.quit()
                quit()
            
            if event.type == pg.MOUSEBUTTONDOWN:
                star = True
                
        pg.display.flip()

def deathScreen(Score):
    gameDisplay =  pg.display.set_mode((800, 454))
    irashai = (pg.image.load('deathdude.png'))
    font = pg.font.SysFont(None, 75)
    
    text = font.render(str(Score), True, white)
    gameExit = False
    while gameExit == False:
        gameDisplay.blit(irashai, (0,0))
        gameDisplay.blit(text,(50,50))
        for event in pg.event.get():
            #if event.type == pg.QUIT:
            #    run_game()
            
            if event.type == pg.MOUSEBUTTONDOWN:
                gameExit = True
                run_game(Score)
                
                
        pg.display.flip()

def music():
    pg.mixer.init()
    pg.mixer.music.load("main_theme.ogg")
    pg.mixer.music.play()

def spriteSheet():
    print()

def sideScrolling():
    W = 800
    H = 454
    x = 0

    gameDisplay =  pg.display.set_mode((800, 454))
    level = (pg.image.load('level_resize.png'))
    
    rel_x = x % level.get_rect().width
    if rel_x < W:
        gameDisplay.blit(level,(rel_x,0))
    gameDisplay.blit(level,(rel_x - level.get_rect().width, 0))
    x -= 1

def run_game(Score):
    pg.init()

    W = 800
    H = 454
    x = 0
    dodged = 0
    count = dodged

    font = pg.font.SysFont(None, 20)
    

    gameDisplay =  pg.display.set_mode((800, 454))
    pg.display.set_caption('Bidr')
    clock = pg.time.Clock()
    gameExit = False
    
    flapp = (pg.image.load('flapp1.png'))
    level = (pg.image.load('level_resize.png'))
    birds = pg.sprite.Group()
    width = level.get_rect().width
    
    pg.display.update()

    bird = Bird()

    while not gameExit:  
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                gameExit = True
            elif event.type == pg.MOUSEBUTTONDOWN and event.button == LEFT:
                bird.jump()

        rel_x = x % level.get_rect().width
        if rel_x < W:
            gameDisplay.blit(level,(rel_x,0))
        gameDisplay.blit(level,(rel_x - level.get_rect().width, 0))
        x -= 1
        
        
        

        pos = pg.mouse.get_pos()
        mouse_x = pos[0]
        
        if x % 50 == 0:
            dodged += 1
            
        text = font.render(str(dodged), True, white)
        Score = dodged
        ##print(Score)
        gameDisplay.blit(text,(mouse_x,(bird.rect.y + -15)))
        if dodged > 5:
            x -= 2
        if dodged > 20:
            x -= 3
        if dodged > 50:
            x -= 4

        bird.update(gravity,Score)

        birds.draw(gameDisplay)
        
        pg.display.update()
        clock.tick(60)

startScreen()
music()
run_game(Score)
pg.quit()
