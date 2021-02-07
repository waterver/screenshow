from RPi import GPIO
import time

class MOTOR():
    def __init__(self,num=0,dirm=None,pwm=None,freq=1000,multifre=16):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        self.num=num
        self.dirm=dirm
        self.pwmchannel=pwm
        self.freq=freq
        self.multfre=multifre
        self.steup(self.dirm,self.pwmchannel,self.fre)


    def steup(self,dirm,pwm,fre):
        GPIO.setup(dirm,GPIO.OUT)
        GPIO.setup(pwm,GPIO.OUT)
        # self.pwm=GPIO.PWM(pwm,fre)

    def change(self,num):
        t=self.num-num
        if t==0:
            return
        #可延最短路径行动
        # if t>0 and t<= 2:
        #     GPIO.output(self.dirm,1)
        # elif t<0 and t>=-2:
        #     GPIO.output(self.dirm,0)
        #     t=-t
        # elif t==3:
        #     GPIO.output(self.dirm,0)
        #     t-=2
        # elif t==-3:
        #     GPIO.output(self.dirm,1)
        #     t+=4
        
        #在一个周期内转动
        if t>0:
            GPIO.output(self.dirm,1)
        else:
            GPIO.output(self.dirm,0)
            t=-t

        step_t=90 *t/1.8*self.multfre
        for i in range(step_t):
            GPIO.output(self.pwmchannel,1)
            time.sleep(1/2/self.freq)
            GPIO.output(self.pwmchannel,0)
            time.sleep(1/2/self.fre)

        # self.pwm.start(50)
        # time.sleep(step)
        # self.pwm.stop()
        self.num=num

class STEER():
    def __init__(self,pwmchannel=None,angle=None):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        self.pwmchannel=pwmchannel
        GPIO.setup(self.pwmchannel,GPIO.OUT)
        self.pwm=GPIO.PWM(self.pwmchannel,50)
        self.sign=0
        if angle!=None:
            self.sign=1
            self.change(angle)
        
    def change(self,angle=None):
        if self.sign==0:
            duty = 10 / 180 * angle + 2
            self.pwm.start(duty)
            self.sign=1
        else:
            duty = 10 / 180 * angle + 2
            self.pwm.ChangeDutyCycle(duty)
    

if __name__=="__main__":
    stepmoter=MOTOR(0,40,38)
    stepmoter.change(2)