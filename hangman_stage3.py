from turtle import *

def drawline(trtlName, x1, y1, x2, y2, psize=3, pcolor="black"):
    trtlName.showturtle()
    trtlName.penup()
    trtlName.goto(x1,y1)
    trtlName.pensize(psize)
    trtlName.pencolor(pcolor)
    trtlName.pendown()
    trtlName.goto(x2, y2)
    trtlName.hideturtle()

def drawcircle(trtlName, radius, x, y, psize=3, pcolor="black"):
    trtlName.showturtle()
    trtlName.penup()
    trtlName.goto(x,y)
    trtlName.pensize(psize)
    trtlName.pencolor(pcolor)
    trtlName.pendown()
    trtlName.circle(radius)
    trtlName.hideturtle()

def writeText(trtlName, text, x, y, pcolor="green", font=["courier", 20, "italic"]):
    trtlName.penup()
    trtlName.goto(x, y)
    trtlName.pencolor(pcolor)
    trtlName.write(text, font=(font[0], font[1], font[2]))

play = True
count = 0
game = Screen()
stewie = Turtle()
stewie.shape("turtle")
stewie.color("red", "blue")

word = "quiet"

for i in range(len(word)):
    step = i*30
    drawline(stewie, step, 150, step+20, 150, 3, "green")



writeText(stewie, "Hangman Game", -220, 270, pcolor="indigo", font=["comic", 40, "bold"])

while play == True:
    
    strGuess = game.textinput("Str", "Guess a letter")

    if strGuess in word:
        ind = word.index(strGuess)
        xPos = ind*30
        writeText(stewie, strGuess, xPos+3, 150)
    else:        
        count = count +1
        if count == 1:
            drawline(stewie, -270, -70, -70, -70, 9, "brown")
        elif count == 2:
            drawline(stewie, -170, -70, -170, 230, 5, "brown")
        elif count == 3:
            drawline(stewie, -170, 230, -70, 230, 5, "brown")
        elif count == 4:
            drawline(stewie, -70, 230, -70, 180, 5, "brown")
        elif count == 5:
            drawcircle(stewie, 30, -70, 120, psize=8, pcolor="red")
        elif count == 6:
            drawline(stewie, -70, 120, -70, 70, 5, "red")
        elif count == 7:
            drawline(stewie, -70, 110, -100, 70, 5, "red")
        elif count == 8:
            drawline(stewie, -70, 110, -40, 70, 5, "red")
        elif count == 9:
            drawline(stewie, -70, 70, -100, 20, 5, "red")
        elif count == 10:
            drawline(stewie, -70, 70, -40, 20, 5, "red")

    if count >=10:
        play = False

