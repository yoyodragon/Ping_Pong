import turtle as t
import time
window=t.getscreen()
window.clear()
window.setup(width = 1.0, height = 1.0)



t.bgcolor("black")
screenTk = window.getcanvas().winfo_toplevel()
screenTk.attributes("-fullscreen", True)
init_text = t.Turtle()
init_text.penup()
init_text.pencolor("white")
init_text.hideturtle()
init_text.setpos(-105,0)
init_text.write("PING PONG\n", font = ('roboto', 30, 'normal'))
time.sleep(1)
init_text.undo()
init_text.setpos(-550,0)
init_text.write("INSTRUCTIONS:\nPlayer A can use \'w\' to move up and \'s\' to move down\nPlayer B can use \'Up\' to move up and \'Down\' to move down\nThree points to win\nALL THE BEST!", font = ('roboto', 30, 'normal'))
time.sleep(6)
window.clear()

bg_box=t.Turtle()
bg_box.speed(1000)
bg_box.hideturtle()
bg_box.begin_fill()
bg_box.pencolor("black")
bg_box.penup()
bg_box.setpos(-660,370)
bg_box.pendown()
for i in range(2):
    bg_box.forward(1320)
    bg_box.right(90)
    bg_box.forward(740)
    bg_box.right(90)
    
bg_box.end_fill()   



t.bgcolor("white")
p = t.textinput("Player A", "\nWhat is the name of player A")
q = t.textinput("Player B", "\nWhat is the name of player B")
if p == None:
    p = "Player A"
if q == None:
    q = "Player B"
    
player_a = t.Turtle()
player_b = t.Turtle()
player_a.pencolor("white")
player_b.pencolor("white")
player_a_score = 0

player_a.penup()
player_a.hideturtle()
player_a.setpos(-100,250)
player_a.write(p+": ",font=('Arial', 20, 'normal'))


player_b_score = 0
player_b.penup()
player_b.hideturtle()
player_b.setpos(100,250)
player_b.write(q + ": ",font=('Arial', 20, 'normal'))







left_paddle=t.Turtle()
left_paddle.penup()
left_paddle.pencolor("white")
left_paddle.shape("square")
left_paddle.shapesize(4,1)
left_paddle.setpos(-630,0)

right_paddle=t.Turtle()
right_paddle.penup()
right_paddle.pencolor("white")
right_paddle.shape("square")
right_paddle.shapesize(4,1)
right_paddle.setpos(630,0)
left_paddle.speed(1000)
right_paddle.speed(1000)

ball=t.Turtle()
ball.penup()
ball.pencolor("white")

ball.shape("circle")
ball.shapesize(1.5)
ball.setpos(0,0)

increase=0
decrease=0

confirm=0
ball.dx = 3
ball.dy = 3

def right_paddle_a():
    right_paddle.setpos(right_paddle.xcor(),right_paddle.ycor() + 20 + increase)
def right_paddle_b():
    right_paddle.setpos(right_paddle.xcor(),right_paddle.ycor() - 20- decrease)
    
def left_paddle_a():
    left_paddle.setpos(left_paddle.xcor(),left_paddle.ycor() + 20+ increase)
def left_paddle_b():
    left_paddle.setpos(left_paddle.xcor(),left_paddle.ycor() - 20 - decrease)

    
    

window.onkeyrelease(right_paddle_a, "Up")
window.onkeyrelease(right_paddle_b, "Down")
window.onkeyrelease(left_paddle_a, "w")
window.onkeyrelease(left_paddle_b, "s")
'''
window.onkeypress(screenTk.attributes("-fullscreen", False), "Escape")
'''
window.listen()

while True:
    window.listen()
    
    ball.setpos(ball.xcor()+ball.dx,ball.ycor()+ball.dy)
    
    window.update()

    if confirm==0:
        num = t.numinput("Start Menu", "\nWhat level would you like to play?\n1.Beginner\n2.Amateur\n3.Novice")
        if num==1:
            ball.dx = 7
            ball.dy = 7
            confirm+=1
            ball.speed(10000)
        if num==2:
            ball.dx = 8
            ball.dy = 8
            increase=5
            decrease=5
            confirm+=1
            ball.speed(10000)
        if num==3:
            ball.dx = 9
            ball.dy = 9
            increase=10
            decrease=10
            confirm+=1
            ball.speed(1000)
        time.sleep(1)
            

    if player_a_score == 3 or player_b_score == 3:
        w = ""
        if player_a_score == 3:
            w = p
        else:
            w = q
        init_text.setpos(-120,200)
        
        init_text.write(" The Winner is: "+ w,font = ('roboto', 30, 'normal'))
        time.sleep(1)
        
        x = t.numinput("EndScreen", "\nWhat would you like to do?\n1.Play again\n2.Exit")
        if x == 2:
            screenTk.attributes("-fullscreen", False)
            window.bye()
            break
        elif x == 1:
            init_text.undo()
            player_a_score, player_b_score = 0,0
            a = p + ": " + str(player_a_score)
            player_a.undo()
            player_b.undo()
            ball.setpos(0,0)
            player_a.write(a,font=('Arial', 20, 'normal'))
            b = q +": " + str(player_b_score)
            player_b.write(b,font=('Arial', 20, 'normal'))
            x = 0
            time.sleep(1)
        
        
    
    
    if ball.xcor()> 650:
        time.sleep(1)
        player_a.undo()
        player_a_score += 1
        a = p+": " + str(player_a_score)
        print(a)
        player_a.write(a,font=('Arial', 20, 'normal'))
        ball.sety(0)
        ball.setx(0)
        left_paddle.setpos(-630,0)
        right_paddle.setpos(630,0)
        time.sleep(1)
        
        ball.dx*=-1

        
        
        
    if ball.xcor()< -650:
        time.sleep(1)
        player_b.undo()
        player_b_score += 1
        b = q + ": " + str(player_b_score)
        player_b.write(b,font=('Arial', 20, 'normal'))

        ball.sety(0)
        ball.setx(0)
        left_paddle.setpos(-630,0)
        right_paddle.setpos(630,0)
        time.sleep(1)
        
        ball.dx*=-1

        
        
    if ball.ycor()> 355:

        ball.dy*=-1
        ball.sety(360)

        
        
    if ball.ycor()< -355:
    
        ball.dy*=-1
        ball.sety(-360)
        
        
    
    

    if ball.ycor()> (right_paddle.ycor()- 20) and ball.ycor()< (right_paddle.ycor()+ 20) and ball.xcor() < (right_paddle.xcor() + 20) and ball.xcor() > (right_paddle.xcor() - 20):
        
        ball.dx*=(-1)
        ball.setx(right_paddle.xcor()-20)



    if ball.ycor()> (left_paddle.ycor()- 25) and ball.ycor()< (left_paddle.ycor()+ 25) and ball.xcor() < (left_paddle.xcor() + 25) and ball.xcor() > (left_paddle.xcor() - 25):
        
        ball.dx*=(-1)
        ball.setx(left_paddle.xcor()+20)

    if right_paddle.ycor()>370:
        right_paddle.setpos(right_paddle.xcor(),368)
        
    if right_paddle.ycor()<-370:
        right_paddle.setpos(right_paddle.xcor(),-368)

    if left_paddle.ycor()>370:
        left_paddle.setpos(left_paddle.xcor(),368)
        
    if left_paddle.ycor()<-370:
        left_paddle.setpos(left_paddle.xcor(),-368)
    

        
    
        


    
