import termcolor


class PickPrinter:

    def __init__(self, point) -> None:
        self.point = point
        self.__name__ = 'print pic'

    def get_point(self):
        return self.point

    def menu_name(self):
        return self.__name__

    def run(self):
        t = termcolor.colored(' script', 'red')
        print(termcolor.colored(' __', 'red') + '	            ____' + termcolor.colored('           _______',
                                                                                           'blue') + termcolor.colored(
            '    ___     ___', 'green'))
        print(termcolor.colored('|  |', 'red') + '	           / /\ |' + termcolor.colored('         |____  /',
                                                                                             'blue') + termcolor.colored(
            '    \  \   /  /', 'green'))
        print(termcolor.colored('|  |', 'red') + '              / /  \ |' + termcolor.colored('            / /',
                                                                                              'blue') + termcolor.colored(
            '      \  \_/  /', 'green'))
        print(termcolor.colored('|  |', 'red') + '             / /____\ |' + termcolor.colored('          / /',
                                                                                               'blue') + termcolor.colored(
            '        \     /', 'green'))
        print(termcolor.colored('|  |', 'red') + '            / /------\ |' + termcolor.colored('        / /',
                                                                                                'blue') + termcolor.colored(
            '          \   /', 'green'))
        print(termcolor.colored('|  |______', 'red') + '     / /        \ |' + termcolor.colored('      / /___',
                                                                                                 'blue') + termcolor.colored(
            '         | |', 'green'))
        print(termcolor.colored('|_________|', 'red') + '   /_/          \_|' + termcolor.colored('    /______|',
                                                                                                  'blue') + termcolor.colored(
            '        |_|', 'green') + t)
        print(termcolor.colored('    =================================================', 'blue'))
        print(termcolor.colored('   |               Created by ', 'green') + termcolor.colored('Almantare',
                                                                                            'red') + termcolor.colored(
            '              |', 'green'))
        print(termcolor.colored('    =================================================', 'blue'))
