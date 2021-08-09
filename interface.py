from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
import datetime
import sys, os

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

    def UiComponents(self):
        self.player = QMediaPlayer()
        full_file_path = os.path.join(os.getcwd(), 'test.mp3')
        url = QUrl.fromLocalFile(full_file_path)
        content = QMediaContent(url)
        #print(content)
        self.player.setMedia(content)
        self.player.play()


class Window(QtWidgets.QMainWindow): # Just add the new pages to this, don't delete anything
    def __init__(self, parent=None):
        super().__init__(parent)
        self.stacked_widget = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.stacked_widget)
        # Modified
        self.resize(1800, 950)
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
    app = QtWidgets.QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())
