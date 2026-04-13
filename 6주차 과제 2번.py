import random
from tkinter.simpledialog import*

def getString(): 
    retStr = ''
    retStr = askstring('문자열 입력', '거북이 쓸 문자열을 입력')
    return retStr

def getRGB(): 
    r, g, b = 0, 0, 0
    r = random.random()
    g = random.random()
    b = random.random()
    return(r,g,b)

def getXYAS(sw, sh): 
    x, y, angle, size = 0, 0, 0, 0
    x = random.randrange(-sw // 2, sw // 2)
    y = random.randrange(-sh // 2, sh // 2)
    angle = random.randrange(0,360)
    size = random.randrange(10,50)
    return [x, y, angle, size]

import turtle

inStr = ''
swidth, sheight = 300, 300
tX, tY, tAngle, tSize = [0] * 4

turtle.title('거북이 글자쓰기(모듈버전)')
turtle.shape('turtle')
turtle.setup(width = swidth + 50, height = sheight + 50)
turtle.screensize(swidth, sheight)
turtle.penup()
turtle.speed(5)

inStr = getString()

for ch in inStr: 
    tX, tY, tAngle, tSize = getXYAS(swidth, sheight)
    r, g, b = getRGB()

    turtle.goto(tX, tY)
    turtle.left(tAngle)

    turtle.pencolor((r, g, b))
    turtle.write(ch, font = ('맑은고딕', tSize, 'bold'))

turtle.done()
