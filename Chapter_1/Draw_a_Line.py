import turtle as tu # 把turtle 套件引入code裡面

turtle = tu.Turtle() #叫一支畫筆叫做turtle
turtle.shape('turtle') #設定turtle的長相為一隻烏龜
window = tu.Screen() # 設定一個叫做window的視窗，用來顯示等等turtle在畫圖的過程
window.title(' My First Turtle Program!') #設定螢幕的名稱叫做 "My First Turtle Program"
window.setup(width=450, height=450) # 設定螢幕尺寸

turtle.forward(100) # 讓 turtle 往它現在面向的方向移動 100 長度

tu.done() # 畫圖結束，一定要這一行唷，不然螢幕會閃一下就消失