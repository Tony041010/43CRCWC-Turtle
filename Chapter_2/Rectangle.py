import turtle as tu

rec = tu.Turtle() #rec 代表 rectangle
rec.shape('square')
rec.color('black', 'yellow')
window = tu.Screen()
window.title('Draw A Rectangle')
window.setup(width=450, height=450)


rec.penup()
rec.goto(-125, -100)
rec.pendown()
w = 100
h = 300

rec.begin_fill()
# 畫圖邏輯 : 畫兩遍長跟寬
for i in range(2):
    rec.forward(w)
    rec.left(90)
    rec.forward(h)
    rec.left(90)

rec.end_fill()

tu.done()