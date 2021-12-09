# turtleSTriangle.py
# (Sierpinsky triangle algorithm)
import turtle as tu

def striangle(myTurtle, depth, base):
    myTurtle.down()
    if depth == 0: # 畫實心三角形
        myTurtle.begin_fill()
        for i in range(3):
            myTurtle.forward(base)
            myTurtle.left(120)
        myTurtle.end_fill()
    else: #移動到要畫的位置
        for i in range(3): # 碎形的 i 個部分
            striangle(myTurtle, depth-1, base) # !!遞迴!!
            myTurtle.penup()
            myTurtle.forward(base*2**depth)
            myTurtle.left(120)
            myTurtle.pendown()


bob = tu.Turtle()
bob.color('black', 'black')
bob.speed(0)
window = tu.Screen()
window.setup(width=600, height=600)
depth = 3 # 要有幾層的碎形
base = 20 # 每一個小三角形的大小
striangle(bob, depth, base)

tu.done()



