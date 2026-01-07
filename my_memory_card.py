from PyQt5.QtCore import Qt  
from PyQt5.QtWidgets import(
    QApplication, QWidget, QLabel, QRadioButton, 
    QVBoxLayout, QHBoxLayout, QGroupBox, QPushButton,QButtonGroup)
from random import shuffle
from random import randint
app = QApplication([])
main_win = QWidget()
main_win.resize(400, 300)
main_win.setWindowTitle('Memory Card')

lb_question = QLabel('Which nationality does not exist?')
rbtn_1 = QRadioButton('Enets')
rbtn_2 = QRadioButton('Smurfs')
rbtn_3 = QRadioButton('Chluyms')
rbtn_4 = QRadioButton('Aleuts')
RadioGroupBox = QGroupBox()
btn_OK = QPushButton('Answer')


layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1, alignment = Qt.AlignCenter)
layout_ans2.addWidget(rbtn_2, alignment = Qt.AlignCenter)
layout_ans3.addWidget(rbtn_3, alignment = Qt.AlignCenter)
layout_ans3.addWidget(rbtn_4, alignment = Qt.AlignCenter)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

main_layout = QVBoxLayout()

layout_question = QHBoxLayout()
layout_answer = QHBoxLayout()
layout_btn = QHBoxLayout()
layout_question.addWidget(lb_question, alignment = Qt.AlignCenter)
layout_answer.addWidget(RadioGroupBox)
layout_btn.addStretch(3)
layout_btn.addWidget(btn_OK)
layout_btn.addStretch(3)

#Membauat grup box result
AnsGroupBox = QGroupBox()
lb_Result = QLabel('True/False')
lb_answer = QLabel('Correct ANswer')

l_v = QVBoxLayout()
l_v.addWidget(lb_Result)
l_v.addWidget(lb_answer)
AnsGroupBox.setLayout(l_v)

main_layout.addLayout(layout_question)
main_layout.addLayout(layout_answer)
main_layout.addWidget(AnsGroupBox)
main_layout.addLayout(layout_btn)

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
#Membuat fungsi
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question1 = Question('Apa makanan kesukaanmu?', 'Ayam Goreng', 'Udang Goreng', 'Ikan goreng', 'Steak')
question2 = Question('Dimana Tempat makan yang paling kamu suka?', 'Aneka Seafood', 'Aroma', 'Pecel Lele', 'bsteak')
question3 = Question('Kapan Kamu makan di luar ?', 'Weekend', 'Weekdays', 'Kapan saja', 'Senin')
list_question = []
list_question.append(question1)
list_question.append(question2)
list_question.append(question3)
index_question = 0
soal_benar = 0
total_soal = 0


answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
def set_question(q):
     lb_question.setText(q.question)
     shuffle(answers)
     answers[0].setText(q.right_answer)
     answers[1].setText(q.wrong1)
     answers[2].setText(q.wrong2)
     answers[3].setText(q.wrong3)
     lb_answer.setText(q.right_answer)

def statistik():
    global soal_benar
    global total_soal
    print('STATISTIK')
    print('Total Soal:', total_soal)
    print('Total Benar:', soal_benar)
    print('Total Salah:', total_soal - soal_benar)
    print('Akurasi Anda:', soal_benar / total_soal * 100, '%')

def next_scene():
   if btn_OK.text() == 'Answer':
        RadioGroupBox.hide()
        AnsGroupBox.show()
        btn_OK.setText('Next Question')
        global total_soal
        total_soal += 1
        check_answer() 
        statistik()
   elif btn_OK.text() == "Next Question":
        index_random = randint(0, len(list_question)-1
                               )
        set_question(list_question[index_random])

        
        AnsGroupBox.hide()
        RadioGroupBox.show()
        btn_OK.setText('Answer')
        RadioGroup.setExclusive(False)
        rbtn_1.setChecked(False)                                            
        rbtn_2.setChecked(False)  
        rbtn_3.setChecked(False)   
        rbtn_4.setChecked(False) 
        RadioGroup.setExclusive(True)  
def check_answer():
    if answers[0].isChecked():
        lb_Result.setText('Text')
        global soal_benar
        soal_benar += 1 
set_question(list_question[index_question])

    
btn_OK.clicked.connect(next_scene)
AnsGroupBox.hide()
main_win.setLayout(main_layout)                                                     
main_win.show()
app.exec_()



