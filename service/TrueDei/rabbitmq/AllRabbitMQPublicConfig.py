import pika
import sys
from tools.GetConfigFile import readConfigurationFileData as RCFD #加载配置信息

# 类定义
class getRabbitMQPublicConf:

    connection = ""

    def __getRabbitMQChannel__(self):
        rcfg = RCFD()  # 配置信息

        # 你的RabbitMQ的地址
        host = rcfg.RabbitMQHost
        # RabbitMQ端口号
        post = rcfg.RabbitMQPost
        # 创建的账号，当然了也可以使用默认的guest账号，密码也是guest
        username = rcfg.RabbitMQUsername
        # 账号的密码
        password = rcfg.RabbitMQPassword

        # 创建一个有凭证的新实例
        credentials = pika.PlainCredentials(username, password)
        # 使用凭证连接RabbitMQ服务器
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host, post, credentials=credentials))
        # 声明一个管道
        channel = self.connection.channel()
        return channel

    # 关闭
    def __close__(self):
        self.connection.close()

    # 定义构造方法
    def __init__(self):
        pass