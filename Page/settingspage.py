"""
Time : 2020/11/11 22:03 
Author : Rex
File : settingspage.py 
Software: PyCharm
"""
from basePage.BasePage import BasePage
class Settings(BasePage):
    YourProfileButton="com.vivalnk.vitalsmonitor:id/tvProfile"
    ReportButton="com.vivalnk.vitalsmonitor:id/tvReport"
    AboutButton="com.vivalnk.vitalsmonitor:id/tvAbout"
    CloseButton="android.widget.ImageButton"
    BackgroundRunningButton="com.vivalnk.vitalsmonitor:id/tvBackground"
    title="android.widget.TextView"

    def return_YourProfile(self):
        self.find_ele(self.YourProfileButton).click()

    def return_Report(self):
        self.find_ele(self.ReportButton).click()

    def return_About(self):
        self.find_ele(self.AboutButton).click()

    def return_BackgroundRunning(self):
        self.find_ele(self.BackgroundRunningButton).click()

    def close(self):
        self.find_ele(self.CloseButton).click()


    def get_settings_ele(self):
        ele_list=[]
        ele_obj=self.find_ele("android.widget.LinearLayout").offspring()
        for ele in ele_obj:
            if ele.get_text() != None:
                ele_list.append(ele.get_text())
        return ele_list

if __name__ == '__main__':
    Settings().return_YourProfile()
