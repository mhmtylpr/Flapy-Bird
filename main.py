import random
import time
import turtle
import winsound

'''
Follow Me 
İNSTAGRAM : ylpr44 
Thanks
'''


screen = turtle.Screen()
screen.title("Flapy Bird")
screen.bgcolor("grey")
screen.bgpic("bgbird.gif")
screen.setup(height=444,width=600)
screen.tracer(0)
screen.register_shape("bird.gif")
screen.register_shape("pipe.gif")
screen.register_shape("gameover.gif")
screen.register_shape("top.gif")


FONT = ("Verdana", 15, "normal")

#oyun müziği çalar

winsound.PlaySound('fp.wav', winsound.SND_ASYNC)

#kuş objesi oluşturuldu

bird = turtle.Turtle()
bird.penup()
bird.shape("bird.gif")
bird.shapesize(1)
bird.goto(-100,0)

#kuşun hareket şeması çizildi
def bird_top():
    time.sleep(0.02)
    x = bird.ycor()
    x += 100
    if x > 202:
        x = 202
        bird.sety(x)
    bird.sety(x)

screen.listen()
screen.onkeypress(bird_top,"space ")
start_time = time.time()
PIPES = list()

#engeller oluşturuldu

for n in range(10):
    dy = random.randint(160, 280)
    pipe_top = turtle.Turtle()
    pipe_top.shape("top.gif")
    pipe_top.penup()
    pipe_top.goto(350, dy)

    pipe_bottom = turtle.Turtle()
    pipe_bottom.setheading(270)
    pipe_bottom.forward(2)
    pipe_bottom.shape("pipe.gif")
    pipe_bottom.penup()
    pipe_bottom.goto(350, dy - 480)
    PIPES.append((pipe_bottom, pipe_top))
m = -1
Score = 0
score = turtle.Turtle()
score.hideturtle()
score.color("white")
score.penup()
score.goto(0, 195)
score.write(arg=f"Score:0", align="center", font=FONT)

a = time.time()
while True:

    if time.time() - start_time > 2 :
        start_time = time.time()
        m += 1
        if m == 9:
            m =-1
            for pipe in PIPES:
                dy = random.randint(80, 280)
                pipe[0].goto(350,dy-480)
                pipe[1].goto(350,dy)

    t_x = PIPES[m][0].xcor()
    t_x -= 10
    PIPES[m][0].setx(t_x)

    b_x = PIPES[m][1].xcor()
    b_x -= 10
    PIPES[m][1].setx(b_x)


    time.sleep(0.02)
    x = bird.ycor()
    x -= 5
    bird.sety(x)

#kaybetme protokolleri olşturuldu

    if bird.ycor() <-170:
        game_over = turtle.Turtle()
        game_over.goto(0 ,0)
        winsound.PlaySound('gameover.wav', winsound.SND_ASYNC)
        game_over.penup()
        game_over.speed(0)
        game_over.shape("gameover.gif")
        game_over.stamp()

        break
    if bird.xcor() + 5 > PIPES[m][1].xcor() + 22 and bird.xcor() + 5 > PIPES[m][1].xcor() - 22:
        if bird.ycor() + 5 > PIPES[m][1].ycor() - 88  or bird.ycor() - 5 < PIPES[m][0].ycor() + 173:
            winsound.PlaySound('gameover.wav', winsound.SND_ASYNC)
            game_over = turtle.Turtle()
            game_over.goto(0, 0)
            game_over.penup()
            game_over.speed(0)
            game_over.shape("gameover.gif")
            game_over.stamp()
            break

#scor biligsiini artışı sağlandı

    times = time.time() - a
    score.clear()
    score.write(arg=f"Score:{times:.0f}", align="center", font=FONT)
    score.hideturtle()

    screen.update()

screen.mainloop()
