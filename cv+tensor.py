import cv2 as cv
from tensorflow.lite import Interpreter
# from tflite_runtime.interpreter import Interpreter
import numpy as np
import time


class DETECT_WITH_CV():
    def __init__(self,model=None):
        #预热摄像头,并获取背景
        # self.bs = cv2.createBackgroundSubtractorKNN(detectShadows=True)
        # time1=time.time()
        self.camera=cv.VideoCapture(0)
        self.camera.set(3,1000)
        self.camera.set(4,750)
        self.camera.set(5,25)
        self.success,self.background=self.camera.read()
        #
        # print(time2-time1)
        # self.mask=bs.apply(self.background)
        # self.th = cv2.threshold(self.mask.copy(), 244, 255, cv.THRESH_BINARY)[1]
        # 加载模型
        self.model=model
        self.interpreter=Interpreter(model_path=self.model)
        self.interpreter.allocate_tensors()
        self.input=self.interpreter.get_input_details()
        print(str(self.input))
        print(str(self.interpreter.get_output_details()))


    def test_cv(self):
        
        while self.camera.isOpened():
            self.success,self.frame=self.camera.read()
            #中值去噪
            self.frame=cv.medianBlur(self.frame,1)
            # self.frame=cv.fastNlMeansDenoisingColored(self.frame,None,5,5,7,21)
            cv.imshow("test1",self.frame)
            if cv.waitKey(25)==ord('q'):
                self.camera.release()

    def get_and_return(self):
        #获取镜像的两张照片提高准确度
        #树莓派目前版本的opencv无法连续读取图像，尝试解决中

        # self.camera=cv.VideoCapture(0)
        # self.success=self.camera.grab()
        # self.success,self.frame=self.camera.retrieve()

        self.success,self.frame=self.camera.read()
        # self.frame=cv.fastNlMeansDenoisingColored(self.frame,None,10,10,7,21)
        self.frame1=cv.cvtColor(self.frame,cv.COLOR_BGR2RGB)
        self.frame1=cv.resize(self.frame1,(224,224))
        self.frame=cv.medianBlur(self.frame,1)
        self.frame2=cv.flip(self.frame1,0)
        
        self.img1=np.array(self.frame1).astype('float32')
        self.img2=np.array(self.frame2).astype('float32')
        self.img1=np.expand_dims(self.img1,axis=0)
        self.img2=np.expand_dims(self.img2,axis=0)

        #开始识别，调用模型
        self.interpreter.set_tensor(self.input[0]['index'],self.img1)
        self.interpreter.invoke()
        self.output_data1 = interpreter.get_tensor(output_details[0]['index'])
        self.result1=np.squeeze(self.output_data1)
        self.return_num1=(np.where(self.result1==np.max(self.result1)))[0][0]

        self.interpreter.set_tensor(self.input[0]['index'],self.img2)
        self.interpreter.invoke()
        self.output_data2 = interpreter.get_tensor(output_details[0]['index'])
        self.result2=np.squeeze(self.output_data2)
        self.return_num2=(np.where(self.result2==np.max(self.result2)))[0][0]

        #进行判定，当两次判断不一致时给出准确度更高的一个答案
        if self.return_num1==self.return_num2:
            return self.return_num1
        elif self.result1[self.return_num1]>self.result2[self.return_num2]:
            return self.return_num1
        else:
            return self.return_num2
        
if __name__=="__main__":
    test=DETECT_WITH_CV("../model-mobile.tflite")
    test.test_cv()