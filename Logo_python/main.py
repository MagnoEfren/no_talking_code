import turtle as t 

t.up()
t.goto(0,100)
t.down()
t.width(2)

t.begin_fill()
t.left(160)
t.circle(100,100)
t.circle(200,60)
t.circle(40,90)
t.circle(-40, 100)
t.circle(40, 100)
t.circle(200, 30)
t.left(90)
t.circle(-70, 150)
t.left(120)
t.circle(160, 50)
t.end_fill()
t.up()

t.right(110)
t.fd(30)
t.down()

def half():
	t.begin_fill()
	t.circle(-100,90)
	t.end_fill()

half()
t.setheading(260)
half()

t.hideturtle()
t.exitonclick()











