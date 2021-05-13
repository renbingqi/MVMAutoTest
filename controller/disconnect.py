"""
Time : 2020/10/29 10:45 
Author : Rex
File : disconnect.py 
Software: PyCharm
"""
from Page.dashboard import Dashboard


class Connect():
    def connectEcg(self):
        Dashboard().isEcgConnection()#获取设备当前的状态并将状态记录
        #判断是否连接
        if Dashboard.isecgconnect == 1 :#1为设备已连接
            dashboard = Dashboard().returnECGPage().disconnectDevice().Skip()
            if dashboard().text(dashboard.ECGPatchButton) == "--":
                print("断开连接成功")
            else:
                print("断开连接失败")
        else:
            print("ECG设备未连接")

    def connectTemp(self):
        pass

    def connectSpO2(self):
        pass