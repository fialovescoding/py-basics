# Import turtle module
import turtle

# Create my turtle onject
t = turtle.Turtle()

# Draw the face using a circle
t.circle(40)

# Turn right and draw person's body
t.right(90)
t.forward(75)

# Hands
t.left(90)
t.right(45)
t.forward(50)
t.up()
t.backward(50)
t.right(90)
t.down()
t.forward(50)

t.backward(50)

t.left(45)

t.forward(75)

# Legs
t.left(90)
t.right(45)
t.forward(50)
t.up()
t.backward(50)
t.right(90)
t.down()
t.forward(50)


# t.left(45)
print('done')

