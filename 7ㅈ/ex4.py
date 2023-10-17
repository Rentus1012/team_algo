import turtle

turtle.shape("turtle")
turtle.speed(0)

def Recursion(sp_length):
    if sp_length <= 5:
        return
    turtle.forward(sp_length)
    turtle.right(90)
    
    Recursion(sp_length - 3)

Recursion(200)