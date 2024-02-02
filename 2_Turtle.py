import turtle
p=turtle.Pen(shape="turtle")

j=30
h=15

for n in range(6,20):
    angle = ((n-2)*180)/n
    p.left(180-(angle/2))
 
    j=j+12
    h+=4
    for i in range(n):
        p.forward(j)
        p.left(180-angle)
    p.right(180-(angle/2))
    p.penup()
    p.forward(h)
    p.down()

turtle.done()