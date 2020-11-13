"""
Time : 2020/10/20 14:12 
Author : Rex
File : menuPage.py
Software: PyCharm
"""
from Page.dashboard import Dashboard
from basePage.BasePage import BasePage


class Menu(BasePage):
    ConnectedDeviceButton="com.vivalnk.vitalsmonitor:id/tvDevice"
    SettingsButton="com.vivalnk.vitalsmonitor:id/tvSetting"
    PrivacyPolicyButton="com.vivalnk.vitalsmonitor:id/tvPrivacy"
    TermsAndConditionsButton="com.vivalnk.vitalsmonitor:id/tvTerms"
    CloseButton="com.vivalnk.vitalsmonitor:id/ivClose"
    title="android.widget.TextView"

    def returnConnectDevice(self):
        self.find_ele(self.ConnectedDeviceButton).click()

    def returnSettings(self):
        self.find_ele(self.SettingsButton).click()

    def PrivacyPolicy(self):
        self.find_ele(self.PrivacyPolicyButton).click()

    def TermsAndConditions(self):
        self.find_ele(self.TermsAndConditionsButton).click()

    def Close(self):
        self.find_ele(self.CloseButton).click()

    def get_menu_ele(self):
        ele_list=[]
        ele_obj=self.find_ele("android.view.ViewGroup").offspring()
        for ele in ele_obj:
            if ele.get_text() != None:
                ele_list.append(ele.get_text())
        return ele_list

    def return_Menu(self):
        while True:
            # print(self.poco(self.title)[1].get_text())

            if self.poco(self.title)[1].get_text() != "Menu":
                Dashboard().return_dashboard()
                Dashboard().returnMenu()
            else:
                break

if __name__ == '__main__':
    Menu().return_Menu()
