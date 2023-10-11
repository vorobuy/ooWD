from pygame import *

window = display.set_mode((1000,700))
display.set_caption("Настольный теннис")
fon = transform.scale(image.load('les.htm'),(1000,700))

font.init()
font = font.SysFont('Arial',35)
class Game_Sprite(sprite.Sprite):
    def __init__(self,player_image, player_x, player_y,size_x,size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_x,size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(Game_Sprite):
    def control(self):
        buttons = key.get_pressed()
        if buttons[K_w] and self.rect.y>5:
            self.rect.y-= self.speed
        if buttons[K_s] and self.rect.y<600:
            self.rect.y+= self.speed
    def control1(self):
        buttons = key.get_pressed()
        if buttons[K_i] and self.rect.y>5:
            self.rect.y-= self.speed
        if buttons[K_k] and self.rect.y<500:
            self.rect.y+= self.speed
game = True
finish = False
clock = time.Clock()
p1= Player('raketka.webp',20,300,10,100,15)
p2= Player('raketka.webp',970,300,10,100,15)
ball = Player('vorobey.png',500,300,50,50,0)
lose1 = font.render('сосиска',True,(12,13,154))
lose2 = font.render('сардеька',True,(12,13,154))
ballspeedx=6
ballspeedy=6
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
       
    if finish != True:
        window.blit(fon,(0,0))
        p1.reset()
        p2.reset()
        p1.control()
        p2.control1()
        ball.reset()
        ball.rect.x+=ballspeedx
        ball.rect.y-=ballspeedy
        if ball.rect.y <0 or ball.rect.y > 650:
            ballspeedy*=-1
        if ball.rect.x <0:
            finish=True
            window.blit(lose1,(400,300))
        if ball.rect.x >1000:
            finish=True
            window.blit(lose2,(400,300))
        if sprite.collide_rect(p1,ball) or sprite.collide_rect(p2,ball):
            ballspeedy *=1
            ballspeedx *=-1
        display.update()
    clock.tick(60)