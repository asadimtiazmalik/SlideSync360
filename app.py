# from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
#
# # Only needed for access to command line arguments
# import sys
#
# # You need one (and only one) QApplication instance per application.
# # Pass in sys.argv to allow command line arguments for your app.
# # If you know you won't use command line arguments QApplication([]) works too.
# app = QApplication(sys.argv)
#
# # Create a Qt widget, which will be our window.
# # window = QWidget()
# # window = QPushButton("Push Me")
# window = QMainWindow()
# window.show()  # IMPORTANT!!!!! Windows are hidden by default.
#
# # Start the event loop.
# app.exec()
#

#
# # Your application won't reach here until you exit and the event
# # loop has stopped.

# import sys
#
# from PyQt6.QtCore import QSize, Qt
# from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
#
#
# # Subclass QMainWindow to customize your application's main window
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("My App")
#
#         button = QPushButton("Press Me!")
#         button.setCheckable(True)
#         button.clicked.connect(self.the_button_was_clicked)
#
#         # Set the central widget of the Window.
#         self.setCentralWidget(button)
#
#     def the_button_was_clicked(self):
#         print("Clicked!")
#
#
# app = QApplication(sys.argv)
#
# window = MainWindow()
# window.show()
#
# app.exec()

import sys
import time

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt
from win32gui import GetWindowText, GetForegroundWindow
import keyboard
import pygetwindow as gw


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
        self.wintext = GetWindowText(GetForegroundWindow())

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
        print('next clicked')
        not_changed = True
        while (not_changed):
            time.sleep(1)
            wintext = GetWindowText(GetForegroundWindow())

            if wintext.startswith('PowerPoint Slide Show - ['):
                # cmd = getcommand(arg_server)
                keyboard.send('space')
                not_changed = False
            # break
        print('here')

    def backClicked(self):
        print('next clicked')
        not_changed = True
        while (not_changed):
            time.sleep(1)
            wintext = GetWindowText(GetForegroundWindow())

            if wintext.startswith('PowerPoint Slide Show - ['):
                # cmd = getcommand(arg_server)
                keyboard.send('backspace')
                not_changed = False
            # break
        print('here')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setGeometry(500, 300, 600, 400)
    window.show()
    sys.exit(app.exec_())
