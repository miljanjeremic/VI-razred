import pygame as pg
import pygamebg

# otvaramo prozor
#(sirina, visina) = (600, 400)
#prozor = pygamebg.open_window(sirina, visina, "Боја позадине")
# bojimo pozadinu prozora
#prozor.fill(pg.Color("white"))

from turtle import *
shape("turtle")

import turtle


title('Moja kuca')

def zid():
    fd(100); rt(90);
    fd(100); rt(90);
    fd(100); rt(90);
    fd(100); rt(90);

def krov():
    fillcolor('red')
    begin_fill()
    fd(100); lt(120);
    fd(100); lt(120);
    fd(100); lt(120);
    end_fill()

def vrata():
    
    rt(90); fd(100);
    lt(90); fd(40);
    lt(90);
    fillcolor('green')
    begin_fill()
    fd(40); rt(90);
    fd(20); rt(90);
    fd(40); rt(90);
    end_fill()

def prozor():
    #fd(40); rt(90);
    #fd(60); rt(90);
    fillcolor('blue')
    begin_fill()
    fd(20); lt(90);
    fd(20); lt(90);
    fd(20); lt(90);
    fd(20); lt(90);
    pu()
    fd(40)
    pd()
    fd(20); lt(90);
    fd(20); lt(90);
    fd(20); lt(90);
    fd(20); lt(90);
    end_fill()

home()
zid()
pu()

pd()
krov()
pu()

pd()
vrata()
pu()

fd(40); rt(90);
fd(60); rt(90);

pd()
prozor()
pu()

pd()

pu()
lt(90); fd(150)
pd()
turtle.write("Moja kucica ", True, align="center")

