import os


class SherlockInstaller:

    def __init__(self, point) -> None:
        self.point = point
        self.__name__ = 'install sherlock'

    def get_point(self):
        return self.point

    def menu_name(self):
        return self.__name__

    def run(self):
        os.chdir('/home/' + os.getlogin())
        os.system('git clone https://github.com/sherlock-project/sherlock')
        os.chdir('/home/' + os.getlogin() + '/sherlock')
        os.system('pip3 install -r requirements.txt')
        os.system('python3 ./sherlock.py -h')