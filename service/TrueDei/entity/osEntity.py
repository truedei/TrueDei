#!/usr/bin/python3

# 类定义
class osEntity:

    # 定义基本属性
    fileSystem = ''  # 文件系统
    size = ''  # 容量大小
    used = ''  # 已用大小
    avil = ''  # 可用大小
    useb = ''  # 已用百分比
    mountedOn = ''

    # 定义构造方法
    def __init__(self,fileSystem,size,used,avil,useb,mountedOn):
         self.fileSystem = fileSystem
         self.size = size
         self.used = used
         self.avil = avil
         self.useb = useb
         self.mountedOn = mountedOn
    def getStrData(self):
        return self.fileSystem+","+self.size+","+self.used+","+self.avil+","+self.useb+","+self.mountedOn
# 实例化类
#p = osEntity('runoob', '10', '30','123','332','43')
#print(p.size)