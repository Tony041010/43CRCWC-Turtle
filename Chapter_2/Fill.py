import turtle as tu

bob = tu.Turtle()
bob.shape('turtle')
window = tu.Screen()
window.title('Fill the patterns')
window.setup(width=450, height=450)

bob.color('black', 'yellow') #設定線條顏色為黑色，被用來填滿圖形的顏色為紅色

bob.begin_fill() #告訴程式開始填滿

#以畫正方形為例
length = 100
for i in range(4):
    bob.forward(100)
    bob.left(90)

bob.end_fill() #結束塗滿，這實在begin_fill和end_fill中間形成的圖形都會被填滿黃色


tu.done()