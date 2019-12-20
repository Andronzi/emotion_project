from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication, QLabel, QVBoxLayout)
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QIcon, QImage, QPixmap
import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
import find_face_video as f
import emotion_video as e
from first import Ui_Form


class QtCapture(QWidget):
    global a
    a = 0

    def __init__(self, *args):
        super(QWidget, self).__init__()

        self.cap = cv2.VideoCapture(*args)

        self.video_frame = QLabel()
        lay = QVBoxLayout()
        lay.addWidget(self.video_frame)
        self.setLayout(lay)

    def nextFrameSlot(self):
        ret, frame = self.cap.read()
        if a == 1:
            frame = f.find_face(frame)
        elif a == 2:
            image = e.format_image(frame)
            frame = e.emotions(image, frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.video_frame.setPixmap(pix)

    def start(self):
        global a
        a = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.nextFrameSlot)
        self.timer.start(1000./30)  # задаем fps

    def stop(self):
        self.timer.stop()

    def deleteLater(self):
        self.cap.release()
        super(QWidget, self).deleteLater()

    def key_points(self):
        global a
        a = 1
        self.timer = QTimer()
        self.timer.timeout.connect(self.nextFrameSlot)
        self.timer.start(1000./30)  # задаем fps

    def emotion(self):
        global a
        a = 2
        self.timer = QTimer()
        self.timer.timeout.connect(self.nextFrameSlot)
        self.timer.start(1000./30)  # задаем fps

class ControlWindow(QWidget):

    def label_happy(self):
        self.window = QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.window)
        self.ui.retranslateUi(self.window)
        self.label = QLabel(self.window)
        self.label.setPixmap(QPixmap('1.jpg'))
        self.label.setGeometry(400, 20, 400, 320)

        self.ui.pushButton.clicked.connect(lambda: self.label_angry())
        self.ui.pushButton_2.clicked.connect(lambda: self.label_surprised())
        self.ui.pushButton_3.clicked.connect(lambda: self.label_happy())

        self.window.show()

    def label_angry(self):
        self.window = QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.window)
        self.ui.retranslateUi(self.window)
        self.label = QLabel(self.window)
        self.label.setPixmap(QPixmap('3.jpg'))
        self.label.setGeometry(400, 20, 400, 320)

        self.ui.pushButton.clicked.connect(lambda: self.label_angry())
        self.ui.pushButton_2.clicked.connect(lambda: self.label_surprised())
        self.ui.pushButton_3.clicked.connect(lambda: self.label_happy())

        self.window.show()

    def label_surprised(self):
        self.window = QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.window)
        self.ui.retranslateUi(self.window)
        self.label = QLabel(self.window)
        self.label.setPixmap(QPixmap('4.jpg'))
        self.label.setGeometry(400, 20, 400, 320)
        self.ui.pushButton.clicked.connect(lambda: self.label_angry())
        self.ui.pushButton_2.clicked.connect(lambda: self.label_surprised())
        self.ui.pushButton_3.clicked.connect(lambda: self.label_happy())
        self.window.show()


    def new(self, parent=None):
        self.window = QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.window)
        self.ui.retranslateUi(self.window)
        self.ui.pushButton.clicked.connect(lambda: self.label_angry())
        self.ui.pushButton_2.clicked.connect(lambda: self.label_surprised())
        self.ui.pushButton_3.clicked.connect(lambda: self.label_happy())
        # self.setLayout(self.vbox)
        self.window.show()

    def __init__(self, *args):
        QWidget.__init__(self)
        self.capture = None
        self.cap = cv2.VideoCapture(*args)

        self.video_frame = QLabel()
        lay = QVBoxLayout()
        lay.addWidget(self.video_frame)

        self.start_button = QPushButton('зеркало')
        self.start_button.clicked.connect(self.startCapture)
        self.quit_button = QPushButton('выход')
        self.quit_button.clicked.connect(self.endCapture)
        self.new_button = QPushButton('Обучение')
        self.new_button.clicked.connect(self.new)
        self.key_points_button = QPushButton('точки')
        self.emotion_button = QPushButton('эмоции')
        self.end_button = QPushButton('пауза')

        vbox = QVBoxLayout(self)
        vbox.addWidget(self.start_button)
        vbox.addWidget(self.end_button)
        vbox.addWidget(self.key_points_button)
        vbox.addWidget(self.new_button)
        vbox.addWidget(self.emotion_button)
        vbox.addWidget(self.quit_button)
        self.setLayout(vbox)
        self.setWindowTitle('управление')
        self.setGeometry(100, 100, 220, 200)
        self.show()


    def startCapture(self):
        if not self.capture:
            self.capture = QtCapture(0)
            self.end_button.clicked.connect(self.capture.stop)
            self.key_points_button.clicked.connect(self.capture.key_points)
            self.emotion_button.clicked.connect(self.capture.emotion)
            # self.capture.setFPS(1)
            self.capture.setParent(self)
            self.capture.setWindowFlags(Qt.Tool)
        self.capture.start()
        self.capture.show()


    def endCapture(self):
        self.capture.deleteLater()
        self.capture = None
        QApplication.quit()


if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    window = ControlWindow()
    sys.exit(app.exec_())
