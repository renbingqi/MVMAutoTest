"""
Time : 2020/10/27 16:15 
Author : Rex
File : pairedpage.py
Software: PyCharm
"""
from Page.dashboard import Dashboard
from Page.ScanningPage import Scanning
from basePage.BasePage import BasePage


class Paired(BasePage):
    BackButton="android.widget.ImageButton"
    NextButton="com.vivalnk.vitalsmonitor:id/btnNext"
    RescanDeviceButton="com.vivalnk.vitalsmonitor:id/btnRescan"
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
        SN_text=self.text(poco(text="ECGRec_{}".format(SN)))
        self.SN=SN_text
        return SN_text
