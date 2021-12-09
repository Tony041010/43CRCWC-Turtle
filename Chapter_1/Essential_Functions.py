import turtle as tu # 把turtle 套件引入code裡面

turtle = tu.Turtle() #叫一支畫筆叫做turtle
turtle.shape('turtle') #設定turtle的長相為一隻烏龜
window = tu.Screen() # 設定一個叫做window的視窗，用來顯示等等turtle在畫圖的過程
window.title(' My First Turtle Program!') #設定螢幕的名稱叫做 "My First Turtle Program"
window.setup(width=450, height=450) # 設定螢幕尺寸
'''
1.  turtle.goto(x, y) : 讓畫筆turtle移動到(x, y)處
把window想像成是一個座標平面，中心是原點O(0, 0), 所以左上角是(225, 225), 左下角是(-225, -225)
這個過程中，畫筆會從原本的座標走最短距離到目標座標，所以軌跡會被畫下來
code : 需要使用的時候解除註解即可
'''
# turtle.goto(100, 100) #把畫筆turtle 移到座標 (100, 100) 的位置

'''
2.	turtle.penup() , turtle.pendown() : 把畫筆turtle抬起來或是下筆，
在penup的狀態下，畫筆的所有移動軌跡都不會被畫出來
code : 需要使用的時候解除註解即可
'''
# turtle.penup() # 把畫筆turtle抬起來
# turtle.circle(100, 360) #以畫圓作範例，在penup的情況下你將不會看到這個圓
# turtle.pendown() # 把畫筆turtle放下來
# turtle.forward(100) # 因為pendown的關係，你會看到這條直線

'''
3.	turtle.speed(n) : 設定畫筆的速度，n 為0 ~ 10 之間的整數，數字越大越慢
如果數字超過10會被設成10，低於0會被設為0
code : 需要使用的時候解除註解即可
'''
# turtle.speed(0) #把速度調快
# turtle.penup()
# turtle.goto(-225, 0)
# turtle.pendown()
# turtle.forward(100) #因為把速度調快的關係，畫這一條線的速度會很快 
# turtle.speed(10) # 把速度調慢
# turtle.forward(100) #畫這條線的速度會比上一條慢很多，可以在執行程式時好好觀察

'''
4.	turtle.setheading(angle) : 設定畫筆turtle面向的角度，以正右方為0度開始算起
code : 需要使用的時候解除註解即可
'''
# turtle.setheading(0) # 把畫筆turtle朝向正右方
# turtle.forward(100) #這條線會向右畫
# turtle.setheading(90) #把畫筆turtle朝向正上方
# turtle.forward(100) #這條線會向上畫

'''
5.	turtle.left(angle), turtle.right(angle) : 把畫筆turtle向左/向右轉angle度
code : 需要使用的時候解除註解即可
'''
# turtle.forward(50)
# turtle.left(90) #讓畫筆turtle向左轉90度
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(50)

'''
6.	turtle.color(color1, color2) : 設定畫筆turtle的顏色，turtle1的顏色是軌跡(線條)的顏色，color2是開啟填滿時用來填滿的顏色
下一個章節在教填滿圖形的時候再講color2，我們現在先演示一遍如何改變線條的顏色
code : 需要使用的時候解除註解即可
'''
# turtle.color('red') #設定畫筆turtle畫出來的線條為紅色
# turtle.penup()
# turtle.goto(-225, 0)
# turtle.pendown()
# turtle.forward(100) #這一條線的顏色為紅色
# turtle.color('blue') #設定畫筆turtle畫出來的線條為藍色
# turtle.forward(100) #這一條線的顏色為藍色

tu.done() # 畫圖結束，一定要這一行唷，不然螢幕會閃一下就消失