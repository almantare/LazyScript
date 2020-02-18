import os


class mdk4Installer:
    def __init__(self, point) -> None:
        self.point = point
        self.__name__ = 'install mdk4'

    def menu_name(self):
        return self.__name__

    def run(self):
        os.chdir('/home/' + os.getlogin())
        os.system('git clone https://github.com/aircrack-ng/mdk4')
        os.chdir('/home/' + os.getlogin() + '/mdk4')
        os.system('apt-get -y install pkg-config libnl-3-dev libnl-genl-3-dev libpcap-dev')
        os.system('make')
        os.system('make install')

    def get_point(self):
        return self.point
