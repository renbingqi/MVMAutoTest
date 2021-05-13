"""
Time : 2020/10/29 10:45 
Author : Rex
File : connect.py 
Software: PyCharm
"""
import time

from Page.dashboard import Dashboard
from Page.pairedpage import Paired
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

from driver.driver import Driver

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
from utils.getYaml import GetYaml

class Connect():

    def connectEcg(self):
        ecg_list=GetYaml().get_ECGStatus_yaml()
        SN=ecg_list[0]["deviceSN"]
        batteryStatus=ecg_list[0]['batteryStatus']
        deviceStatus=ecg_list[0]['deviceStatus']
        if Dashboard.isecgconnect ==  0:  ## 判断是否连接 0未连接
            Pair=Dashboard().returnECGPage().startpairing().connect(SN="201904/C500149")
            if poco("android.widget.TextView").wait(20).exists():  # 应该判断paired！是否存在
                Pair.next()#返回到主页面
                print("连接成功")
            else:
                print("连接失败")
        else:
            #已经连接设备
            print("Ecg设备已连接")

    def connectTemp(self,sn):
        # 判断是否连接
        if Dashboard.istempconnect == " 0":  # 未连接
            Pair=Dashboard().returnTempPage().startpairing().connect(SN=sn)
            if poco("android.widget.TextView").exists():  # 应该判断paired！是否存在
                Pair.next()#返回到主页面
            else:
                print("连接失败")
        else:
            #已经连接设备
            print("Temp设备已连接")

    def connectSpO2(self,sn):
        # 判断是否连接
        if Dashboard.isspo2connect == " 0":  # 未连接
            Pair=Dashboard().returnSpO2().startpairing().connect(SN=sn)
            if poco("android.widget.TextView").wait(20).exists():  # 应该判断paired！是否存在
                Pair.next()#返回到主页面
            else:
                print("连接失败")
        else:
            #已经连接设备
            print("SpO2设备已连接")
if __name__ == '__main__':
    Driver().connect_device()
    Driver().start_app()
    driver=Connect()
    driver.connectEcg()
    Driver().close_app()