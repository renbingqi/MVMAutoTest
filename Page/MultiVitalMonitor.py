"""
Time : 2020/10/20 14:24 
Author : Rex
File : MultiVitalMonitor.py
Software: PyCharm
"""
from Page.DashboardPage import Dashboard
from basePage.BasePage import BasePage


class MultiVitalMonitor(BasePage):
    BackButton=None
    Skip=None
    DisconnectDeviceButton=None

    def back(self):
        self.find_ele(self.BackButton).click()
        return Dashboard()

    def disconnectDevice(self):
        self.find_ele(self.DisconnectDeviceButton).click()
        return MultiVitalMonitor()

    def skip(self):
        self.find_ele(self.Skip).click()
        return Dashboard()







