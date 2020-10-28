"""
Time : 2020/10/20 14:12 
Author : Rex
File : MenuPage.py 
Software: PyCharm
"""
from basePage.BasePage import BasePage


class Menu(BasePage):
    ConnectedDeviceButton=None
    SettingsButton=None
    PrivacyPolicyButton=None
    TermsAndConditionsButton=None
    CloseButton=None

    def returnConnectDevice(self):
        self.find_ele(self.ConnectedDeviceButton).click()

    def returnSettings(self):
        self.find_ele(self.SettingsButton).click()

    def PrivacyPolicy(self):
        self.find_ele(self.PrivacyPolicyButton).click()

    def TermsAndConditions(self):
        self.find_ele(self.TermsAndConditionsButton).click()
