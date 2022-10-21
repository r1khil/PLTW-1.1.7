#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []



# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic", "arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold", "red", "blue", "green", "orange", "purple", "gold"]

# direction for new turtle
angle = 45
distance = 50

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  t.penup()
  my_turtles.append(t)


#  assigns the values startx and starty to 0
startx = 0
starty = 0

# for each value in turtle_shapes, it will go to the startx and starty value, turn right 45 degrees, and then go forward 50
for t in my_turtles:
  t.goto(startx, starty)
  t.pendown()
  t.right(angle)     
  t.forward(distance)
  

#	the value of startx and starty is increased by 50
  
  startx = t.xcor()
  starty = t.ycor()
  angle += 45
  distance += 10
  # print("popping", turtle_colors[-1])
  new_color = turtle_colors.pop()
  t.pencolor(new_color)
  t.fillcolor(new_color)
  

wn = trtl.Screen()
wn.mainloop()