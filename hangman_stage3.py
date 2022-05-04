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

def findLetter(searchLetter, word):
      count = 0
      ltrFound = []
      for letter in word:
            if letter == searchLetter:
                  ltrFound.append(count)
            count +=1
      return ltrFound

play = True
countRight = 0
countWrong = 0
game = Screen()
game.screensize(500,200)
game.bgpic("paper_gif.gif")
stewie = Turtle()
stewie.shape("turtle")
stewie.color("red", "blue")

word = "zimzima"

for i in range(len(word)):
    step = i*30
    drawline(stewie, step, 150, step+20, 150, 3, "green")



writeText(stewie, "Hangman Game", -220, 270, pcolor="indigo", font=["comic", 40, "bold"])

while play == True:
    
    strGuess = game.textinput("Str", "Guess a letter")

    if strGuess in word:
        ltrloc = findLetter(strGuess, word)
        for ind in ltrloc:
            xPos = ind*30
            writeText(stewie, strGuess, xPos+3, 150)
            countRight += 1
        if len(word) <= countRight:
            play = False
    else:        
        countWrong = countWrong +1
        if countWrong == 1:
            drawline(stewie, -270, -70, -70, -70, 9, "brown")
        elif countWrong == 2:
            drawline(stewie, -170, -70, -170, 230, 5, "brown")
        elif countWrong == 3:
            drawline(stewie, -170, 230, -70, 230, 5, "brown")
        elif countWrong == 4:
            drawline(stewie, -70, 230, -70, 180, 5, "brown")
        elif countWrong == 5:
            drawcircle(stewie, 30, -70, 120, psize=8, pcolor="red")
        elif countWrong == 6:
            drawline(stewie, -70, 120, -70, 70, 5, "red")
        elif countWrong == 7:
            drawline(stewie, -70, 110, -100, 70, 5, "red")
        elif countWrong == 8:
            drawline(stewie, -70, 110, -40, 70, 5, "red")
        elif countWrong == 9:
            drawline(stewie, -70, 70, -100, 20, 5, "red")
        elif countWrong == 10:
            drawline(stewie, -70, 70, -40, 20, 5, "red")

    if countWrong >=10:
        play = False

