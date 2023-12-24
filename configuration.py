import os
from pydantic import BaseModel
import lesson22_hw
from lesson22_hw.utils import file_path


class Settings(BaseModel):
    context: str
    login: str = os.getenv('LOGIN')
    password: str = os.getenv('PASSWORD')
    appWaitActivity: str = os.getenv('appWaitActivity')
    remote_url: str = os.getenv('remote_url')
    udid: str = os.getenv('udid')
    app: str = os.getenv('app')
    platformVersion: str = os.getenv('platformVersion')
    deviceName: str = os.getenv('deviceName')
    projectName: str = os.getenv('projectName')
    buildName: str = os.getenv('buildName')
    sessionName: str = os.getenv('sessionName')

    def to_driver_options(self, context):

        if context == 'local_emulator':
            options: str = {
                'app': lesson22_hw.utils.file_path.abs_path_from_project(self.app),
                'appWaitActivity': self.appWaitActivity,
                'udid': self.udid,
            }

        if context == 'local_real':
            options: str = {
                'app': lesson22_hw.utils.file_path.abs_path_from_project(self.app),
                'appWaitActivity': self.appWaitActivity,
                'udid': self.udid
            }

        if context == 'bstack':
            options: str = {
                'platformVersion': self.platformVersion,
                'deviceName': self.deviceName,
                'app': self.app,
                'bstack:options': {
                    'projectName': self.projectName,
                    'buildName': self.buildName,
                    'sessionName': self.sessionName,
                    'userName': self.login,
                    'accessKey': self.password,
                }
            }

        return options


settings = Settings(context="bstack")
