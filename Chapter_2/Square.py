import turtle as tu

square = tu.Turtle()
square.shape('square')
window = tu.Screen()
window.title('Draw A Square')
window.setup(width=450, height=450)

length = 100 #設定正方形的邊長為length

# 畫圖邏輯 : 每畫完一條邊就轉90度
for i in range(4):
    square.forward(length)
    square.left(90)

tu.done()