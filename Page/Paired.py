"""
Time : 2020/10/27 16:15 
Author : Rex
File : Paired.py 
Software: PyCharm
"""
from Page.DashboardPage import Dashboard
from Page.Scanning import Scanning
from basePage.BasePage import BasePage

class Paired(BasePage):
    BackButton=None
    NextButton=None
    RescanDeviceButton=None
    SN=None

    def back(self):
        self.find_ele(self.BackButton).click()
        return Scanning()

    def next(self):
        self.find_ele(self.NextButton).click()
        return Dashboard()

    def rescandevice(self):
        self.find_ele(self.RescanDeviceButton).click()
        return Scanning()

    def get_SN(self,SN):
        self.SN=self.text(SN)
