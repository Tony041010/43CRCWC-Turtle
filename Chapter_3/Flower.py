import turtle as tu

def flower(bob, length):
    for i in range(length):
        bob.circle(length-i, 90)
        bob.left(90)
        bob.circle(length-i, 90)
        bob.left(18)


pen = tu.Turtle()
pen.speed(-1)
window = tu.Screen()
window.setup(width=600, height=600)
window.title('Draw a flower')
flower(pen, 190)

tu.done()

