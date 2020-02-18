import os
try:
    import termcolor
except ImportError:
    os.system('apt-get install python3-pip && pip3 install termcolor')
    import termcolor
from commands.Menu import Menu
from commands.Helper import Helper
from commands.SherlockInstaller import SherlockInstaller
from commands.WallpaperChanger import WallpaperChanger
from commands.exit import doExit
from commands.main_installation import main_Installation
from commands.upgrade import upgrader
from commands.mdk4Installer import mdk4Installer
from commands.reload import reloader
from commands.executer import executer


def init_menu():
    menu = Menu()
    menu.add_command(Helper('0'))
    menu.add_command(upgrader('1'))
    menu.add_command(WallpaperChanger('2'))
    menu.add_command(main_Installation('3'))
    menu.add_command(SherlockInstaller('4'))
    menu.add_command(mdk4Installer('5'))
    menu.add_command(executer('6'))
    menu.add_command(reloader('r'))
    menu.add_command(doExit('x'))
    return menu


if os.geteuid() == 0:
    menu = init_menu()
    while True:
        os.system('clear')
        menu.print_menu_points()
        menu.run_command(input("select option: "), True)
else:
    print(termcolor.colored("You need to have root privileges to run this script. \nPlease try again, this time using 'sudo'.", 'red'))



