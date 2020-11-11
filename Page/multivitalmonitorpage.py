"""
Time : 2020/10/20 14:24 
Author : Rex
File : multivitalmonitorpage.py
Software: PyCharm
"""
from basePage.BasePage import BasePage




class MultiVitalMonitor(BasePage):
    BackButton="Navigate up"
    Skip="com.vivalnk.vitalsmonitor:id/btnSkip"
    DisconnectDeviceButton="com.vivalnk.vitalsmonitor:id/btnDelete"

    def back(self):
        from Page.dashboard import Dashboard
        self.find_ele(self.BackButton).click()
        return Dashboard()

    def disconnectDevice(self):
        self.find_ele(self.DisconnectDeviceButton).click()
        return MultiVitalMonitor()

    def skip(self):
        from Page.dashboard import Dashboard
        self.find_ele(self.Skip).click()
        return Dashboard()
if __name__ == '__main__':
    print("123")






