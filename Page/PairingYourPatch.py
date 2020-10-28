"""
Time : 2020/10/20 14:38 
Author : Rex
File : PairingYourPatch.py 
Software: PyCharm
"""
from Page.DashboardPage import Dashboard
from Page.Scanning import Scanning
from basePage.BasePage import BasePage


class PairingYourPatch(BasePage):
    StartPairingButton=None
    BackButton=None
    SkipButton=None

    def back(self):
        self.find_ele(self.BackButton).click()
        return Dashboard()

    def startpairing(self):
        self.find_ele(self.StartPairingButton).click()
        return Scanning()

    def skip(self):
        self.find_ele(self.SkipButton).click()
        return Dashboard()
