import turtle as tu

bob = tu.Turtle()
window = tu.Screen()
window. setup(width=600, height=600)

bob.speed(0)

for i in range(500):
    bob.forward(i)
    bob.left(91)

tu.done()


