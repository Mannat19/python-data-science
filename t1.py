from turtle import *
speed('slowest')
fillcolor('purple')
side=7
begin_fill()
for i in range(side):
    forward(100)
    left(360/side)
end_fill()
hideturtle()
mainloop()