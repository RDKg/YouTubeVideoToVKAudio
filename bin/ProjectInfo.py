import os
import re

class ProjectInformation:
    def __init__(self):
        self.__current_dir = os.path.dirname(os.path.dirname(__file__))
        self.__lib_dir = f"{self.current_dir}\\lib"
        self.__src_dir = f"{self.current_dir}\\src"
        
        self.access_token = self.get_access_token()
        
    @property
    def current_dir(self):
        return self.__current_dir
    
    @property
    def lib_dir(self):
        return self.__lib_dir
    
    @property
    def src_dir(self):
        return self.__src_dir
    
    def get_access_token(self):
        with open(f"{self.__current_dir}\\config.txt", "r") as file:
            file_data = file.readline()

        return re.findall(r"vk1[^&]{0,400}", file_data)[0]
    
PI = ProjectInformation()