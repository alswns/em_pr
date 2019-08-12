import sys
import PyQt5.QtWidgets as pq
import PyQt5.QtGui as gui
class MyApp(pq.QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowIcon(gui.QIcon('emotion_logo.jpg'))
        self.setWindowTitle('Emotion project')
       # self.move(300, 300)
        #self.resize(400, 200)
        self.setGeometry(100,100,300,300)



        label=pq.QLabel('예약하실 교실을 선택하여 주십시오',self)
        label.move(90,50)
        btn_first = pq.QPushButton('제 1 강의실', self)
        btn_first.move(50, 100)
        btn_second = pq.QPushButton('제 2 강의실', self)
        btn_second.move(100, 100)


        self.show()
if __name__ == '__main__':

    app = pq.QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())