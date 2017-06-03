import turtle

def rectangular():
    window = turtle.Screen()
    window.bgcolor("white")

    b = turtle.Turtle()
    b.shape("square")
    b.color("blue")
    b.speed(2)
    
    b.forward(100)
    b.right(90)
    b.forward(100)
    b.right(90)
    b.forward(100)
    b.right(90)
    b.forward(100)
    b.right(90)
 
    window.exitonclick()

rectangular()
