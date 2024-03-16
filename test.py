import win32api
import win32gui
import win32con

def getShell():
    thelist = []
    def findit(hwnd,ctx):
        print(f'HWND {hwnd} found - title {win32gui.GetWindowText(hwnd)}')
        if win32gui.GetWindowText(hwnd).startswith('PowerPoint Slide Show - ['): # check the title
            thelist.append(hwnd)

    win32gui.EnumWindows(findit,None)
    return thelist

b = getShell()
print(b) # b is the list of hwnd,contains those windows title is "Windows PowerShell"
temp = win32api.PostMessage(b[0], win32con.WM_CHAR, 0x20, 0)
window = win32gui.GetWindow(b[0], win32con.GW_CHILD)
temp = win32api.PostMessage(window, win32con.WM_CHAR, 0x20, 0)
print(temp)