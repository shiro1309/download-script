import webbrowser as wb, pyautogui as pgi, json, time

time.sleep(2)

#pgi.moveTo(1278, 284)

print(pgi.size())

class Combo:
    def page_close(self):
        pgi.keyDown("ctrl")
        pgi.press("w")
        
    def download_click(self):
        pgi.moveTo(1278, 284)
        time.sleep(5)
        pgi.moveTo(1650, 600)
        
while False:
    print(1)