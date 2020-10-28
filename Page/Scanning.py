"""
Time : 2020/10/27 16:14 
Author : Rex
File : Scanning.py 
Software: PyCharm
"""

from Page.Paired import Paired
from Page.PairingYourPatch import PairingYourPatch
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

from basePage.BasePage import BasePage

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


class Scanning(BasePage):
    Backbutton=None

    def back(self):
        self.find_ele(self.Backbutton).click()
        return PairingYourPatch()

    def connect(self,SN):
        self.find_ele(poco(text="ECGRec_{}".format(SN))).click()
        return Paired()