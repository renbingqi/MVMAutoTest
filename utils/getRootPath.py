"""
Time : 2020/11/1 22:41 
Author : Rex
File : getRootPath.py 
Software: PyCharm
"""
import os
def get_rootpath():
    path=os.path.abspath(__file__)
    path_list=path.split("\\")
    rootpath="\\".join(path_list[0:path_list.index("MVM Android Auto Test")+1])
    return rootpath


if __name__ == '__main__':

    get_rootpath()


