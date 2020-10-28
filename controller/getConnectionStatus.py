"""
Time : 2020/10/27 16:49 
Author : Rex
File : getConnectionStatus.py 
Software: PyCharm
"""
from Page.DashboardPage import Dashboard
class getConnectionStatus():
    def __init__(self):
        self.ecg=Dashboard.ECGPatchButton
        self.temp=Dashboard.TempPatchButton
        self.spo2=Dashboard.SpO2PatchButton

    def get_ecg_status(self):
        if self.ecg.get_text() == "--":
            #未连接设备
            Dashboard.isecgconnect=0
        else:
            Dashboard.isecgconnect=1

    def get_temp_status(self):
        if self.temp.get_text() == "--":
            Dashboard.istempconnect=0
        else:
            Dashboard.istempconnect=1

    def get_spo2_status(self):
        if self.spo2.get_text() == "--":
            Dashboard.isspo2connect=0
        else:
            Dashboard.isspo2connect=1



