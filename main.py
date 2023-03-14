import utime
import time
from srv import Servo

serv = Servo(28,50,0,180,1350,7500)       
z=0
if __name__ == '__main__':
    while True:
        if z<1:
            if serv.durum==True:  
                time.sleep(2)
                print("Servo sürülebilir.")
                time.sleep(1)
            else:
                print("Servo sürülemez.")
                serv.deinit()
            z+=1
        print("Sağa dönüyor ...")
        for i in range(0,180,10):
            serv.aciGit(i)
            utime.sleep(0.1)
        print("Sola dönüyor ...")
        for i in range(180,0,-10):
            serv.aciGit(i)
            utime.sleep(0.1)