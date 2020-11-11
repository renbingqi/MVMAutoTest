"""
Time : 2020/10/20 14:38 
Author : Rex
File : pairingyourpatchpage.py
Software: PyCharm
"""
from Page.dashboard import Dashboard
from basePage.BasePage import BasePage


class PairingYourPatch(BasePage):
    StartPairingButton="com.vivalnk.vitalsmonitor:id/btnStartPairing"
    BackButton="android.widget.ImageButton"
    SkipButton="com.vivalnk.vitalsmonitor:id/btnSkip"

    def back(self):
        self.find_ele(self.BackButton).click()
        return Dashboard()

    def startpairing(self):
        from Page.ScanningPage import Scanning
        self.find_ele(self.StartPairingButton).click()
        return Scanning()

    def skip(self):
        self.find_ele(self.SkipButton).click()
        return Dashboard()

    def get_PairingYourPatchECG_ele(self):
        ele_list=[]
        ele_obj=self.find_ele("android.widget.LinearLayout").offspring()
        for ele in ele_obj:
            if ele.get_text() != None:
                ele_list.append(ele.get_text())
        return ele_list

    def get_PairingYourPatchTemp_ele(self):
        ele_list=[]
        ele_obj=self.find_ele("android.widget.LinearLayout").offspring()
        for ele in ele_obj:
            if ele.get_text() != None:
                ele_list.append(ele.get_text())
        return ele_list

    def get_PairingYourPatchSpO2_ele(self):
        ele_list=[]
        ele_obj=self.find_ele("android.widget.LinearLayout").offspring()
        for ele in ele_obj:
            if ele.get_text() != None:
                ele_list.append(ele.get_text())
        return ele_list
