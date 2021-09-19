import pygame
import math
import random

#variables
white = (255, 255, 255)
black=(0,0,0)
size=width,height= 920,640
screen=pygame.display.set_mode(size)
screen_rect = screen.get_rect()
clock= pygame.time.Clock()
fps = 60

#sprites
sprites = pygame.sprite.Group()
players = pygame.sprite.Group()
opponents = pygame.sprite.Group()

class Player(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

        self.speedy = 0
    
    def update(self):
        self.rect.y += self.speedy
        self.speedy = 0

class Opponent(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        self.image = pygame.image.load('sprites/player.png')
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.speed = speed

    def update(self, ball):
        #moving while the ball is on his side of the screen
        if ball.rect.y > self.rect.y and ball.rect.x > width/2:
            self.rect.y += self.speed
        if ball.rect.y < self.rect.y and ball.rect.x > width/2:
            self.rect.y -= self.speed

        #moving while the ball is on the players side of the screen
        if height/2 > self.rect.y and ball.rect.x < width/2:
            self.rect.y += self.speed
        if height/2 < self.rect.y and ball.rect.x < width/2:
            self.rect.y -= self.speed
        

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, speed = 3):
        super().__init__()
        self.image = pygame.image.load('sprites/ball.png')
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.speed = speed

        if random.randint(0,2) % 2 == 0:
            self.speedx = self.speed
            self.speedy = -self.speed
        else:
            self.speedx = -self.speed
            self.speedy = -self.speed

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.y > height:
            self.speedy = -self.speedy
        if self.rect.y < 0:
            self.speedy = -self.speedy
        #if self.rect.x > width-12:
        #    self.speedx = -self.speedx
        #if self.rect.x < 0:
        



class Message_to_screen():

    def __init__(self, font, color, position, msg):
        self.font = font
        self.color = color
        self.position = position
        self.msg = msg
        self.rect = 0
        
    def Display(self):
       text = self.font.render(self.msg, True, self.color)
       self.rect = text.get_rect()
       position = self.rect
       position.center = (self.position[0], self.position[1])
       screen.blit(text, position)

def main_menu():
    menu_running = True

    while menu_running:
        screen.fill(black)
        title = Message_to_screen(pygame.font.Font('arcadeclassic/ARCADECLASSIC.TTF',40), (255,255,255), [width/2, height*0.3], 'PONG')
        title.Display()
        play_text = Message_to_screen(pygame.font.Font('arcadeclassic/ARCADECLASSIC.TTF',25), (255,255,255), [width/2, height*0.75], 'PLAY')
        play_text.Display()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu_running = False
            if event.type == pygame.MOUSEBUTTONDOWN and play_text.rect.collidepoint(pygame.mouse.get_pos()):
                menu_running = False
                difficulty_select_menu()
            
        
        pygame.display.update()
    
def difficulty_select_menu():
    difficulty_menu_running = True

    while difficulty_menu_running:
        screen.fill(black)
        title = Message_to_screen(pygame.font.Font('arcadeclassic/ARCADECLASSIC.TTF',40), (255,255,255), [width/2, height*0.3], 'SELECT DIFFICULTY')
        title.Display()
        difficulty1 = Message_to_screen(pygame.font.Font('arcadeclassic/ARCADECLASSIC.TTF',35), (255,255,255), [width/2, height*0.5], 'EASY')
        difficulty1.Display()
        difficulty2 = Message_to_screen(pygame.font.Font('arcadeclassic/ARCADECLASSIC.TTF',35), (255,255,255), [width/2, height*0.6], 'MEDIUM')
        difficulty2.Display()
        difficulty3 = Message_to_screen(pygame.font.Font('arcadeclassic/ARCADECLASSIC.TTF',35), (255,255,255), [width/2, height*0.7], 'HARD')
        difficulty3.Display()
        survival = Message_to_screen(pygame.font.Font('arcadeclassic/ARCADECLASSIC.TTF',35), (255,255,255), [width/2, height*0.8], 'SURVIVAL')
        survival.Display()

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    difficulty_menu_running = False
                if event.type == pygame.MOUSEBUTTONDOWN and difficulty1.rect.collidepoint(pygame.mouse.get_pos()):
                    difficulty_menu_running = False
                    game_loop('easy')
                if event.type == pygame.MOUSEBUTTONDOWN and difficulty2.rect.collidepoint(pygame.mouse.get_pos()):
                    difficulty_menu_running = False
                    game_loop('medium')
                if event.type == pygame.MOUSEBUTTONDOWN and difficulty3.rect.collidepoint(pygame.mouse.get_pos()):
                    difficulty_menu_running = False
                    game_loop('hard')
                if event.type == pygame.MOUSEBUTTONDOWN and survival.rect.collidepoint(pygame.mouse.get_pos()):
                    difficulty_menu_running = False
                    game_loop('survival')

        pygame.display.update()

def game_loop(difficulty):
    game_running = True

    player = Player(pygame.image.load('sprites/player.png'), 20, height/2)
    sprites.add(player)
    players.add(player)
    if difficulty == 'easy':
        opponent = Opponent(width-20, height/2, 3)
    if difficulty == 'medium':
        opponent = Opponent(width-20, height/2, 5)
    if difficulty == 'hard':
        opponent = Opponent(width-20, height/2, 10)
    if difficulty == 'survival':
        opponent = Opponent(width-20, height/2, 15)
    opponents.add(opponent)
    players.add(opponent)

    if difficulty == 'easy':
        ball = Ball(width/2, height/2, 4)
    if difficulty == 'medium':
        ball = Ball(width/2, height/2, 6)
    if difficulty == 'hard':
        ball = Ball(width/2, height/2, 12)
    if difficulty == 'survival':
        ball = Ball(width/2, height/2, 15)
    sprites.add(ball)

    score1 = 0
    score2 = 0
    
    while game_running:
        screen.fill(black)
        
        score1_text = Message_to_screen(pygame.font.Font('arcadeclassic/ARCADECLASSIC.TTF',40), (255,255,255), [width/2 - 20, height*0.05], str(score1))
        score1_text.Display()
        score2_text = Message_to_screen(pygame.font.Font('arcadeclassic/ARCADECLASSIC.TTF',40), (255,255,255), [width/2 + 20, height*0.05], str(score2))
        score2_text.Display()
        
        pygame.draw.line(screen, white, (width/2, 0), (width/2, height))    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            player.speedy -= 12
        if pressed[pygame.K_DOWN]:
            player.speedy += 12

        player_ball_collision = pygame.sprite.spritecollide(ball, players, False)
        for hit in player_ball_collision:
            ball.speedx = -ball.speedx
        
        if ball.rect.x > width:
            ball.kill()
            score1 += 1
            if difficulty == 'easy':
                ball = Ball(width/2, height/2, 4)
            if difficulty == 'medium':
                ball = Ball(width/2, height/2, 6)
            if difficulty == 'hard':
                ball = Ball(width/2, height/2, 10)
            sprites.add(ball)
        if ball.rect.x < 0:
            ball.kill()
            score2 += 1
            if difficulty == 'easy':
                ball = Ball(width/2, height/2, 4)
            if difficulty == 'medium':
                ball = Ball(width/2, height/2, 6)
            if difficulty == 'hard':
                ball = Ball(width/2, height/2, 10)
            sprites.add(ball)

        if score1 == 10:
            player.kill()
            opponent.kill()
            ball.kill()
            game_running = False
            end_screen(True)
            
        
        if score2 == 10:
            player.kill()
            opponent.kill()
            ball.kill()
            game_running = False
            end_screen(False)
            

        opponent.rect.clamp_ip(screen_rect)
        player.rect.clamp_ip(screen_rect)
        sprites.update()
        sprites.draw(screen)
        opponents.update(ball)
        opponents.draw(screen)
        pygame.display.update()
        clock.tick(fps)
        
def end_screen(won):
    end_screen_running = True

    while end_screen_running:
        screen.fill(black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_screen_running = False

        
        if won == True:
            you_win_text = Message_to_screen(pygame.font.Font('arcadeclassic/ARCADECLASSIC.TTF',70), (255,255,255), [width/2 - 20, height*0.2], 'YOU WIN!!!')
            you_win_text.Display()
        else:
            you_lost_text = Message_to_screen(pygame.font.Font('arcadeclassic/ARCADECLASSIC.TTF',70), (255,255,255), [width/2 - 20, height*0.2], 'YOU LOST HAHA!')
            you_lost_text.Display()

        back_to_menu_text = Message_to_screen(pygame.font.Font('arcadeclassic/ARCADECLASSIC.TTF',50), (255,255,255), [width/2 - 20, height*0.8], 'BACK TO MENU')
        back_to_menu_text.Display()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and back_to_menu_text.rect.collidepoint(pygame.mouse.get_pos()):
                end_screen_running = False
                main_menu()

        pygame.display.update()


def main():
    pygame.init()
    main_menu()

    pygame.quit()
    quit()

main()