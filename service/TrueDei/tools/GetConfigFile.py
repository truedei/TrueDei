from entity.ConfigDataEntity import ConfigDataEntity as CDE
#获取配置文件
cde = CDE()

def readConfigurationFileData():
    dataFile = open('conf/truedei.conf','r',encoding='utf-8')
    for line in dataFile.readlines():
        #去掉换行符
        line = line.strip('\n')
        #获取监听端口号
        if line.rfind("ListenPost", 0, len("ListenPost")) != -1:
            cde.ListenPort = (line.split(" "))[1]
        #获取监听的Ip地址
        elif line.rfind("ListenIp", 0, len("ListenIp")) != -1:
            cde.ListenIp = (line.split(" "))[1]
        # 获取监听间隔的时间
        elif line.rfind("SleepTime", 0, len("SleepTime")) != -1:
            cde.SleepTime = (line.split(" "))[1]
        # 获取客户端的连接数
        elif line.rfind("ClientNumber", 0, len("ClientNumber")) != -1:
            cde.ClientNumber = (line.split(" "))[1]

# RabbitMQ相关的配置信息
        # 获取RabbitMQ的地址
        elif line.rfind("RabbitMQHost", 0, len("RabbitMQHost")) != -1:
            cde.RabbitMQHost = (line.split(" "))[1]
        # 获取RabbitMQ的地址
        elif line.rfind("RabbitMQPost", 0, len("RabbitMQPost")) != -1:
            cde.RabbitMQPost = (line.split(" "))[1]
        # 获取RabbitMQ的地址
        elif line.rfind("RabbitMQUsername", 0, len("RabbitMQUsername")) != -1:
            cde.RabbitMQUsername = (line.split(" "))[1]
        # 获取RabbitMQ的地址
        elif line.rfind("RabbitMQPassword", 0, len("RabbitMQPassword")) != -1:
            cde.RabbitMQPassword = (line.split(" "))[1]
        # 获取监控间隔的时间
        elif line.rfind("DiskDataSleepTime", 0, len("DiskDataSleepTime")) != -1:
            cde.DiskDataSleepTime = (line.split(" "))[1]
        #RabbitMQExchange
        elif line.rfind("RabbitMQExchange", 0, len("RabbitMQExchange")) != -1:
            cde.RabbitMQExchange = (line.split(" "))[1]
        #RabbitMQDiskDataRouting_key
        elif line.rfind("RabbitMQDiskDataRouting_key", 0, len("RabbitMQDiskDataRouting_key")) != -1:
             cde.RabbitMQDiskDataRouting_key = (line.split(" "))[1]
        # RabbitMQDiskWarningRouting_key
        elif line.rfind("RabbitMQDiskWarningRouting_key", 0, len("RabbitMQDiskWarningRouting_key")) != -1:
             cde.RabbitMQDiskWarningRouting_key = (line.split(" "))[1]

    return cde

# if __name__ == '__main__':
#     readConfigurationFileData()
