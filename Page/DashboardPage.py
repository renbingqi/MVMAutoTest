"""
Time : 2020/10/20 13:50 
Author : Rex
File : DashboardPage.py 
Software: PyCharm
"""
from Page.MenuPage import Menu
from Page.MultiVitalMonitor import MultiVitalMonitor
from Page.PairingYourPatch import PairingYourPatch
from basePage.BasePage import BasePage


class Dashboard(BasePage):
    MenuButton=None
    INVERTButton=None
    ECGPatchButton=None
    TempPatchButton=None
    SpO2PatchButton=None
    isecgconnect=None
    istempconnect=None
    isspo2connect=None

    def returnECGPage(self):
        self.find_ele(self.ECGPatchButton).click()
        if self.isecgconnect==0:
            return PairingYourPatch()
        else:
            return MultiVitalMonitor()

    def returnTempPage(self):
        self.find_ele(self.TempPatchButton).click()
        if self.istempconnect == 0:
            return PairingYourPatch()
        else:
            return MultiVitalMonitor()

    def returnSpO2(self):
        self.find_ele(self.SpO2PatchButton).click()
        if self.isspo2connect == 0:
            return PairingYourPatch()
        else:
            return MultiVitalMonitor()

    def returnMenu(self):
        self.find_ele(self.MenuButton).click()
        return Menu()

    def Invert(self):
        self.find_ele(self.INVERTButton).click()

