from tkinter import *


def keyPressed(event):
    # 키보드 문자하나 출력
    print(type(event.Key))


root = Tk()

frame = Frame(root, width=100, height=100)
# Key 이벤트 바인딩
frame.bind('<Button-1> ', keyPressed)
frame.place(x=0, y=0)

# 키보드 포커를 갖게 한다


root.mainloop()