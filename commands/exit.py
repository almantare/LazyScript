import os


class doExit:

    def __init__(self, point) -> None:
        self.point = point
        self.__name__ = 'exit'

    def get_point(self):
        return self.point

    def menu_name(self):
        return self.__name__

    def run(self):
        os.system('clear')
        exit()
