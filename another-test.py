import keyboard
import pygetwindow as gw
print(gw.getAllTitles())
notepadWindow = gw.getWindowsWithTitle('PowerPoint Slide Show -')[0]
# notepadWindow.show()
# notepadWindow.activate()
# keyboard.send('space')
print(notepadWindow)