"""
Time : 2020/11/1 22:39 
Author : Rex
File : getYaml.py 
Software: PyCharm
"""
import yaml
from utils.getRootPath import get_rootpath
class GetYaml():
    def get_dashboard_yaml(self):
        ele_list = []
        file_path=get_rootpath()+"/config/initialElement/dashboard.yaml"
        with open(file_path) as f:
            message=yaml.load(f,Loader=yaml.Loader)
            for ele in message:
                ele_list.append(ele)
        # print(ele_list)
        return ele_list

    def get_menu_yaml(self):
        ele_list = []
        file_path=get_rootpath()+"/config/initialElement/menu.yaml"
        with open(file_path) as f:
            message=yaml.load(f,Loader=yaml.Loader)
            # print(message)
            for ele in message:
                ele_list.append(ele)
        return ele_list

    def get_PairingYourPatchECG_yaml(self):
        ele_list = []
        file_path=get_rootpath()+"/config/initialElement/PairingYourPatchECG.yaml"
        with open(file_path) as f:
            message=yaml.load(f,Loader=yaml.Loader)
            # print(message)
            for ele in message:
                ele_list.append(ele)
        return ele_list

    def get_PairingYourPatchTemp_yaml(self):
        ele_list = []
        file_path=get_rootpath()+"/config/initialElement/PairingYourPatchTemp.yaml"
        with open(file_path) as f:
            message=yaml.load(f,Loader=yaml.Loader)
            # print(message)
            for ele in message:
                ele_list.append(ele)
        return ele_list

    def get_PairingYourPatchSpO2_yaml(self):
        ele_list = []
        file_path=get_rootpath()+"/config/initialElement/PairingYourPatchSpO2.yaml"
        with open(file_path) as f:
            message=yaml.load(f,Loader=yaml.Loader)
            # print(message)
            for ele in message:
                ele_list.append(ele)
        return ele_list

    def get_Settings_yaml(self):
        ele_list = []
        file_path=get_rootpath()+"/config/initialElement/Settings.yaml"
        with open(file_path) as f:
            message=yaml.load(f,Loader=yaml.Loader)
            # print(message)
            for ele in message:
                ele_list.append(ele)
        return ele_list

    def get_YourProfile_yaml(self):
        ele_list = []
        file_path=get_rootpath()+"/config/initialElement/YourProfile.yaml"
        with open(file_path) as f:
            message=yaml.load(f,Loader=yaml.Loader)
            # print(message)
            for ele in message:
                ele_list.append(ele)
        return ele_list


    def get_ECGStatus_yaml(self):
        ele_list = []
        file_path=get_rootpath()+"/config/deviceStatus/ECGStatus.yaml"
        with open(file_path,encoding="utf-8") as f:
            message=yaml.load(f,Loader=yaml.Loader)
            # print(message)
            for ele in message:
                ele_list.append(ele)
        return ele_list

    def get_TempStatus_yaml(self):
        ele_list = []
        file_path=get_rootpath()+"/config/deviceStatus/TempStatus.yaml"
        with open(file_path,encoding="utf-8") as f:
            message=yaml.load(f,Loader=yaml.Loader)
            # print(message)
            for ele in message:
                ele_list.append(ele)
        return ele_list

    def get_SpO2Status_yaml(self):
        ele_list = []
        file_path=get_rootpath()+"/config/deviceStatus/SpO2Status.yaml"
        with open(file_path,encoding="utf-8") as f:
            message=yaml.load(f,Loader=yaml.Loader)
            # print(message)
            for ele in message:
                ele_list.append(ele)
        return ele_list

if __name__ == '__main__':
    run=GetYaml()
    print(run.get_ECGStatus_yaml())
    print(run.get_TempStatus_yaml())
    print(run.get_SpO2Status_yaml())
