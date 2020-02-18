import os


class upgrader:
    def __init__(self, point) -> None:
        self.point = point
        self.__name__ = 'upgrade'

    def menu_name(self):
        return self.__name__

    def run(self):
        os.system('apt-get update && apt-get upgrade')

    def get_point(self):
        return self.point
