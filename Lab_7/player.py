import time
import pygame
import pygame as pg
pg.init()

skyFullOfStarsPath = "sky.mp3"
mozzartPath = "sonata.mp3"
on_and_on_Path = "on_and_on.mp3"
sc = pg.display.set_mode((480, 360))
pg.display.set_caption("MP3 PLAYER")
clock = pg.time.Clock()
mozzart = pg.mixer.music.load(mozzartPath)
on_and_on = pg.mixer.music.load(on_and_on_Path)
despacito = pg.mixer.music.load(skyFullOfStarsPath)
musicList = [skyFullOfStarsPath, mozzartPath, on_and_on_Path]
pg.mixer.music.play(-1)
new_york = pg.image.load("new_york.png")
new_york = pygame.transform.scale(new_york, (600, 350))

sc.blit(new_york, (0, 0))
flPlay = False
run = True
index = 0
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                flPlay = not flPlay
                if flPlay:
                    pg.mixer.music.pause()
                else:
                    pg.mixer.music.unpause()
            elif event.key == pg.K_RIGHT:
                
                index += 1
                if index == len(musicList):
                    index = 0
                pg.mixer.music.load(musicList[index])
                pg.mixer.music.play()
            elif event.key == pg.K_LEFT:
                index -= 1
                if index == -1:
                    index = len(musicList)-1
                pg.mixer.music.load(musicList[index])
                pg.mixer.music.play()


    pg.display.flip()
    clock.tick(60)