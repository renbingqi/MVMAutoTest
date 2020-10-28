"""
Time : 2020/10/27 17:23 
Author : Rex
File : BasePage.py 
Software: PyCharm
"""

class BasePage():

    def find_ele(self,ele):
        """
        查找元素
        :return:返回查找到的元素
        """
        target_ele=ele.wait(20)
        if target_ele.exists():
            return target_ele
        else:
            print("等待超时，元素未找到")

    def text(self,ele):
        target_ele=self.find_ele(ele)
        return target_ele.get_text()
