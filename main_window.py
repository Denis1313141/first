from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QMessageBox, QLabel, QHBoxLayout, QVBoxLayout, QGroupBox, QSpinBox, QPushButton,QButtonGroup
from random import shuffle

app = QApplication([])

window = QWidget()
window.resize(700, 400)
window.move(1000, 299)
window.setWindowTitle("Memory Card")

RadioGroupBox = QGroupBox("Answers:")
RadioGroup = QButtonGroup()

rb_1 = QRadioButton("apple")
rb_2 = QRadioButton("building")
rb_3 = QRadioButton("orange")
rb_4 = QRadioButton("screwdriver")

RadioGroup.addButton(rb_1)
RadioGroup.addButton(rb_2)
RadioGroup.addButton(rb_3)
RadioGroup.addButton(rb_4)

btn_Next = QPushButton("Continue")
btn_Menu = QPushButton("Menu")
btn_Rest = QPushButton("Rest")

box_Minutes = QSpinBox()
box_Minutes.setValue(30)

text = QLabel("яблуко")

window.show()