import os, termcolor


class main_Installation:
    def __init__(self, point) -> None:
        self.point = point
        self.__name__ = 'main installation'

    def menu_name(self):
        return self.__name__

    def run(self):
        before_s = termcolor.colored('\n' * 5 + 76 * ' ' + '| ', 'red')
        post_s = termcolor.colored(' ' + '|' + ' ' * 10 + "\n" * 5, 'red')
        tools_to_install = ['gnome-tweaks',
                            'net-tools',
                            'chromium-browser',
                            'pycharm-community',
                            'clion',
                            'git',
                            'aircrack-ng',
                            'proxychains',
                            'g++',
                            'cmake',
                            'gcc',
                            'python3-pip',
                            'snap',
                            'wget',
                            'make',
                            'curl']
        tools_to_uninstall = ['firefox']
        for i in tools_to_install:
            print(before_s + termcolor.colored(i, 'green') + post_s)
            os.system('apt-get install ' + i)
        for i in tools_to_uninstall:
            print(before_s + i + post_s)
            os.system('apt-get purge ' + i)

    def get_point(self):
        return self.point
