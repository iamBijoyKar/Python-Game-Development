import turtle 
# game window 

wn=turtle.Screen()
wn.bgcolor("black")
wn.title("Pong")
wn.setup(width=800, height=600)
wn.tracer(0)

#paddle a

paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.color("white")
paddle_a.goto(-350,0)

#paddle b

paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.color("white")
paddle_b.goto(350,0)

#ball

ball=turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.penup()
ball.color("white")
ball.goto(0,0)
ball.dx=.1
ball.dy=.1

# obstracles 

ob1=turtle.Turtle();
ob1.speed();
ob1.penup();
ob1.shape("square")
ob1.shapesize(stretch_len=1,stretch_wid=5)
ob1.color("red")
ob1.goto(50,0)

ob2=turtle.Turtle();
ob2.speed();
ob2.penup();
ob2.shape("square")
ob2.shapesize(stretch_len=1,stretch_wid=5)
ob2.color("red")
ob2.goto(-50,0)

# initial score
score_a=0
score_b=0


# score board

pen=turtle.Turtle();
pen.penup();
pen.speed(0)
pen.color("white")
pen.hideturtle()
pen.goto(0,260)
pen.shapesize()
pen.write("Player A : {0}   Player B : {1} ".format(score_a,score_b), align="center", font=("Courier",24,"normal"))



#movement of paddles

def paddle_a_up():
    y=paddle_a.ycor()
    y+=20
    paddle_a.sety(y)

def paddle_a_down():
    y=paddle_a.ycor()
    y-=20
    paddle_a.sety(y)

def paddle_b_up():
    y=paddle_b.ycor()
    y+=20
    paddle_b.sety(y)

def paddle_b_down():
    y=paddle_b.ycor()
    y-=20
    paddle_b.sety(y)

#key bindings 

wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")

#main gameloop

while True :

    wn.update()
    # ball movement 
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    # border checking 
    if ball.ycor()>290  :
        ball.sety(290)
        ball.dy*=-1

    if ball.ycor()<-290  :
        ball.sety(-290)
        ball.dy*=-1
    
    if ball.xcor()>390:
        ball.setx(390)
        ball.goto(0,0)
        ball.dx*=-1
        score_a+=1
        pen.clear()
        pen.write("Player A : {0}   Player B : {1} ".format(score_a,score_b), align="center", font=("Courier",24,"normal"))


    if ball.xcor()<-390:
        ball.setx(-390)
        ball.goto(0,0)
        ball.dx*=-1
        score_b+=1
        pen.clear()
        pen.write("Player A : {0}   Player B : {1} ".format(score_a,score_b), align="center", font=("Courier",24,"normal"))


    # paddle and ball collisions 
    if (ball.xcor()>=340 and ball.xcor()<=350) and (ball.ycor()>=paddle_b.ycor()-50 and ball.ycor()<=paddle_b.ycor()+50):
        ball.setx(340);
        ball.dx*=-1;
    
    if (ball.xcor()<=-340 and ball.xcor()>=-350) and (ball.ycor()>=paddle_a.ycor()-50 and ball.ycor()<=paddle_a.ycor()+50):
        ball.setx(-340);
        ball.dx*=-1;

    if (ball.xcor()>=40 and ball.xcor()<=60) and (ball.ycor()<=100 and ball.ycor()>=-100 ):
        ball.dx*=-1;

    if (ball.xcor()<=-40 and ball.xcor()>=-60) and (ball.ycor()<=100 and ball.ycor()>=-100 ):
        ball.dx*=-1;

    paddle_a.sety(ball.ycor())
# score board 
# this is a opne player game 
