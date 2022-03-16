"""
Time : 2020/10/27 16:43 
Author : Rex
File : test_UI.py
Software: PyCharm
"""
import time
from Page.dashboard import Dashboard
import pytest
from Page.menuPage import Menu
from Page.pairingyourpatchpage import PairingYourPatch
from Page.settingspage import Settings
from Page.yourprofilepage import YourProfile
from utils.getYaml import GetYaml
from ddt import ddt,data
import unittest
from driver.driver import Driver
@ddt
class Test_UI():

    @pytest.fixture(scope="module")
    def setup(self):
        Dashboard().start_app("com.vivalnk.cardiacscout.beta")
        yield
        Dashboard().close_app()

    #获取预期元素列表&dashboard元素列表
    @pytest.fixture(scope="class")
    def setup_dashboard(self):
        Dashboard().return_dashboard()
        ele_list = GetYaml().get_dashboard_yaml()
        time.sleep(1)
        dashboardele_list = Dashboard().get_dashboard_ele()
        return (ele_list, dashboardele_list)

    # 获取预期元素列表&menu元素列表
    @pytest.fixture(scope="class")
    def setup_menu(self):
        Dashboard().returnMenu()
        ele_list = GetYaml().get_menu_yaml()
        menu_list = Menu().get_menu_ele()
        return (ele_list, menu_list)

    # 获取预期元素列表&Setting元素列表
    @pytest.fixture(scope="class")
    def setup_Settings(self):
        Menu().returnSettings()
        ele_list = GetYaml().get_Settings_yaml()
        menu_list = Settings().get_settings_ele()
        return (ele_list, menu_list)

    # 获取预期元素列表&YourProfile元素列表
    @pytest.fixture(scope="class")
    def setup_YourProfile(self):
        Settings().return_YourProfile()
        ele_list = GetYaml().get_YourProfile_yaml()
        menu_list = YourProfile().get_yourprofile_ele()
        return (ele_list, menu_list)

    # 获取预期元素列表&pairingYourPatchECG元素列表
    @pytest.fixture(scope="class")
    def setup_PairingYourPatchECG(self):
        YourProfile().close()
        Settings().close()
        Dashboard().returnECGPage()
        ele_list = GetYaml().get_PairingYourPatchECG_yaml()
        menu_list = PairingYourPatch().get_PairingYourPatchECG_ele()
        return (ele_list, menu_list)

    # 获取预期元素列表&pairingYourPatchTemp元素列表
    @pytest.fixture(scope="class")
    def setup_PairingYourPatchTemp(self):
        PairingYourPatch().skip()
        Dashboard().returnTempPage()
        ele_list = GetYaml().get_PairingYourPatchTemp_yaml()
        menu_list = PairingYourPatch().get_PairingYourPatchTemp_ele()
        return (ele_list, menu_list)

    # 获取预期元素列表&PairingYourPatchSpO2元素列表
    @pytest.fixture(scope="class")
    def setup_PairingYourPatchSpO2(self):
        PairingYourPatch().skip()
        Dashboard().returnSpO2()
        ele_list = GetYaml().get_PairingYourPatchSpO2_yaml()
        menu_list = PairingYourPatch().get_PairingYourPatchSpO2_ele()
        return (ele_list, menu_list)


#--------------------------------------------------------------------------------------
    #dashboard元素测试
    @pytest.mark.usefixtures("setup")
    def test_dashboard_ele(self,setup_dashboard):
        ele_list=setup_dashboard[0]
        for ele in ele_list:
            assert ele in setup_dashboard[1]

    #menu页面元素测试
    @pytest.mark.usefixtures("setup")
    def test_menu_ele(self,setup_menu):
        ele_list = setup_menu[0]
        for ele in ele_list:
            assert ele in setup_menu[1]

    #settings页面元素测试
    @pytest.mark.usefixtures("setup")
    def test_settings_ele(self,setup_Settings):
        ele_list = setup_Settings[0]
        for ele in ele_list:
            assert ele in setup_Settings[1]

    #yourprofile页面元素测试
    @pytest.mark.usefixtures("setup")
    def test_yourprofile_ele(self,setup_YourProfile):
        ele_list = setup_YourProfile[0]
        for ele in ele_list:
            assert ele in setup_YourProfile[1]

    #pairingYourPatchECG页面元素测试
    @pytest.mark.usefixtures("setup")
    def test_PairingYourPatchECG_ele(self,setup_PairingYourPatchECG):
        ele_list = setup_PairingYourPatchECG[0]
        for ele in ele_list:
            assert ele in setup_PairingYourPatchECG[1]

    #pairingYourPatchTemp页面元素测试
    @pytest.mark.usefixtures("setup")
    def test_PairingYourPatchTemp_ele(self,setup_PairingYourPatchTemp):
        ele_list = setup_PairingYourPatchTemp[0]
        for ele in ele_list:
            assert ele in setup_PairingYourPatchTemp[1]

    #pairingYourPatch页面元素测试
    @pytest.mark.usefixtures("setup")
    def test_PairingYourPatchSpo2_ele(self,setup_PairingYourPatchSpO2):
        ele_list = setup_PairingYourPatchSpO2[0]
        for ele in ele_list:
            assert ele in setup_PairingYourPatchSpO2[1]





if __name__ == '__main__':
    pytest.main(["-v","-s"])



