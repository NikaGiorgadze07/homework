from turtle import *

speed(40)
#we want print a house
#step 1 draw a square
width(10)
color("black")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square


#drawin a dore
begin_fill()
forward(60)
color("red")
left(90)
forward(100)
right(90)
forward(80)
right(90)
forward(100)
end_fill()
left(90)

penup()
goto(200, 200)
pendown()

begin_fill()
color("red")
left(120)
forward(200)
left(120)
forward(200)
end_fill()
#end door



#window
begin_fill()
color("black")

penup()
goto(130, 130)
pendown()

right(150)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
end_fill()

penup()
goto(8, 8)

forward(8)
right(90)
forward(120)
begin_fill()
right(90)
forward(30)
pendown()
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()

#the end






exitonclick()