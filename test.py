"""
Time : 2020/10/28 10:19 
Author : Rex
File : test.py 
Software: PyCharm
"""
if __name__ == '__main__':
    from airtest.core.api import *
    init_device("Android","FA7C61A04541")
    print(device())
    start_app("com.vivalnk.vitalsmonitor")
    touch


