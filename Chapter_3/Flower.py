import turtle as tu

flower = tu.Turtle()
window = tu.Screen()
window.title('Draw A Flower')
window.setup(width=450, height=450)

flower.penup()
flower.goto(-125, 0)
flower.pendown()
flower.speed(0)


times = 10 #設定要有多少片花瓣
length = 200
for i in range(times):
    flower.forward(length)
    flower.left(180-180//times)
    flower.forward(length)
    flower.left(180-180//times)


tu.done()