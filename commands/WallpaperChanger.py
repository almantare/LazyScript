import os


class WallpaperChanger:

    def __init__(self, point) -> None:
        self.point = point
        self.__name__ = 'change wallpapers'

    def menu_name(self):
        return self.__name__

    def run(self):
        os.chdir('/home/' + os.getlogin())
        link = "https://cdn.wallscloud.net/converted/2101555372-gori-xN2l-1920x1080-MM-100.jpg"
        os.system('wget ' + link)
        os.system(
            'gsettings set org.gnome.desktop.background picture-uri file:/home/' + os.getlogin() + '/2101555372-gori-xN2l-1920x1080-MM-100.jpg')

    def get_point(self):
        return self.point


