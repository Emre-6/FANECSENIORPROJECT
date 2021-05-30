from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QPalette
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QFileDialog, QStyle, QVBoxLayout, QHBoxLayout, QSizePolicy, QLabel, QSlider, QPushButton, \
    QWidget


class MediaPlayer(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)

        # self.setWindowTitle("Media Player")
        # self.setGeometry(350, 100, 100, 100)
        # self.setWindowIcon(QIcon("mediaPlayerIcon.png"))

        palette = self.palette()
        palette.setColor(QPalette.Background, Qt.black)
        self.setPalette(palette)

        self.init_ui()

        # self.show()

    def init_ui(self):
        # Create MediaPlayer Object
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

        # Create Videowidget Object
        videowidget = QVideoWidget()

        # Create Open Button
        openBtn = QPushButton("Open Video")
        openBtn.clicked.connect(self.open_file)

        # Create button for Playing
        self.playBtn = QPushButton()
        self.playBtn.setEnabled(False)
        self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playBtn.clicked.connect(self.play_video)

        # Create  Media Player buttons
        # Volume Button  mute/unmute
        self.buttonVolume = QPushButton(self)
        self.buttonVolume.clicked.connect(self.volume_mute)
        self.buttonVolume.setIcon(QtGui.QIcon('icons/unmute.png'))
        # Forward Button
        self.buttonForward = QPushButton('Forward', self)
       # self.buttonForward.setIcon(QtGui.QIcon("icons/forward.ico"))


        self.buttonBackward = QPushButton('Backward', self)
        self.buttonFrameForward = QPushButton('FrameForward', self)
        self.buttonFrameBackward = QPushButton('FrameBackward', self)

        layout_button = QtWidgets.QHBoxLayout()
       # layout_button.addWidget(self.buttonVolume)
        layout_button.addWidget(self.buttonForward)
        layout_button.addWidget(self.buttonBackward)
        layout_button.addWidget(self.buttonFrameForward)
        layout_button.addWidget(self.buttonFrameBackward)

        # self.setLayout(layout_button)

        # Create Slider
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0, 0)
        self.slider.sliderMoved.connect(self.set_position)

        # Create Label
        self.label = QLabel()
        self.label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)

        # Create Hbox layout
        hboxLayout = QHBoxLayout()
        hboxLayout.setContentsMargins(0, 0, 0, 0)

        # Media Player Volume Slider
        self.volumeSlider = QSlider(Qt.Horizontal)
        self.volumeSlider.setMaximum(100)
        self.volumeSlider.setValue(100)
        self.volumeSlider.sliderMoved.connect(self.volume_change)


        # Set Widget to the hbox layout
        hboxLayout.addWidget(openBtn)
        hboxLayout.addWidget(self.playBtn)
        hboxLayout.addWidget(self.slider, 30)
        hboxLayout.addWidget(self.volumeSlider, 10)
        hboxLayout.addWidget(self.buttonVolume)

        # Create vbox layout
        vboxLayout = QVBoxLayout()
        vboxLayout.addWidget(videowidget)
        vboxLayout.addLayout(hboxLayout)
        vboxLayout.addLayout(layout_button)
        vboxLayout.addWidget(self.label)
        # vboxLayout.setGeometry(50, 100, 300, 100)

        self.setLayout(vboxLayout)

        self.mediaPlayer.setVideoOutput(videowidget)

        # media player signals
        self.mediaPlayer.stateChanged.connect(self.mediastate_changed)
        self.mediaPlayer.positionChanged.connect(self.position_changed)
        self.mediaPlayer.durationChanged.connect(self.duration_changed)

    # self.mediaPlayer.volumeChanged.connect(self.volume_change)

    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open Video")

        if filename != '':
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
            self.playBtn.setEnabled(True)

    def play_video(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()

    def mediastate_changed(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))

        else:
            self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))

    def position_changed(self, position):
        self.slider.setValue(position)

    def duration_changed(self, duration):
        self.slider.setRange(0, duration)
        print(duration)

    def set_position(self, position):
        self.mediaPlayer.setPosition(position)

    def volume_mute(self):
        if self.mediaPlayer.volume() == 0:
            self.mediaPlayer.setVolume(100)
            self.volumeSlider.setValue(100)
            self.buttonVolume.setIcon(QtGui.QIcon('icons/unmute.png'))

        elif self.mediaPlayer.volume() == 100:
            self.mediaPlayer.setVolume(0)
            self.volumeSlider.setValue(0)
            self.buttonVolume.setIcon(QtGui.QIcon('icons/mute.ico'))

    def volume_change(self, value):
        print(value)
        self.mediaPlayer.setVolume(value)

    def forward_changed(self):
        pass

    def backward_changed(self):
        pass

    def frame_forward(self):
        pass

    def frame_backward(self):
        pass