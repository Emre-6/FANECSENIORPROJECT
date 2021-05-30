import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QHBoxLayout, QVBoxLayout, QCalendarWidget
from PyQt5.QtCore import Qt
import media_player, select_algorithm

# Subclass QMainWindow to customise your application's main window
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
      #  super().__init__()

        self.SetupUİ()

    def SetupUİ(self):

        self.setWindowTitle("FANEC")
        self.setGeometry(300, 300, 800, 500)
        self.widgets()
        self._layout()

    def widgets(self):
        # Central Widget
        self.centralWidget = QtWidgets.QWidget()
        self.setCentralWidget(self.centralWidget)

        # Media Player Widget
        self.mediaPlayerWidget = media_player.MediaPlayer()


        # Algorithm Box Widget
        self.algo_box = select_algorithm.AlgoWindow()




    def _layout(self):

       # Media PLayer Area layout
        self.MediaPlayerArea = QtWidgets.QWidget(self.centralWidget)
        self.MediaPlayerArea.setGeometry(0, 0, 500, 500)
        self.layoutMediaPlayer = QtWidgets.QVBoxLayout(self.MediaPlayerArea)

        self.layoutMediaPlayer.addWidget(self.mediaPlayerWidget)
        self.layoutMediaPlayer.addWidget(self.algo_box)
