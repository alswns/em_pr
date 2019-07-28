from tkinter import *
emotion=Tk()
emotion.resizable(False,False)
main=Frame(emotion,width=100,height=50)
openning=Frame(emotion,width=300,height=150)
select=Frame(emotion)
name=str('박민준')
emotion.title('emotion')
main_check=0
openning_check=0
select_check=0
def init():
    Main()
    emotion.mainloop()

def Main():

    def Click_me():
        global name
        name=label.get()
        print(name)

    emotion.geometry('180x50')
    label=Entry(main)
    btn_input=Button(main,text='입력',command=Click_me)
    btn = Button(main, text='다음페이지',command=Text)
    label.grid(row=0,column=0)
    btn_input.grid(row=0,column=1)
    btn.grid(row=1,column=0,columnspan=2)

    main.pack()



def Text():
    global name
    global openning_check
    emotion.geometry('300x150')
    main.pack_forget()

    if openning_check==0:
        intro = Label(openning,text=name+'님 접속을 환영합니다', font=(30))
        btn_one=Button(openning,text='특강', command=Select,width=10,heigh=5,relief='raised')
        btn_two=Button(openning,text='소수전공',command=Select,width=10,heigh=5,relief='raised')
        btn_three=Button(openning,text='자습실',command=Select,width=10,heigh=5,relief='raised')
        # intro.grid(row=0,column=0)
        # btn_one.grid(row=1,column=0)
        # btn_two.grid(row=1,column=1)
        # btn_three.grid(row=1,column=2)
        intro.pack(expand=True,pady=10,fill='both')
        btn_one.pack(side='left', padx=5)
        btn_two.pack(side='left', padx=5)
        btn_three.pack(side='left', padx=5)
        openning_check += 1
    openning.pack()

def Select():
    global select_check
    openning.pack_forget()
    if select_check==0:
        label = Button(select, text='come')
        label.pack()
        select_check+=1
    select.pack()

init()