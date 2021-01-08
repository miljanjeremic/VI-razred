import pygame as pg
import pygamebg

(sirina, visina) = (400, 400)
prozor = pygamebg.open_window(sirina, visina, "Pygame")
prozor.fill(pg.Color("white"))

pg.draw.polygon(prozor, pg.Color("red"), [(100, 150), (200, 50), (300, 150)])
pg.draw.rect(prozor, pg.Color("yellow"), (100, 150, 200, 150))
pg.draw.rect(prozor, pg.Color("green"), (120, 180, 50, 50))
pg.draw.rect(prozor, pg.Color("green"), (230, 180, 50, 50))
pg.draw.rect(prozor, pg.Color("brown"), (175, 200, 50, 100))
font = pg.font.SysFont("Arial", 20)
tekst = font.render("Moja kućica", True, pg.Color("black"))
prozor.blit(tekst, (110, 300))

pygamebg.wait_loop()
