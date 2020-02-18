import os
import termcolor


class executer:
    def __init__(self, point) -> None:
        self.point = point
        self.__name__ = 'execute command'

    def menu_name(self):
        return self.__name__

    def parsing_os_info(self):
        temp = termcolor.colored(os.uname().__str__().split()[1][10:-2], 'green') + ':' + termcolor.colored('~', 'blue') + '$ '
        return termcolor.colored(os.getlogin(), 'green') + termcolor.colored('@', 'green') + temp

    def run(self):
        command = input(termcolor.colored("which command will we execute today, Captain?\n", 'blue') + self.parsing_os_info())
        os.system(command)
        temp = input("press ENTER to continue...")

    def get_point(self):
        return self.point