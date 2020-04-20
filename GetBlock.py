import turtle
import time
import winsound
import random

win = turtle.Screen()
win.title("Collect Balls! v2.0.20")
win.bgcolor("#64E15E")
win.setup(600, 700)
win.tracer(0)


#Timer
class Timer(turtle.Turtle):
    def __init__(self, x, y, c, p, sec, action):
        turtle.Turtle.__init__(self)
        self.sec = 0
        self.pensize = "30"
        self.action = action
        self.ht()
        self.color("red")
        self.penup()
        self.goto(0, -260)
        self.write(time.strftime("%H:%M:%S", time.gmtime(self.sec)), False
                   , align="center", font=("Arial", self.pensize, "bold"))
    def start(self):
        self.clear()
        self.write(time.strftime("%H:%M:%S", time.gmtime(self.sec)), False
                   , align="center", font=("Arial", self.pensize, "bold"))
        self.sec += 1
          
        if self.sec != -1:
            win.ontimer(self.start, 1000)
        else:
            self.action()
    def stop(self):
        self.clear()
    def restart(self):
        self.clear()
        self.sec = 0
        self.write(time.strftime("%H:%M:%S", time.gmtime(self.sec)), False, align="center", font=("Arial", self.pensize, "bold"))
def testaction():
    timer.restart()

timer = Timer(0, 0, "red", 100, 15, testaction)
timer.start()

##ACTUAL GAME CODES##

delay = 0.1
score = 0


#Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

#Balls
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("white")
food.penup()
food.goto(0, 50)

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Balls Collected: 0", align="center", font=("Ariel", 24, "normal"))

peen = turtle.Turtle()
peen.speed(0)
peen.color("black")
peen.penup()
peen.hideturtle()
peen.goto(0, 230)
peen.write("Top Score: ", align="center", font=("Ariel", 20, "bold"))



#Functions
def go_up():
	head.direction="up"

def go_down():
	head.direction="down"

def go_left():
	head.direction="left"

def go_right():
	head.direction="right"

def move():
	if head.direction == "up":
		y = head.ycor()
		head.sety(y + 20)

	if head.direction == "down":
		y = head.ycor()
		head.sety(y - 20)

	if head.direction == "left":
		x = head.xcor()
		head.setx(x - 20)

	if head.direction == "right":
		x = head.xcor()
		head.setx(x + 20)

# Keyboard
win.listen()
win.onkeypress(go_up, "Up")
win.onkeypress(go_down, "Down")
win.onkeypress(go_left, "Left")
win.onkeypress(go_right, "Right")





while True:
	win.update()

	if head.xcor()>290 or head.xcor()<-290 or head.ycor()>320 or head.ycor()<-320:
		time.sleep(1)
		head.goto(0,0)
		food.goto(0,50)
		head.direction = "stop"
		pen.clear()
		pen.write("Balls Collected: 0".format(score), align="center", font=("Ariel", 24, "normal"))
		peen.clear()
		peen.write("Top Score: {}".format(score), align="center", font=("Ariel", 20, "bold"))
		score = 0
		timer.stop()
		timer.restart()
	
	if head.distance(food) < 20:
		x = random.randint(-290, 290)
		y = random.randint(-290, 290)
		score += 1
		pen.clear()
		pen.write("Balls Collected: {}".format(score), align="center", font=("Ariel", 24, "normal"))
		food.goto(x,y)
		winsound.PlaySound("smw_coin.wav", winsound.SND_ASYNC)
	
	
	move()
	
	time.sleep(delay)
	
win.mainloop()




