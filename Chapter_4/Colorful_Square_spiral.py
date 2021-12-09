import turtle as tu

bob = tu.Turtle()
window = tu.Screen()
window. setup(width=600, height=600)

bob.speed(0)

Color = ['red', 'blue', 'green', 'orange']

for i in range(400):
    bob.forward(i)
    bob.left(89)
    bob.color(Color[i%4])
tu.done()
