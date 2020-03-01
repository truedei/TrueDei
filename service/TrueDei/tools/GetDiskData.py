import os
import re
from entity.osEntity import osEntity

def getDiskData():
    #p = os.system("echo ll ");
    command = "cat /etc/redhat-release"
    comm1 = "df -h" #运行df命令，查看当前磁盘使用情况
    os_str = os.popen(comm1).read() #执行linux命令，并读取执行结果
    """
    # Filesystem      Size  Used Avail Use% Mounted on
    # devtmpfs        1.9G     0  1.9G   0% /dev
    # tmpfs           1.9G     0  1.9G   0% /dev/shm
    # tmpfs           1.9G  368K  1.9G   1% /run
    # tmpfs           1.9G     0  1.9G   0% /sys/fs/cgroup
    # /dev/vda1        40G   19G   19G  51% /
    """
    #先按照回车 换行符进行分割
    arr1 = os_str.split('\n')
    #定义存储的List
    osList = []
    #把每行数据进行分割
    n = 0
    for i in arr1:
            #1、把多个空格合并成一个空格
            str1 = re.sub(' +',',',i)
            #2、按空格符进行分割数据
            str2 = str1.split(',')
            #过滤掉最后一行的空格
            if n!=(len(arr1)-1):
                #创建一个新的对象合并数，使数据对象化,从而有一定的规则，便于以后调用数据
                oe = osEntity(str2[0], str2[1], str2[2],str2[3],str2[4],str2[5]).getStrData()
                #追加到list中存储
                osList.append(oe)
            #计算已经处理的行数
            n = n + 1
    # #定义存储的List
    # osList = []
    # osList.append(osEntity("1", "2", "3", "4", "5", "6").getStrData())
    # osList.append(osEntity("1", "2", "3", "4", "5", "6").getStrData())
    # osList.append(osEntity("1", "2", "3", "4", "5", "6").getStrData())
    # osList.append(osEntity("1", "2", "3", "4", "5", "6").getStrData())
    print("我被调用了")
    return osList
    # return "a"
# for ol in osList [:]:
#         #只监控某一个
#         if ol.mountedOn=='/':
#             print(ol.mountedOn,"目录，当前使用情况：\r\n 总容量：【",ol.size,"】,已经使用大小：【",ol.used,"】,可用大小：【",ol.avil,"】，已用百分比：【",ol.useb,"】")

#磁盘报警信息
def getDiskWarning():
    #p = os.system("echo ll ");
    command = "cat /etc/redhat-release"
    comm1 = "df -h" #运行df命令，查看当前磁盘使用情况
    os_str = os.popen(comm1).read() #执行linux命令，并读取执行结果
    """
    # Filesystem      Size  Used Avail Use% Mounted on
    # devtmpfs        1.9G     0  1.9G   0% /dev
    # tmpfs           1.9G     0  1.9G   0% /dev/shm
    # tmpfs           1.9G  368K  1.9G   1% /run
    # tmpfs           1.9G     0  1.9G   0% /sys/fs/cgroup
    # /dev/vda1        40G   19G   19G  51% /
    """
    #先按照回车 换行符进行分割
    arr1 = os_str.split('\n')
    #定义存储的List
    osList = []
    #把每行数据进行分割
    n = 0
    for i in arr1:
            #1、把多个空格合并成一个空格
            str1 = re.sub(' +',',',i)
            #2、按空格符进行分割数据
            str2 = str1.split(',')
            #过滤掉最后一行的空格
            if n!=(len(arr1)-1):
                #创建一个新的对象合并数，使数据对象化,从而有一定的规则，便于以后调用数据
                oe = osEntity(str2[0], str2[1], str2[2],str2[3],str2[4],str2[5]).getStrData()
                #追加到list中存储
                osList.append(oe)
            #计算已经处理的行数
            n = n + 1
    # #定义存储的List
    # osList = []
    # osList.append(osEntity("1", "2", "3", "4", "5", "6").getStrData())
    # osList.append(osEntity("1", "2", "3", "4", "5", "6").getStrData())
    # osList.append(osEntity("1", "2", "3", "4", "5", "6").getStrData())
    # osList.append(osEntity("1", "2", "3", "4", "5", "6").getStrData())
    print("我被调用了")
    return osList