import sys
import PyQt5.QtWidgets as pq
import PyQt5.QtGui as gui
import PyQt5.QtCore as cr
from pymongo import MongoClient
#시작하기전에 cmd에서 mongod --dbpath D:\dev\mongoDB\data\db 입력


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
        db_data=self.collection.find({'id':1})
        for i in db_data:
            self.inputs=i['input']
        print(self.inputs)
        if self.inputs == '제1강의실':
            result = self.collection.find({'name': '제1강의실'})
            for i in result:
                seat = i['seat']
            seat = list(map(int, seat))
            print(seat)
        if self.inputs=='제2강의실':
            result = self.collection.find({'name': '제2강의실'})
            for i in result:
                seat = i['seat']
            seat = list(map(int, seat))
            print(seat)

        self.seat = seat

        self.name=str()
        self.all=[]
        self.i=0
        self.j=0
        self.id = None
        self.password = None

        self.setupUI()
    def setupUI(self):

        one=self.seat.count(1)
        info='남은좌석수는 '+str(one)+' 석입니다'
        self.setGeometry(400,100,700,400)

        label=pq.QLabel(info,self)
        label.move(100,10)
        number=1
        yplus = 0

        for i in range(5):
            xplus = 0
            if self.inputs=='제2강의실':
                yplus += 10
            for j in range(6):
                if self.inputs == '제2강의실':
                    xplus += 10
                self.all.append(pq.QPushButton(str(number),self))
                #self.all[number].pq.QPushButton(str(number),self)
                self.all[number-1].setText(str(number))
                self.all[number-1].resize(100,50)
                self.all[number-1].clicked.connect(self.pushButtonClicked)
                i=int(i)
                j=int(j)

                if self.inputs=='제1강의실':
                    if j%2==0:
                        xplus+=20

                self.all[number-1].move(j*100+xplus,i*50+yplus+80)
                if self.seat[number-1]==0:
                    self.all[number-1].setDisabled(True)
                number+=1


    def pushButtonClicked(self):
        sending_button = self.sender()
        sending_button.setDisabled(True)
        self.name=sending_button.text()

        self.seat[int(sending_button.text())-1]=0
        print(self.seat)
        if self.inputs=='제1강의실':
            self.collection.update({'name': '제1강의실'}, {'name': '제1강의실', 'seat': self.seat}, upsert=False)
        else:
            self.collection.update({'name': '제2강의실'}, {'name': '제2강의실', 'seat': self.seat}, upsert=False)
        self.close()

class Main_display(pq.QWidget):

    def __init__(self):
        super().__init__()
        # db에서 데이터 받아오기
        client = MongoClient('localhost', 27017)
        # localhost: ip주소
        # 27017: port 번호
        # db=client['seat']
        # posts = db.posts
        db = client['seat']
        self.collection = db['seat']
        result = self.collection.find({'name': '제1강의실'})
        for i in result:
            seats = i['seat']
        self.first_seat = list(map(int, seats))

        result = self.collection.find({'name': '제2강의실'})
        for i in result:
            seats = i['seat']
        self.second_seat= list(map(int, seats))
        print(self.first_seat)
        print(self.second_seat)

        sing_in=login()
        sing_in.exec_()
        print(sing_in.toss)
#        title=sing_in.

        self.initUI()

    def initUI(self):
        self.setWindowIcon(gui.QIcon('emotion_logo.jpg'))
        self.setWindowTitle('Emotion project')
        self.setGeometry(400,100,300,300)
        first_all = len(self.first_seat)
        first_remain = self.first_seat.count(1)
        first_mesesge = str(first_remain) + '/' + str(first_all)

        second_all = len(self.second_seat)
        second_remain = self.second_seat.count(1)
        second_mesesge = str(second_remain) + '/' + str(second_all)

        label=pq.QLabel('예약하실 교실을 선택하여 주십시오',self)
        label.move(50,60)
        self.btn_first = pq.QPushButton('제1강의실\n'+first_mesesge,self)
        self.btn_first.move(60, 110)
        self.btn_first.resize(75,81)
        self.btn_first.clicked.connect(self.pushButoon)
        self.btn_second = pq.QPushButton('제2강의실\n'+second_mesesge, self)
        self.btn_second.resize(75,81)
        self.btn_second.clicked.connect(self.pushButoon)
        self.btn_second.move(170, 110)

        btn_format=pq.QPushButton('초기화',self)
        btn_format.move(100,280)
        btn_format.clicked.connect(self.format)

        self.plus = pq.QLabel('예약하실 교실을 선택하여 주십시오',self)
        self.plus.move(50, 220)

        self.show()
    def format(self):

        self.collection.update({'name': '제1강의실'}, {'name': '제1강의실', 'seat': [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]}, upsert=False)
        self.collection.update({'name': '제2강의실'}, {'name': '제2강의실', 'seat': [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]}, upsert=False)
    def pushButoon(self):
        inputs=self.sender().text()
        self.collection.update({'id': 1}, {'id': 1, 'input': str(inputs)[0:5]})
        display=LogInDialog()
        self.close()
        display.exec_()

        result = self.collection.find({'name': '제1강의실'})
        for i in result:
            seats = i['seat']
        self.first_seat = list(map(int, seats))

        result = self.collection.find({'name': '제2강의실'})
        for i in result:
            seats = i['seat']
        self.second_seat = list(map(int, seats))

        first_all = len(self.first_seat)
        first_remain = self.first_seat.count(1)
        first_mesesge = '제1강의실\n'+str(first_remain) + '/' + str(first_all)

        second_all = len(self.second_seat)
        second_remain = self.second_seat.count(1)
        second_mesesge = '제2강의실\n'+str(second_remain) + '/' + str(second_all)


        self.plus.move(70, 220)
        self.plus.setText(str(display.name)+'번 자리 예약 하셨습니다')
        self.btn_first.setText(first_mesesge)
        self.btn_second.setText(second_mesesge)
        self.show()

class login(pq.QDialog):
    def __init__(self):
        super().__init__()
        self.resize(300,120)

        client = MongoClient('localhost', 27017)
        # localhost: ip주소
        # 27017: port 번호
        # db=client['seat']
        # posts = db.posts
        db = client['seat']
        self.collection = db['member']
        self.income_id=str()
        self.toss=str()
        self.initUI()


    def initUI(self):
        label=pq.QLabel("아이디와 학번을 입력하여 주십시오",self)
        label.move(10,0)
        label1 = pq.QLabel("학번:",self)
        label1.move(10,30)
        label2 = pq.QLabel("ID:",self)
        label2.move(10, 60)
        label1.alignment()
        self.lineEdit1 = pq.QLineEdit(self)
        self.lineEdit1.move(40,30)
        self.lineEdit2 = pq.QLineEdit(self)
        self.lineEdit2.move(40, 60)
        self.pushButton1 = pq.QPushButton("로그인",self)
        self.pushButton1.move(200,30)
        self.pushButton1.clicked.connect(self.pushButtonClicked)
        self.pushButton2 = pq.QPushButton("회원가입", self)
        self.pushButton2.clicked.connect(self.pushButton2Clicked)
        self.pushButton2.move(200, 60)
        self.error=pq.QLabel('',self)
        self.error.resize(171,16)
        self.error.move(0,90)
        self.error.setStyleSheet('color: red')
    def pushButtonClicked(self):
        self.class_num = self.lineEdit1.text()
        self.id = self.lineEdit2.text()
        result = self.collection.find({'class_num': self.class_num})
        for i in result:
            self.income_id = i['id']
        if self.id == self.income_id:
            self.close()
        else:
            self.error.setText('회원정보가 일치하지 않습니다')
            return
    def pushButton2Clicked(self):
        self.close()
        di=sing_up()
        di.exec_()
        self.toss=di.set_name


class sing_up(pq.QDialog):
    def __init__(self):
        super().__init__()

        client = MongoClient('localhost', 27017)
        # localhost: ip주소
        # 27017: port 번호
        # db=client['seat']
        # posts = db.posts
        db = client['seat']
        self.collection = db['member']
        self.set_name=str()
        self.resize(310,250)
        self.initUI()
    def initUI(self):
        title=pq.QLabel('회원 정보를 입력하여주십시오',self)
        title.move(20,20)
        labe_number=pq.QLabel('학번:',self)
        labe_number.move(20,70)
        labe_id=pq.QLabel('ID:',self)
        labe_id.move(20, 110)
        labe_name=pq.QLabel('이름:',self)
        labe_name.move(20, 150)

        self.number=pq.QLineEdit(self)
        self.number.move(70,70)
        self.id = pq.QLineEdit(self)
        self.id.move(70, 110)
        self.name = pq.QLineEdit(self)
        self.name.move(70, 150)
        btn_ok=pq.QPushButton('확인',self)
        btn_ok.move(220,220)
        btn_ok.clicked.connect(self.pushButton)
        self.error_text=pq.QLabel('',self)
        self.error_text.resize(231,16)
        self.error_text.move(10, 200)
    def pushButton(self):
        self.set_num=self.number.text()
        set_id=self.id.text()
        set_name=self.name.text()
        informaition={'class_num':self.set_num,'id':set_id,'name':set_name}
        data=self.collection.find_one({'class_num': self.set_num})

        if data == None:
            self.collection.insert(informaition)
            self.close()
        else:
            self.error_text.setText('이미 있는 학번입니다.다시입력해주십시오')


if __name__ == '__main__':

    app = pq.QApplication(sys.argv)
    ex = Main_display()
    ex.show()
    app.exec_()