import _thread
import time
from tools.GetConfigFile import readConfigurationFileData as RCFD #加载配置信息
from rabbitmq.TopicPublicSendMassage import topicPublicSendMassage #发送消息
from tools.GetDiskData import getDiskData

def main():
    rcfg = RCFD()  # 配置信息
    gdd = getDiskData()
    diskDataSleepTime = int(rcfg.DiskDataSleepTime) #diskData Time
    tpsm = topicPublicSendMassage()

    def diskData( threadName, delay):
        while 1:
            # message = "监控disk数据:" + str(time.time()) + str
            message =  gdd.__str__() + "\r\n"
            print(message)
            tpsm.__sendDiskDataMsg__(message)
            time.sleep(diskDataSleepTime)
            str = ""
            pass

    # 为线程定义一个函数
    def diskWarning( threadName, delay):
        while 1:
            time.sleep(diskDataSleepTime)
            message = gdd.__str__() + "\r\n"
            # message = "监控disk报警:" + str(time.time())
            print(message)
            tpsm.__sendDiskWarningMsg__(message)
            pass

    # 创建两个线程
    try:
        #监控disk data线程
        _thread.start_new_thread(diskData,("Thread-diskData",diskDataSleepTime))
        #监控disk 报警线程
        _thread.start_new_thread(diskWarning,("Thread-diskWarning",diskDataSleepTime))
    except:
       print ("Error: 无法启动TrueDei")

    #不间断监控
    while 1:
       pass

if __name__ == '__main__':
    main()


