import  global_data
import requests

class Request:
    def __init__(self,git_url:str):
        self.git_url = git_url
        self.data=global_data.default_req
        self.data["gitUrl"]=self.git_url

        self.target=global_data.default_target

    def set_data(self,key:str,value:str):
        self.data[key]=value

    def set_target(self,target:str):
        self.target=target

    def request(self):
        response = requests.post(global_data.default_target,data=self.data)
        if response.status_code!=200:
            raise Exception("request error")
        return response.text




