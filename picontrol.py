from RPi import GPIO
import time

class MOTOR():
    def __init__(self,num=0,dirm=None,pwm=None,fre=1000):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        self.num=num
        self.dirm=dirm
        self.pwmchannel=pwm
        self.fre=fre
        self.steup(self.dirm,self.pwmchannel,self.fre)
    
    def steup(self,dirm,pwm,fre):
        GPIO.setup(dirm,GPIO.OUT)
        GPIO.setup(pwm,GPIO.OUT)
        self.pwm=GPIO.PWM(pwm,fre)

    def change(self,num):
        t=self.num-num
        if t>0 and t<= 2:
            GPIO.output(self.dirm,1)
        elif t<0 and t>=-2:
            GPIO.output(self.dirm,0)
            t=-t
        elif t==3:
            GPIO.output(self.dirm,0)
            t-=2
        else:
            GPIO.output(self.dirm,1)
            t+=2
            
        step=102.6 *t/1.8*16/self.fre
        self.pwm.start(50)
        time.sleep(step)
        self.pwm.stop()
        self.num=num

if __name__=="__main__":
    stepmoter=MOTOR(0,40,38)
    stepmoter.change(2)