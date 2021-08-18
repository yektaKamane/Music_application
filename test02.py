import sys, os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, \
                            QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

# full_file_path = os.path.join(os.getcwd(), 'test.mp3')
# url = QUrl.fromLocalFile(full_file_path)
# content = QMediaContent(url)
#content = QMediaContent(QUrl("https://p.scdn.co/mp3-preview/8226164717312bc411f8635580562d67e191a754?cid=9535173dce7c4a5d8049be9aeeb229ba"))


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.window_width, self.window_height = 800, 120
        self.setMinimumSize(self.window_width, self.window_height)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        btn = QPushButton('Play', clicked=self.playAudioFile)
        self.layout.addWidget(btn)

        volumeControl = QHBoxLayout()
        self.layout.addLayout(volumeControl)

        btnVolumeUp = QPushButton('+', clicked=self.volumeUp)
        btnVolumeDown = QPushButton('-', clicked=self.volumeDown)
        butVolumeMute = QPushButton('Mute', clicked=self.volumeMute)
        volumeControl.addWidget(btnVolumeUp)
        volumeControl.addWidget(butVolumeMute)
        volumeControl.addWidget(btnVolumeDown)

        self.player = QMediaPlayer()

    def volumeUp(self):
        currentVolume = self.player.volume() #
        print(currentVolume)
        self.player.setVolume(currentVolume + 5)

    def volumeDown(self):
        currentVolume = self.player.volume() #
        print(currentVolume)
        self.player.setVolume(currentVolume - 5)

    def volumeMute(self):
        self.player.setMuted(not self.player.isMuted())

    def playAudioFile(self):
        options = webdriver.ChromeOptions()
        # options.add_argument('headless')
        # options.add_argument('window-size=1920x1080')
        # options.add_argument("disable-gpu")

        driver = webdriver.Chrome(executable_path = 'C:\\Users\\lenovo\\Desktop\\Spotify-project\\chromedriver.exe', options=options)
        driver.get('https://freemp3cloud.com/')

        assert "Music" in driver.title

        elem = driver.find_element_by_name("searchSong")
        elem.clear()
        elem.send_keys("Maneskin")
        elem.send_keys(Keys.RETURN)


        soup = BeautifulSoup(driver.page_source, 'lxml')
        search_res = soup.find('div', class_ = 'play-item')
        track_res = search_res.find('div', class_ = 'play-ctrl')

        url = track_res.get('data-src')
        print((track_res).encode('utf8'))
        url = str(url)
        print(url)

        content = QMediaContent(QUrl(url))
        self.player.setMedia(content)
        self.player.play()

if __name__ == '__main__':
    # don't auto scale when drag app to a different monitor.
    # QApplication.setAttribute(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)

    app = QApplication(sys.argv)
    app.setStyleSheet('''
        QWidget {
            font-size: 30px;
        }
    ''')

    myApp = MyApp()
    myApp.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')
