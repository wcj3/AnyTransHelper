import os
import re
import shutil
from urllib import parse
from AnyTransHelper import settings
import xmltodict


class CopyPlaylist:

    def __init__(self, filename, username):
        self.filename = filename
        self.username = username
        self.playlist_loc = ''

    def copy_files(self):
        with open(self.filename) as f:
            doc = xmltodict.parse(f.read())
            playlist = doc['plist']['dict']['dict']['dict']
            for counter, song in enumerate(playlist):
                file_name = song['key'].index("Name")
                file_index = song['key'].index("Location")
                print(song['key'][file_name], song['string'][file_name])
                print(song['key'][file_index], song['string'][-1])
                file_loc = song['string'][-1]
                regex_file = re.search(r'C:/[\w\/\%.\-\(\)\&]+', file_loc)
                decoded_file_loc = parse.unquote(regex_file.group())
                shutil.copy(decoded_file_loc, 'C:/users/willi/Music/AnyTransHelper/')
        return counter

    def create_directory(self):
        self.playlist_loc = 'C:/users/'+self.username+'/Music/AnyTransHelper'
        if not os.path.exists(self.playlist_loc):
            os.makedirs(self.playlist_loc)
        return self.playlist_loc

if __name__ == '__main__':
    itunes = CopyPlaylist(settings.xml_playlist_loc, settings.music_folder_dir)
    itunes.copy_files()
