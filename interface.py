from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *

import datetime
import sys, os

from test01 import Spotify

# import test01
# some random url
# 'https://open.spotify.com/artist/1BAdSa5cdtCNLbvT7gWmtJ'
# 'https://open.spotify.com/track/4pt5fDVTg5GhEvEtlz9dKk?si=8a9d35fdc5294dd5'

class PageWindow(QtWidgets.QMainWindow): # Do not touch this
    gotoSignal = QtCore.pyqtSignal(str)
    def goto(self, name):
        self.gotoSignal.emit(name)

class MainPage(PageWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Home")
        self.UiComponents()

    def sync_search(self, text):
        print(spotify.search_artist(text))

    def playlist_bar_printer(self):
        for i in range(17):
            self.commandLinkButton = QtWidgets.QCommandLinkButton(self.scrollAreaWidgetContents_pb)
            self.commandLinkButton.setMaximumSize(QtCore.QSize(240, 40))
            self.commandLinkButton.setObjectName("commandLinkButton")
            self.commandLinkButton.setText("playlist # " + str(i+1))
            icon = QtGui.QIcon.fromTheme("n")
            self.commandLinkButton.setIcon(icon)
            self.commandLinkButton.setStyleSheet("color: rgb(179, 179, 179);")
            font = QtGui.QFont()
            font.setFamily("Visby Round CF")
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.commandLinkButton.setFont(font)
            self.gridLayout_pb.addWidget(self.commandLinkButton, i, 0, 1, 1, QtCore.Qt.AlignTop)

        self.scrollArea_playlistBar.setWidget(self.scrollAreaWidgetContents_pb)
        self.vertical_playlistBar.addWidget(self.scrollArea_playlistBar, 0, QtCore.Qt.AlignTop)

    def UiComponents(self):
        self.setStyleSheet("border-radius: 0px;\n""background-color: rgb(35, 35, 35);")
        self.upper_menu_frame = QtWidgets.QFrame(self)
        self.upper_menu_frame.setGeometry(QtCore.QRect(0, 0, 1921, 60))
        self.upper_menu_frame.setStyleSheet("background-color: rgb(47, 47, 47);\n""border-radius: 0px;")
        self.upper_menu_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.upper_menu_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.upper_menu_frame.setObjectName("upper_menu_frame")
        self.right_menu_frame = QtWidgets.QFrame(self)
        self.right_menu_frame.setGeometry(QtCore.QRect(0, 60, 290, 941))
        self.right_menu_frame.setStyleSheet("background-color: rgb(35, 35, 35);\n""border-right-color: rgb(0, 0, 0);\n""border-radius: 0px;")
        self.right_menu_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.right_menu_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.right_menu_frame.setObjectName("right_menu_frame")
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(8)
        shadow.setColor(QColor(0, 0, 0, 16))
        shadow.setOffset(2,0)
        self.right_menu_frame.setGraphicsEffect(shadow)
        self.search_input = QtWidgets.QLineEdit(self.right_menu_frame)
        self.search_input.setGeometry(QtCore.QRect(30, 30, 230, 40))
        font = QtGui.QFont()
        font.setFamily("Visby Round CF")
        font.setPointSize(9)
        self.search_input.setFont(font)
        self.search_input.setStyleSheet("border-radius: 20px;\n""color: rgb(115, 115, 115);\n""background-color: rgb(30, 30, 30);padding-left: 20px;")
        self.search_input.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.search_input.setClearButtonEnabled(True)
        self.search_input.setObjectName("search_input")
        # Synch Search
        self.search_input.textChanged.connect(lambda ch : self.sync_search(self.search_input.text()))
        self.Home_button = QtWidgets.QCommandLinkButton(self.right_menu_frame)
        self.Home_button.setGeometry(QtCore.QRect(40, 100, 71, 48))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Home_button.setFont(font)
        self.Home_button.setStyleSheet("color: rgb(179, 179, 179);")
        icon = QtGui.QIcon.fromTheme("n")
        self.Home_button.setIcon(icon)
        self.Home_button.setObjectName("Home_button")
        self.Library_button = QtWidgets.QCommandLinkButton(self.right_menu_frame)
        self.Library_button.setGeometry(QtCore.QRect(40, 150, 121, 48))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Library_button.setFont(font)
        self.Library_button.setStyleSheet("color: rgb(179, 179, 179);")
        icon = QtGui.QIcon.fromTheme("n")
        self.Library_button.setIcon(icon)
        self.Library_button.setObjectName("Library_button")
        self.liked_songs_button = QtWidgets.QCommandLinkButton(self.right_menu_frame)
        self.liked_songs_button.setGeometry(QtCore.QRect(40, 200, 121, 48))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.liked_songs_button.setFont(font)
        self.liked_songs_button.setStyleSheet("color: rgb(179, 179, 179);")
        icon = QtGui.QIcon.fromTheme("n")
        self.liked_songs_button.setIcon(icon)
        self.liked_songs_button.setObjectName("liked_songs_button")

        self.playlist_label = QtWidgets.QCommandLinkButton(self.right_menu_frame)
        self.playlist_label.setGeometry(QtCore.QRect(40, 300, 121, 48))
        font = QtGui.QFont()
        font.setFamily("Visby Round CF")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(65)
        self.playlist_label.setFont(font)
        self.playlist_label.setStyleSheet("color: rgb(115, 115, 115);")
        icon = QtGui.QIcon.fromTheme("n")
        self.playlist_label.setIcon(icon)
        self.playlist_label.setObjectName("playlist_label")
        self.new_playlist_button = QtWidgets.QPushButton(self.right_menu_frame)
        self.new_playlist_button.setGeometry(QtCore.QRect(50, 360, 191, 45))
        font = QtGui.QFont()
        font.setFamily("Visby Round CF")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.new_playlist_button.setFont(font)
        self.new_playlist_button.setStyleSheet("background-color: rgb(45, 45, 45);\n""color: rgb(115, 115, 115);")

        self.verticalLayout_playlistBar = QtWidgets.QWidget(self.right_menu_frame)
        self.verticalLayout_playlistBar.setGeometry(QtCore.QRect(9, 429, 271, 381))
        self.verticalLayout_playlistBar.setObjectName("verticalLayoutWidget")
        self.vertical_playlistBar = QtWidgets.QVBoxLayout(self.verticalLayout_playlistBar)
        self.vertical_playlistBar.setContentsMargins(0, 0, 0, 0)
        self.vertical_playlistBar.setObjectName("verticalLayout")
        self.scrollArea_playlistBar = QtWidgets.QScrollArea(self.verticalLayout_playlistBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_playlistBar.sizePolicy().hasHeightForWidth())
        self.scrollArea_playlistBar.setSizePolicy(sizePolicy)
        self.scrollArea_playlistBar.setWidgetResizable(True)
        self.scrollArea_playlistBar.setObjectName("scrollArea")
        self.scrollArea_playlistBar.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_playlistBar.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollAreaWidgetContents_pb = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_pb.setGeometry(QtCore.QRect(0, 0, 269, 156))
        self.scrollAreaWidgetContents_pb.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_pb = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_pb)
        self.gridLayout_pb.setObjectName("gridLayout")
        self.playlist_bar_printer()

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Home"))
        self.search_input.setPlaceholderText(_translate("Form", "Search..."))
        self.Home_button.setText(_translate("Form", "Home"))
        self.Library_button.setText(_translate("Form", "Your library"))
        self.liked_songs_button.setText(_translate("Form", "Liked songs"))
        self.playlist_label.setText(_translate("Form", "Playlists"))
        self.new_playlist_button.setText(_translate("Form", "New Playlist"))


class Window(QtWidgets.QMainWindow): # Just add the new pages to this, don't delete anything
    def __init__(self, parent=None):
        super().__init__(parent)
        self.stacked_widget = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.stacked_widget)
        # Modified
        self.resize(1900, 980)
        self.m_pages = {}
        # Register all the pages of app
        self.register(MainPage(), "main")
        # Fisrt page to be
        self.goto("main")

    def register(self, widget, name):
        self.m_pages[name] = widget
        self.stacked_widget.addWidget(widget)
        if isinstance(widget, PageWindow):
            widget.gotoSignal.connect(self.goto)

    @QtCore.pyqtSlot(str)
    def goto(self, name):
        if name in self.m_pages:
            widget = self.m_pages[name]
            widget.UiComponents()
            self.stacked_widget.setCurrentWidget(widget)
            self.setWindowTitle(widget.windowTitle())

if __name__ == "__main__":
    spotify = Spotify()

    app = QtWidgets.QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())
