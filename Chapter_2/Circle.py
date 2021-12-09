import turtle as tu

circle = tu.Turtle()
circle.shape('circle')
window = tu.Screen()
window.title('Draw A Circle')
window.setup(width=450, height=450)

# 1. 暴力土法煉鋼
# count = 0
# while(count < 360):
#     circle.forward(2)
#     circle.left(1)
#     count += 1
# print("finished!")

# 2. 使用內建函式
# circle.circle(100, 360)

tu.done()