#! /usr/local/bin/python3
import pygame as pg

pg.init()
screen = pg.display.set_mode((800, 800))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    screen.fill('white')

    pg.display.flip()
    
