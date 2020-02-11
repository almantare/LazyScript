import os
import time

try:
    import termcolor
except ImportError:
    os.system('pip3 install termcolor')
    import termcolor
    os.system('clear')
    print(termcolor.colored(' =================================================================', 'green'))
    s = termcolor.colored('UPLOADED', 'red') + termcolor.colored('              |', 'green')
    print(termcolor.colored('|               The missing components are ', 'green') + s)
    print(termcolor.colored(' =================================================================', 'green'))
    temp = input("Press Enter to continue...")


def checkroot():
    if os.geteuid() == 0:
        return True
    return False


def do_upgrade():
    os.system('clear')
    os.system('apt-get update && apt-get upgrade')


def install_mdk4():
    os.chdir('/home/' + os.getlogin())
    os.system('git clone https://github.com/aircrack-ng/mdk4')
    os.chdir('/home/' + os.getlogin() + '/mdk4')
    os.system('apt-get install pkg-config libnl-3-dev libnl-genl-3-dev libpcap-dev')
    os.system('make')
    os.system('make install')


def install_sherlock():
    os.chdir('/home/' + os.getlogin())
    os.system('git clone https://github.com/sherlock-project/sherlock')
    os.chdir('/home/' + os.getlogin() + '/sherlock')
    os.system('pip3 install -r requirements.txt')
    os.system('python3 ./sherlock.py -h')


def change_wallpapers():
    os.chdir('/home/' + os.getlogin())
    link = "https://cdn.wallscloud.net/converted/2101555372-gori-xN2l-1920x1080-MM-100.jpg"
    os.system('wget ' + link)
    os.system('gsettings set org.gnome.desktop.background picture-uri file:/home/' + os.getlogin() + '/2101555372-gori-xN2l-1920x1080-MM-100.jpg')


def loading(body: str):
    os.system('clear')
    for i in range(20):
        if i % 3 == 0:
            print(body + "...-")
            time.sleep(0.2)
            os.system('clear')
        elif i % 3 == 1:
            print(body + '.../')
            time.sleep(0.2)
            os.system('clear')
        elif i % 3 == 2:
            print(body + '...|')
            time.sleep(0.2)
            os.system('clear')


def main_installation():
    before_s = '\n' * 5 + 76 * ' ' + '| '
    post_s = ' ' + '|' + ' ' * 10 + "\n" * 5
    #-----------------------------
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
    #-----------------------------
    tools_to_uninstall = ['firefox']
    #-----------------------------
    loading('Starting installing most wanted tools')
    for i in tools_to_install:
        print(before_s + i + post_s)
        os.system('apt-get install ' + i)
    loading('closing installing process')
    print('------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(before_s + 'STARTING UNISTALL' + post_s)
    print('------------------------------------------------------------------------------------------------------------------------------------------------------')
    for i in tools_to_uninstall:
        print(before_s + i + post_s)
        os.system('apt-get purge ' + i)
        loading('closing uninstalling process')


def parsing_os_info():
    temp = termcolor.colored(os.uname().__str__().split()[1][10:-2], 'green') + ':' + termcolor.colored('~', 'blue') + '$ '
    return termcolor.colored(os.getlogin(), 'green') + termcolor.colored('@', 'green') + temp


def print_pic():
    t = termcolor.colored(' script', 'red')
    print(termcolor.colored(' __', 'red') + '	            ____' + termcolor.colored('           _______', 'blue') + termcolor.colored('    ___     ___', 'green'))
    print(termcolor.colored('|  |', 'red') + '	           / /\ |' + termcolor.colored('         |____  /', 'blue') + termcolor.colored('    \  \   /  /', 'green'))
    print(termcolor.colored('|  |', 'red') + '              / /  \ |' + termcolor.colored('            / /', 'blue') + termcolor.colored('      \  \_/  /', 'green'))
    print(termcolor.colored('|  |', 'red') + '             / /____\ |' + termcolor.colored('          / /', 'blue') + termcolor.colored('        \     /', 'green'))
    print(termcolor.colored('|  |', 'red') + '            / /------\ |' + termcolor.colored('        / /', 'blue') + termcolor.colored('          \   /', 'green'))
    print(termcolor.colored('|  |______', 'red') + '     / /        \ |' + termcolor.colored('      / /___', 'blue') + termcolor.colored('         | |', 'green'))
    print(termcolor.colored('|_________|', 'red') + '   /_/          \_|' + termcolor.colored('    /______|', 'blue') + termcolor.colored('        |_|', 'green') + t)


def show_help():
    print_pic()
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


def print_menu():
    print_pic()
    s_num_1 = termcolor.colored('[', 'red')
    s_num_2 = termcolor.colored(']', 'red')
    print()
    print(termcolor.colored(' =================================================', 'green'))
    print(termcolor.colored('|               Created by ', 'green') + termcolor.colored('Almantare', 'red') + termcolor.colored('              |', 'green'))
    print(termcolor.colored(' =================================================', 'green'))
    print(s_num_1 + termcolor.colored('0', 'blue') + s_num_2 + '  ' + termcolor.colored('help', 'green'))
    print(s_num_1 + termcolor.colored('1', 'blue') + s_num_2 + '  ' + termcolor.colored('upgrade', 'green'))
    print(s_num_1 + termcolor.colored('2', 'blue') + s_num_2 + '  ' + termcolor.colored('install default tools', 'green'))
    print(s_num_1 + termcolor.colored('3', 'blue') + s_num_2 + '  ' + termcolor.colored('change wallpapers', 'green'))
    print(s_num_1 + termcolor.colored('4', 'blue') + s_num_2 + '  ' + termcolor.colored('install mdk4', 'green'))
    print(s_num_1 + termcolor.colored('5', 'blue') + s_num_2 + '  ' + termcolor.colored('install sherlock', 'green'))
    print(s_num_1 + termcolor.colored('6', 'blue') + s_num_2 + '  ' + termcolor.colored('execute command', 'green'))
    print(s_num_1 + termcolor.colored('7', 'blue') + s_num_2 + ' ' + termcolor.colored(' full installation', 'green'))
    print(s_num_1 + termcolor.colored('r', 'blue') + s_num_2 + ' ' + termcolor.colored(' reload script', 'green'))
    print(s_num_1 + termcolor.colored('99', 'blue') + s_num_2 + ' ' + termcolor.colored('exit', 'green'))
    print()


def menu():
    print_menu()
    choice = input('select option: ')
    if choice == '99' or choice == 'exit':
        os.system('clear')
        exit()
    elif choice == '0':
        os.system('clear')
        show_help()
        temp = input(termcolor.colored("press Enter to continue...", 'green'))
        os.system('clear')
        menu()
    elif choice == '1':
        os.system('clear')
        do_upgrade()
        os.system('clear')
        menu()
    elif choice == '2':
        os.system('clear')
        main_installation()
        os.system('clear')
        menu()
    elif choice == '3':
        os.system('clear')
        change_wallpapers()
        os.system('clear')
        menu()
    elif choice == '4':
        os.system('clear')
        install_mdk4()
        os.system('clear')
        menu()
    elif choice == '5':
        os.system('clear')
        install_sherlock()
        os.system('clear')
    elif choice == '6':
        command = input(termcolor.colored("which command will we execute today, Captain?\n", 'blue') + parsing_os_info())
        os.system(command)
        temp = input(termcolor.colored("press Enter to continue...", 'red'))
        os.system('clear')
        menu()
    elif choice == '7':
        do_upgrade()
        main_installation()
        install_mdk4()
        install_sherlock()
        change_wallpapers()
        os.system('clear')
        menu()
    elif choice == 'r':
        os.chdir('/home/almantare/PycharmProjects/fpython/')
        os.system('sudo python3 LazyScript.py')
        exit()
    else:
        os.system('clear')
        menu()


if checkroot():
    os.system('clear')
    menu()
else:
    print(termcolor.colored("You need to have root privileges to run this script. \nPlease try again, this time using 'sudo'.", 'red'))



