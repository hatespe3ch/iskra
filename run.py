import os,time,sys,threading
def i():
    os.system("python3 bot.py")
    time.sleep(600)
    i()
t = threading.Thread(target=1)
t.start()