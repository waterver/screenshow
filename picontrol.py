from RPi import GPIO
import time

class MOTOR():
    def __init__(self,num=0):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        self.num=num

    
    def steup(self,dirm=40,pwm=38,fre=1000):
        GPIO.setup(dirm,GPIO.OUT)
        GPIO.setup(pwm,GPIO.OUT)
        self.dirm=dirm
        self.pwm_channel=pwm
        self.p=GPIO.PWM(pwm,fre)
        self.fre=fre

    def change(self,num):
        t=self.num-num
        if t>0:
            GPIO.output(self.dirm,1)
        else:
            GPIO.output(self.dirm,0)
            t=-t
            
        step=102.6 *t/1.8*16/self.fre
        self.p.start(50)
        time.sleep(step)
        self.p.stop()
        self.num=num

