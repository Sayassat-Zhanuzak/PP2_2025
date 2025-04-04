import pygame as pg
import random, time, sys
from pygame.locals import *

pg.init()

font = pg.font.SysFont("Areal", 60)
font_small = pg.font.SysFont("Verdana", True, 20)

sc = pg.display.set_mode((1000, 1000))
W, H = 1000, 1000
pg.display.set_caption("Cool Race")
clock = pg.time.Clock()

bgRoad = pg.image.load("bgRoad.png")
sharkIm = pg.image.load("shark.png")
rocketIm = pg.image.load("rocket.png")
bombIm = pg.image.load("bomb.png")

speed = 3
score = 0
total_score = 0
money = 0
index = 0
game_over = False

def display_game_over():
    sc.fill((255, 255, 255))
    game_over_text = font.render("Game Over", True, (0, 0, 0))
    final_score = font.render(f"Score: {int(score)}", True, (0, 0, 0))
    total_score_text = font.render(f"Total Score: {int(total_score)}", True, (0, 0, 0))
    sc.blit(game_over_text, (W // 2 - 100, H // 2 - 50))
    sc.blit(final_score, (W // 2 - 100, H // 2))
    sc.blit(total_score_text, (W // 2 - 150, H // 2 + 50))
    pg.display.update()
    time.sleep(2)
    pg.quit()
    sys.exit()

class Cherry(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("cherry.png")
        self.rect = self.image.get_rect()
    def move(self):
        global score
        self.rect.move_ip(0, 3)
        if self.rect.top > 1100:
            self.rect.bottom = 0
            self.rect.center = (random.randint(40, W-40), 200)
    def draw(self):
        sc.blit(self.image, self.rect)

class Coin(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("coin.png")
        self.rect = self.image.get_rect()
    def move(self):
        global score
        self.rect.move_ip(0, 7)
        if self.rect.top > 1000:
            self.rect.bottom = 0
            self.rect.center = (random.randint(40, W-40), 200)
    def draw(self):
        sc.blit(self.image, self.rect)

class Enemy(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("bomb.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, W-40), 220)

    def move(self):
        self.image = pg.transform.scale(self.image, (100, 100))
        self.rect.move_ip(0, speed)
        if self.rect.top > 1000:
            self.rect.bottom = 0
            self.rect.center = (random.randint(40, W-40), 200)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Shark(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("shark.png")
        self.rect = self.image.get_rect()
        self.rect.center = (500, 700)

    def move(self):
        pressed_keys = pg.key.get_pressed()
        if self.rect.top > 5 and pressed_keys[pg.K_UP]:
            self.rect.move_ip(0, -15)
        if self.rect.bottom < 1200 and pressed_keys[pg.K_DOWN]:
            self.rect.move_ip(0, 15)
        if self.rect.left > 0 and pressed_keys[pg.K_LEFT]:
            self.rect.move_ip(-15, 0)
        if self.rect.right < 1000 and pressed_keys[pg.K_RIGHT]:
            self.rect.move_ip(15, 0)

rocket = Enemy()
shark = Shark()
coin = Coin()
cherry = Cherry()

coins = pg.sprite.Group()
coins.add(coin)

cherrys = pg.sprite.Group()
cherrys.add(cherry)

rockets = pg.sprite.Group()
rockets.add(rocket)

group = pg.sprite.Group()
group.add(rocket, shark, coin, cherry)

speed_incr = pg.USEREVENT + 1
pg.time.set_timer(speed_incr, 2000)

pg.mixer.music.load("Tokyo drift.mp3")
pg.mixer.music.play()

while True:
    for event in pg.event.get():
        if event.type == speed_incr:
            speed += money / 20
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    sc.blit(bgRoad, (0, 0))
    scores = font.render(f"Score: {int(score)}", True, (0, 0, 0))
    sc.blit(scores, (20, 20))

    for entity in group:
        sc.blit(entity.image, entity.rect)
        entity.move()
    
    if pg.sprite.spritecollideany(shark, coins):
        score += 1
        coin.rect.top = 1000
    
    if pg.sprite.spritecollideany(shark, cherrys):
        score += 2
        cherry.rect.top = 1000

    if pg.sprite.spritecollideany(shark, rockets):
        pg.mixer.music.pause()
        total_score = score
        display_game_over()
    
    pg.display.update()
    clock.tick(60)
