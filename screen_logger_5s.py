# Requires pywin32
# pip install pywin32
import time  
import win32api
import win32con
import win32gui
import win32ui
import os

tm = 1
user = os.getlogin()
file = user + str(tm)

while True:
	def get_dimensions():
	    width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
	    height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
	    left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
	    top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)
	    return (width, height, left, top)


	def screenshot(name= file):
	    # Get a handle for the entire desktop, including the viewable area across
	    # multiple monitors.
	    hdesktop = win32gui.GetDesktopWindow()
	    width, height, left, top = get_dimensions()
	    
	    desktop_dc = win32gui.GetWindowDC(hdesktop)
	    img_dc = win32ui.CreateDCFromHandle(desktop_dc)
	    mem_dc = img_dc.CreateCompatibleDC()

	    screenshot = win32ui.CreateBitmap()
	    screenshot.CreateCompatibleBitmap(img_dc, width, height)
	    mem_dc.SelectObject(screenshot)
	    # Store a bit-for-bit copy on the desktop.
	    mem_dc.BitBlt((0, 0), (width, height), img_dc, (left, top), win32con.SRCCOPY)
	    screenshot.SaveBitmapFile(mem_dc, f"{tm}.bmp")

	    mem_dc.DeleteDC()
	    win32gui.DeleteObject(screenshot.GetHandle())
	  
	    

	def run():
	    screenshot()
	    with open("{tm}.bmp") as f:
	        img = f.read()
	    return img

	screenshot()
	tm += 1
	time.sleep(5.0)


	#if __name__ == "__main__":
        
	   

 

