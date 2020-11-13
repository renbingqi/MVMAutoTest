"""
Time : 2020/10/20 13:50 
Author : Rex
File : dashboard.yaml.py
Software: PyCharm
"""

from Page.multivitalmonitorpage import MultiVitalMonitor
# from driver.driver import Driver
from basePage.BasePage import BasePage


class Dashboard(BasePage):
    MenuButton="Open navigation drawer"
    INVERTButton="com.vivalnk.vitalsmonitor:id/tvInvertModeOne"
    ECGPatchButton="com.vivalnk.vitalsmonitor:id/tvBattery330"
    TempPatchButton="com.vivalnk.vitalsmonitor:id/tvBattery200"
    SpO2PatchButton="com.vivalnk.vitalsmonitor:id/tvBatterySpo2"
    title ="android.widget.TextView"
    isecgconnect=None
    istempconnect=None
    isspo2connect=None


    def returnECGPage(self):
        from Page.pairingyourpatchpage import PairingYourPatch
        self.find_ele(self.ECGPatchButton).click()
        if self.isecgconnect==0:
            return PairingYourPatch()
        else:
            return MultiVitalMonitor()

    def returnTempPage(self):
        from Page.pairingyourpatchpage import PairingYourPatch
        self.find_ele(self.TempPatchButton).click()
        if self.istempconnect == 0:
            return PairingYourPatch()
        else:
            return MultiVitalMonitor()

    def returnSpO2(self):
        from Page.pairingyourpatchpage import PairingYourPatch
        self.find_ele(self.SpO2PatchButton).click()
        if self.isspo2connect == 0:
            return PairingYourPatch()
        else:
            return MultiVitalMonitor()

    def returnMenu(self):
        from Page.menuPage import Menu
        self.find_ele(self.MenuButton).click()
        return Menu()

    def Invert(self):
        self.find_ele(self.INVERTButton).click()

    def isEcgConnection(self):
        if self.text(self.ECGPatchButton) == "--":
            #设备未连接
            Dashboard.isecgconnect = 0
        else:
            Dashboard.isecgconnect = 1

    def isTempConnecton(self):
        if self.text(self.TempPatchButton) == "--":
            #设备未连接
            Dashboard.istempconnect = 0
        else:
            Dashboard.istempconnect = 1

    def isSpO2Connection(self):
        if self.text(self.SpO2PatchButton) == "--":
            #设备未连接
            Dashboard.isspo2connect = 0
        else:
            Dashboard.isspo2connect = 1

    def get_dashboard_ele(self):
        ele_list=[]
        ele_obj=self.find_ele("android.widget.LinearLayout").offspring()
        for ele in ele_obj:
            if ele.get_text() != None:
                ele_list.append(ele.get_text())
        return ele_list

    def return_dashboard(self):
        while True:
            if self.text(self.title) != "Multi Vital Monitor":
                self.back()
            else:
                break





if __name__ == '__main__':
    # Driver().connect_device()
    # print(Dashboard().get_dashboard_ele())
    Dashboard().return_dashboard()
    # Dashboard().returnTempPage()



