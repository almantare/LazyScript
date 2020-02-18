import os


class reloader:
    def __init__(self, point) -> None:
        self.point = point
        self.__name__ = 'reload script'

    def menu_name(self):
        return self.__name__

    def run(self):
        os.system('sudo python3 ' + os.path.abspath(os.curdir) + '/application.py')

    def get_point(self):
        return self.point