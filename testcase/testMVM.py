"""
Time : 2020/10/27 16:43 
Author : Rex
File : testMVM.py 
Software: PyCharm
"""
from Page.DashboardPage import Dashboard
from Page.Paired import Paired
from controller.getConnectionStatus import getConnectionStatus
class TestMVM():

    def test_ecgConnectAnddisconnect(self,SN):
        #先判断ecg设备是否连接并将状态进行记录
        getConnectionStatus().get_ecg_status()
        # 如果状态为0 说明未连接则进行正常的连接操作
        if Dashboard.isecgconnect == 0:
            # 连接操作,成功后并返回到dashboard
            Pair=Dashboard().returnECGPage().startpairing().connect(SN=SN)
            Paired().get_SN(SN)
            if SN in Paired().SN:
                Pair.next()
                dashboard=Dashboard().returnECGPage().disconnectDevice().Skip()
                if dashboard.text(SN) == "--":
                    print("断开连接成功")
                else:
                    print("断开连接失败")

            else:
                print("连接失败")



