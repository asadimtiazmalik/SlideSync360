import win32com.client

app = win32com.client.Dispatch("PowerPoint.Application")
objCOM = app.Presentations.Open(FileName="D:\\manan\\sync-ppt-desktop\\test.pptx", WithWindow=1)
objCOM.SlideShowWindow.View.Next()
objCOM.SlideShowWindow.View.Next()

class ppt:
    def __init__(self):
        self.objCOM = app.Presentations.Open(FileName="path_to_file",    WithWindow=1)