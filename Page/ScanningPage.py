"""
Time : 2020/10/27 16:14 
Author : Rex
File : ScanningPage.py
Software: PyCharm
"""


from Page.pairingyourpatchpage import PairingYourPatch
from basePage.BasePage import BasePage


class Scanning(BasePage):
    Backbutton="android.widget.ImageButton"

    def back(self):
        self.find_ele(self.Backbutton).click()
        return PairingYourPatch()

    def connect(self,SN):
        from Page.pairedpage import Paired
        self.find_ele(poco(text="ECGRec_{}".format(SN))).click()
        return Paired()