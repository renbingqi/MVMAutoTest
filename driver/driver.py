"""
Time : 2020/10/28 14:02 
Author : Rex
File : driver.py 
Software: PyCharm
"""
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.report.report import simple_report
from airtest.core.android.adb import ADB
class Driver():

    def start_app(self,uuid):
        init_device(platform="Android",uuid=uuid)  # 初始化设备,并设置为当前设备
        start_app("com.vivalnk.vitalsmonitor")#打开mvm
    def get_poco(self):
        poco = AndroidUiautomationPoco(screenshot_each_action=False)
        return poco

    def close_app(self):
        stop_app("com.vivalnk.vitalsmonitor")

    def back(self):
        keyevent("KEYCODE_BACK")

if __name__ == '__main__':
    p_list=[]
    from multiprocessing import Process
    driver=Driver()
    adb=ADB()
    all_devices=adb.devices()
    for item in range(len(all_devices)):
        # print(all_devices[item][0])
        p=Process(target=driver.start_app,args=(all_devices[item][0],))
        p.start()
        p_list.append(p)
    for i in p_list:
        i.join()

