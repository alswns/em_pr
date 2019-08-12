import sys
import PyQt5.QtWidgets as pq
import PyQt5.QtGui as gui

seat=[[1,1,1,1,1,1],[1,0,1,1,1,1],
              [1,1,1,1,1,1],[0,0,1,0,1,1 ],[1,1,0,1,0,0]]

class LogInDialog(pq.QDialog):

    def __init__(self):
        super().__init__()
        self.name=str()
        self.all=[]
        self.i=0
        self.j=0
        self.id = None
        self.password = None
        self.seat=[[1,1,1,1,1,1],[1,0,1,1,1,1],
              [1,1,1,1,1,1],[0,0,1,0,1,1 ],[1,1,0,1,0,0]]
        self.setupUI()
    def setupUI(self):
        one=int()
        for i in range(5):
            one+=self.seat[i].count(1)
        info='남은좌석수는'+str(one)+'입니다'
        self.setGeometry(400,100,600,600)
        label=pq.QLabel(info,self)
        label.move(500,400)
        number=1


        for i in range(5):
            plus = 0

            for j in range(6):
                self.i=i
                self.j=j

                self.all.append(pq.QPushButton(str(number),self))
                #self.all[number].pq.QPushButton(str(number),self)
                self.all[number-1].setText(str(number))
                self.all[number-1].resize(100,50)
                self.all[number-1].clicked.connect(self.pushButtonClicked)
                i=int(i)
                j=int(j)

                if j%2==0:
                    plus+=20
                self.all[number-1].move(j*100+plus,i*50)
                if self.seat[i][j]==0:
                    self.all[number-1].setDisabled(True)
                number+=1


    def pushButtonClicked(self):
        print(self.i,self.j)
        sending_button = self.sender()
        sending_button.setDisabled(True)
        self.name=sending_button.text()
        print(sending_button.text())
        self.close()

class Main_display(pq.QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowIcon(gui.QIcon('emotion_logo.jpg'))
        self.setWindowTitle('Emotion project')
        self.setGeometry(100,100,300,300)


        label=pq.QLabel('예약하실 교실을 선택하여 주십시오',self)
        label.move(50,60)
        btn_first = pq.QPushButton('제 1 강의실',self)
        btn_first.move(60, 110)
        btn_first.resize(75,81)
        btn_first.clicked.connect(self.pushButoon)
        btn_second = pq.QPushButton('제 2 강의실', self)
        btn_second.resize(75,81)

        btn_second.move(170, 110)

        self.show()
    def pushButoon(self):
        display=LogInDialog()
        self.close()
        display.exec_()

        self.plus = pq.QLabel(self)
        self.plus.move(0, 200)
        self.plus.setText(str(display.name)+'번 자리 예약 하셨습니다')


        self.show()


if __name__ == '__main__':

    app = pq.QApplication(sys.argv)
    ex = Main_display()
    ex.show()
    app.exec_()