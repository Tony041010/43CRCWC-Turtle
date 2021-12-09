import turtle as tu
ninja = tu.Turtle()
ninja.speed(0)
ninja.color('orange')

window = tu.Screen()
window.setup(width=600, height=600)

for i in range(180):
    ninja.forward(100)
    ninja.right(30)
    ninja.forward(20)
    ninja.left(60)
    ninja.forward(50)
    ninja.right(30) # 把 ninja 喬回原來的角度

    # 畫筆回到中心點
    ninja.penup()
    ninja.setposition(0, 0)
    ninja.pendown()

    ninja.right(2)

tu.done()


