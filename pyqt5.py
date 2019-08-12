import sys
import PyQt5.QtWidgets as pq
import PyQt5.QtGui as gui
from pymongo import MongoClient



class LogInDialog(pq.QDialog):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Emotion project')
        self.setWindowIcon(gui.QIcon('emotion_logo.jpg'))


        #db에서 데이터 받아오기
        client = MongoClient('localhost', 27017)
        # localhost: ip주소
        # 27017: port 번호
        # db=client['seat']
        # posts = db.posts
        db = client['seat']
        self.collection = db['seat']
        result = self.collection.find({'name': '제1강의실'})
        for i in result:
            seat = i['seat']
        seat = list(map(int, seat))
        print(seat)



        self.name=str()
        self.all=[]
        self.i=0
        self.j=0
        self.id = None
        self.password = None
        self.seat=seat
        self.setupUI()
    def setupUI(self):

        one=self.seat.count(1)
        info='남은좌석수는 '+str(one)+' 석입니다'
        self.setGeometry(400,100,700,400)

        label=pq.QLabel(info,self)
        label.move(100,10)
        number=1


        for i in range(5):
            plus = 0

            for j in range(6):

                self.all.append(pq.QPushButton(str(number),self))
                #self.all[number].pq.QPushButton(str(number),self)
                self.all[number-1].setText(str(number))
                self.all[number-1].resize(100,50)
                self.all[number-1].clicked.connect(self.pushButtonClicked)
                i=int(i)
                j=int(j)

                if j%2==0:
                    plus+=20
                self.all[number-1].move(j*100+plus,i*50+100)
                if self.seat[number-1]==0:
                    self.all[number-1].setDisabled(True)
                number+=1


    def pushButtonClicked(self):
        sending_button = self.sender()
        sending_button.setDisabled(True)
        self.name=sending_button.text()

        self.seat[int(sending_button.text())-1]=0
        print(self.seat)
        self.collection.update({'name': '제1강의실'}, {'name': '제1강의실', 'seat': self.seat}, upsert=False)

        self.close()

class Main_display(pq.QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowIcon(gui.QIcon('emotion_logo.jpg'))
        self.setWindowTitle('Emotion project')
        self.setGeometry(400,100,300,300)


        label=pq.QLabel('예약하실 교실을 선택하여 주십시오',self)
        label.move(50,60)
        btn_first = pq.QPushButton('제1강의실',self)
        btn_first.move(60, 110)
        btn_first.resize(75,81)
        btn_first.clicked.connect(self.pushButoon)
        btn_second = pq.QPushButton('제2강의실', self)
        btn_second.resize(75,81)
        btn_format=pq.QPushButton('초기화',self)
        btn_format.move(100,280)
        btn_format.clicked.connect(self.format)
        btn_second.move(170, 110)
        self.plus = pq.QLabel('예약하실 교실을 선택하여 주십시오',self)
        self.plus.move(50, 220)

        self.show()
    def format(self):
        # db에서 데이터 받아오기
        client = MongoClient('localhost', 27017)
        # localhost: ip주소
        # 27017: port 번호
        # db=client['seat']
        # posts = db.posts
        db = client['seat']
        collection = db['seat']
        collection.update({'name': '제1강의실'}, {'name': '제1강의실', 'seat': [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]}, upsert=False)

    def pushButoon(self):
        inputs=self.sender()
        print(inputs.text())
        display=LogInDialog()
        self.close()
        display.exec_()
        self.plus.move(70, 220)
        self.plus.setText(str(display.name)+'번 자리 예약 하셨습니다')
        from pymongo import MongoClient
        client = MongoClient()
        # 클래스 객체 할당
        self.show()


if __name__ == '__main__':

    app = pq.QApplication(sys.argv)
    ex = Main_display()
    ex.show()
    app.exec_()