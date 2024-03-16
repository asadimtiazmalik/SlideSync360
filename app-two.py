import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout
from PyQt5.QtCore import Qt
import keyboard
from win32gui import GetWindowText, GetForegroundWindow, IsWindowVisible, EnumWindows


class CircularButton(QPushButton):
    def __init__(self, text):
        super().__init__(text)
        self.setFixedSize(200, 200)
        self.setStyleSheet(
            "border-radius: 50px; background-color: #4CAF50; color: white; font-size: 20px;"
        )


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Sync Slides')

        self.next_button = CircularButton('Next')
        self.back_button = CircularButton('Back')

        self.next_button.clicked.connect(self.nextClicked)
        self.back_button.clicked.connect(self.backClicked)

        layout = QHBoxLayout()
        layout.addWidget(self.back_button, alignment=Qt.AlignCenter)
        layout.addWidget(self.next_button, alignment=Qt.AlignCenter)

        self.setLayout(layout)

    def nextClicked(self):
        print('Next clicked')
        wintext = self.getPowerPointWindowTitle()
        print('Window Title:', wintext)
        if wintext.startswith('PowerPoint Slide Show - ['):
            print('Sending space key')
            keyboard.send('space')
        else:
            print('Not in PowerPoint Slide Show')

    def backClicked(self):
        print('Back clicked')
        wintext = self.getPowerPointWindowTitle()
        print('Window Title:', wintext)
        if wintext.startswith('PowerPoint Slide Show - ['):
            print('Sending backspace key')
            keyboard.send('backspace')
        else:
            print('Not in PowerPoint Slide Show')

    @classmethod
    def getPowerPointWindowTitle(cls):
        if not cls.ppt_window_title:
            try:
                def enumHandler(hwnd, lParam):
                    if IsWindowVisible(hwnd):
                        text = GetWindowText(hwnd)
                        if text.startswith("PowerPoint Slide Show"):
                            lParam.append(text)
                    return True

                ppt_titles = []
                EnumWindows(enumHandler, ppt_titles)
                cls.ppt_window_title = ppt_titles[0] if ppt_titles else ""
            except Exception as e:
                print("Error:", e)
        return cls.ppt_window_title

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setGeometry(500, 300, 600, 400)
    window.show()
    sys.exit(app.exec_())
