"""
Time : 2020/11/12 17:23 
Author : Rex
File : test_ buttom.py 
Software: PyCharm
"""
import time

import pytest

from Page.about import About
from Page.connectedDevice import ConnectedDevice
from Page.dashboard import Dashboard
from Page.menuPage import Menu
from Page.pairingyourpatchpage import PairingYourPatch
from Page.report import Report
from Page.settingspage import Settings


class Test_Buttom():
    @pytest.fixture(scope="module")
    def setup(self):
        Dashboard().start_app()
        yield
        Dashboard().close_app()

    @pytest.fixture()
    def return_doshboard(self):
        Dashboard().return_dashboard()

    @pytest.mark.usefixtures("setup")
    @pytest.mark.usefixtures("return_doshboard")
    def test_ECG_Button(self):
        Dashboard().returnECGPage()
        assert PairingYourPatch().text("com.vivalnk.vitalsmonitor:id/tvPatchTypeName") == "ECG Recorder"

    @pytest.mark.usefixtures("setup")
    @pytest.mark.usefixtures("return_doshboard")
    def test_Temp_Button(self):
        time.sleep(0.5)
        # Dashboard().return_dashboard()
        Dashboard().returnTempPage()
        assert PairingYourPatch().text("com.vivalnk.vitalsmonitor:id/tvPatchTypeName") == "Temperature Patch"

    @pytest.mark.usefixtures("setup")
    @pytest.mark.usefixtures("return_doshboard")
    def test_SpO2_Button(self):
        time.sleep(0.5)
        # Dashboard().return_dashboard()
        Dashboard().returnSpO2()
        assert PairingYourPatch().text("com.vivalnk.vitalsmonitor:id/tvPatchTypeName") == "SpO2 Monitor(Checkme O2)"

    @pytest.mark.usefixtures("setup")
    @pytest.mark.usefixtures("return_doshboard")
    def test_Menu_Button(self):
        time.sleep(0.5)
        Dashboard().returnMenu()
        assert Menu().poco(Menu.title)[1].get_text() == "Menu"

    @pytest.mark.usefixtures("setup")
    @pytest.mark.usefixtures("return_doshboard")
    def test_Connected_Device_Button(self):
        time.sleep(0.5)
        # Dashboard().returnMenu()
        Menu().returnConnectDevice()
        assert ConnectedDevice().text(ConnectedDevice.title) == "Connected Device"

    @pytest.mark.usefixtures("setup")
    @pytest.mark.usefixtures("return_doshboard")
    def test_Settings(self):
        time.sleep(0.5)
        Dashboard().returnMenu()
        Menu().returnSettings()
        assert Settings().text(Settings.title) == "Settings"


    @pytest.mark.usefixtures("setup")
    @pytest.mark.usefixtures("return_doshboard")
    def test_Settings_YourProfile(self):
        time.sleep(0.5)
        Dashboard().returnMenu()
        Menu().returnSettings()
        Settings().return_YourProfile()
        assert Settings().text(Settings.title) == "Your Profile"

    @pytest.mark.usefixtures("setup")
    @pytest.mark.usefixtures("return_doshboard")
    def test_Settings_Report(self):
        time.sleep(0.5)
        Dashboard().returnMenu()
        Menu().returnSettings()
        Settings().return_Report()
        assert Report().text(Report.title) == "Report"

    @pytest.mark.usefixtures("setup")
    @pytest.mark.usefixtures("return_doshboard")
    def test_Settings_about(self):
        time.sleep(0.5)
        Dashboard().returnMenu()
        Menu().returnSettings()
        Settings().return_About()
        assert About().text(About.title) == "About"

    @pytest.mark.usefixtures("setup")
    @pytest.mark.usefixtures("return_doshboard")
    def test_PrivacyPolicy(self):
        time.sleep(0.5)
        Dashboard().returnMenu()
        Menu().PrivacyPolicy()
        time.sleep(5)
        assert Menu().text('android.widget.TextView') == "Privacy Policy"

    @pytest.mark.usefixtures("setup")
    @pytest.mark.usefixtures("return_doshboard")
    def test_TermAndConditions(self):
        time.sleep(0.5)
        Dashboard().returnMenu()
        Menu().TermsAndConditions()
        time.sleep(5)
        assert Menu().text('android.widget.TextView') == "Terms and Conditions"




if __name__ == '__main__':
    pytest.main(["-s","-v"])





