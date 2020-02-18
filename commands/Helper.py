import termcolor


class Helper:

    def __init__(self, point) -> None:
        self.point = point
        self.__name__ = 'help'

    def menu_name(self):
        return self.__name__

    def run(self):
        print(termcolor.colored(r"""
        *upgrade - getting update and upgrading ur packages

        *install default tools - installing next tools:
            --gnome-tweaks
            --net-tools
            --chromium-browser
            --pycharm-community
            --clion
            --git
            --aircrack-ng
            --proxychains
            --g++
            --cmake
            --gcc
            --pip3
            --snap
            --wget
            --make
            --curl
            if it possible this installation script remove firefox.

        *change wallpapers - change wallpapers to https://cdn.wallscloud.net/converted/2101555372-gori-xN2l-1920x1080-MM-100.jpg

        *install mdk4 - installing mdk4

        *install sherlock - installing sherlock

        *execute command - executing bash command

        *full installation - makes full installation. all tools that were written above with mdk4 and sherlock.

        *exit - terminates the script)

        *reload script - u know what does it mean""", 'blue'))
        temp = input("press ENTER to continue...")

    def get_point(self):
        return self.point


