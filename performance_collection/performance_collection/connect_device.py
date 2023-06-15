# -*- encoding: utf-8 -*-
"""
@File    :   connect_device.py    
@Author  :   wanhongda
@Modify Time      @Version    @Desciption
------------      --------    -----------
2023/5/13 16:49    1.0         None
"""
import subprocess
from solox.public.apm import APM

# 先连接上设备，再返回设备的ip:host 供solox使用
def get_connect(adb_url):
    # 传入adb连接url，连接云真机设备adb connect 172.19.1.28:20065   或者serialno
    cmd = adb_url
    # 执行连接，并返回adb连接到的设备
    # usb连接的设备也统一成adb connect的格式
    # print(".......",cmd)
    if "adb connect " not in cmd:
        cmd = "adb connect " + cmd
        # print("......",cmd)
    output = subprocess.check_output(cmd, shell=True)
    # print("get_connect-------",output)
    try:
        if output:
            # print(output.decode())
            adb_url = parse_device_url()
            # print("adb",adb_url)
            return adb_url
    except Exception as e:
        print("连接adb设备出错", e)


# 单设备字符串处理
def parse_device_url():
    # adb devices获取当前已占用的设备,返回连接的url串，即adb connect后面的那串和包名
    cmd2 = "adb devices"
    # 返回所有已连接的设备
    output = subprocess.check_output(cmd2, shell=True)
    # print(output.decode())
    temp = output.split(b'List of devices attached')[1].split(b'device')[0].decode()
    adb_url = temp.splitlines()[1]
    # print("xxxxxxxxxxxxx",adb_url)
    return adb_url


# 返回当前通过adb connect设备的ip和端口号
def parse_devices_url(devices_str):
    # adb devices获取当前已占用的设备
    # 返回连接的url串，即adb connect后面的那串和包名
    cmd2 = devices_str
    # 返回所有已连接的设备
    output = subprocess.check_output(cmd2, shell=True)
    # print(output.decode())
    # adb_url = output.split(b'List of devices attached')[1].split(b'device')[0].decode()
    a = output.split(b'List of devices attached')
    # print("11111",a[1].decode())
    # 遍历获取到的设备，转成列表
    temp = []
    for i in a[1].split(b'device'):
        temp.append(i.decode().splitlines()[1])
        # print(i.decode())
    # 处理当前所有的devices串，返回纯粹的ip和端口号
    return temp


# 获取当前包名
def get_current_pkgname():
    # cmd='adb shell dumpsys activity top | findstr "ACTIVITY"'
    cmd = 'adb shell dumpsys window | findstr mCurrentFocus'
    temp = subprocess.check_output(cmd, shell=True)
    temp = temp.decode().split('/')
    pkg_name = temp[0][temp[0].index("com"):]  # 获取com之后的内容
    # print(pkg_name)
    return pkg_name


def start_perf(adb_connect_url):
    # print("00",adb_connect_url)
    adb_url = get_connect(adb_connect_url)
    # print("11",adb_url)
    pkg_name = get_current_pkgname()
    # print("22",pkg_name)
    # apm = APM(pkgName=get_current_pkgname(), deviceId=adb_url, platform='Android')#需要连接上设备，才能获取当前正在运行的包名
    apm = APM(pkgName=pkg_name, deviceId=adb_url, platform='Android')
    return apm


if __name__ == '__main__':
    adb_url = get_connect("adb connect 172.19.1.24:20037")
    # print("adb_url", adb_url)
    # pkg_name = get_current_pkgname()
    # print(pkg_name)
    apm = APM(pkgName=get_current_pkgname(), deviceId=adb_url, platform='Android')
    print(apm.collectCpu())
    # print(apm.collectFps())
    # print(apm.collectFlow())
    # print(apm.collectCpu())
