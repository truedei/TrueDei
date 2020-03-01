class ConfigDataEntity():
#Socket配置
    #端口号
    ListenPort = 0
    #监听Ip地址
    ListenIp = ""
    #间隔时间  单位：秒 默认60秒
    SleepTime = 0
    #客户端连接数 默认10个
    ClientNumber = 0

# RabbitMQ相关的配置信息
    # 你的RabbitMQ的地址
    RabbitMQHost=""
    # RabbitMQ端口号
    RabbitMQPost=0
    # 创建的账号，当然了也可以使用默认的guest账号，密码也是guest
    RabbitMQUsername=""
    # 账号的密码
    RabbitMQPassword=""

#监控的休眠的间隔时间
    DiskDataSleepTime=0

    #RabbitMQ  exchange
    RabbitMQExchange =""
    #RabbitMQ  routing_key
    RabbitMQDiskDataRouting_key =""
    #RabbitMQ Disk Warning Routing_key
    RabbitMQDiskWarningRouting_key = ""

    def __init__(self):
        pass
    # def __init__(self,listenPort,listenIp):
    #     self.listenPort = listenPort
    #     self.listenIp = listenIp

    def getData(self):
        print(self.ListenIp,self.ListenPort)

