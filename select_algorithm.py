# importing libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class AlgoWindow(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)

        self.SetupUi()


    def SetupUi(self):
        self.Widgets()
        self._layout()
        self.actionButton()


    def Widgets(self):
        # Algorithm Box
        self.combo_box = QComboBox(self)

        algo_list = ["algo1", "algo2", "algo3"]

        # Adding algo to algorithm box
        self.combo_box.addItems(algo_list)


        # Select Algorithm
        self.buttonAlgSelect = QPushButton("Select Algorithm", self)

        # OK Button
        self.buttonOK = QPushButton("OK", self)
        self.buttonOK.setVisible(False)

        # creating label to
        self.label = QLabel(self)
        self.labelparam1 = QLabel(self)  ## parameter1
        self.labelparam2 = QLabel(self)
        self.labelparam3 = QLabel(self)

        # Create textbox
        self.textboxparam1 = QLineEdit(self)
        self.textboxparam1.setVisible(False)
        self.textboxparam2 = QLineEdit(self)
        self.textboxparam2.setVisible(False)
        self.textboxparam3 = QLineEdit(self)
        self.textboxparam3.setVisible(False)

    def actionButton(self):

        self.buttonAlgSelect.pressed.connect(self.find)

    def find(self):
        content = self.combo_box.currentText()
        print(content)
        if content == "algo1":
            self.labelparam1.setText("parameter-1: ")
            self.labelparam2.setText("parameter-2: ")
            self.labelparam3.setText("parameter-3: ")
            self.buttonOK.setVisible(True)
            self.textboxparam1.setVisible(True)
            self.textboxparam2.setVisible(True)
            self.textboxparam3.setVisible(True)
        elif content == "algo2":
            self.labelparam1.setText("parameter-4: ")
            self.labelparam2.setText("parameter-5: ")
            self.labelparam3.setText("parameter-6: ")
            self.buttonOK.setVisible(True)
            self.textboxparam1.setVisible(True)
            self.textboxparam2.setVisible(True)
            self.textboxparam3.setVisible(True)

        elif content == "algo3":
            self.labelparam1.setText("param7: ")
            self.labelparam2.setText("param8: ")
            self.labelparam3.setText("param9: ")
            self.buttonOK.setVisible(True)
            self.textboxparam1.setVisible(True)
            self.textboxparam2.setVisible(True)
            self.textboxparam3.setVisible(True)



    def _layout(self):
        # layout 1 for main layout
        layout1 = QVBoxLayout()

        # layout2  for algorithm box && selectalgortihm button  && ok button
        layout2 = QHBoxLayout()
        layout2.addWidget(self.combo_box)
        layout2.addWidget(self.buttonAlgSelect)
        layout2.addWidget(self.buttonOK)

        layout1.addLayout(layout2)

        # label and textbox layout
        layout3 = QFormLayout()
        layout3.addRow(self.labelparam1, self.textboxparam1)
        layout3.addRow(self.labelparam2, self.textboxparam2)
        layout3.addRow(self.labelparam3, self.textboxparam3)

        layout1.addLayout(layout3)

        # Set layout
        self.setLayout(layout1)
