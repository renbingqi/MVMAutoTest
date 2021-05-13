"""
Time : 2020/11/11 22:12 
Author : Rex
File : yourprofilepage.py 
Software: PyCharm
"""
from basePage.BasePage import BasePage
class YourProfile(BasePage):
    closeButton="android.widget.ImageButton"

    def close(self):
        self.find_ele(self.closeButton).click()

    def get_yourprofile_ele(self):
        ele_list=[]
        ele_obj=self.find_ele("android.widget.LinearLayout").offspring()
        for ele in ele_obj:
            if ele.get_text() != None:
                ele_list.append(ele.get_text())
        return ele_list
