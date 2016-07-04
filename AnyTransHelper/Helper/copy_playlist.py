import os
import re
import shutil
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))
from urllib import parse
from AnyTransHelper import settings
import xmltodict


class CopyPlaylist:

    def __init__(self, filename, username):
        self.filename = filename
        self.username = username
        self.playlist_loc = ''

    # copy files from xml to new directory
    def copy_files(self):
        with open(self.filename) as f:
            doc = xmltodict.parse(f.read())
            playlist = doc['plist']['dict']['dict']['dict']
            print('Copying files..')
            for counter, song in enumerate(playlist):
                # Print copy progress to console using string formatting and carriage return
                sys.stdout.write('{0}\r'.format(str(counter + 1) + ' of ' + str(len(playlist))))
                # .flush() writes all buffered data stored until this point
                sys.stdout.flush()
                # file location is the last index in the branch
                file_loc = song['string'][-1]
                # regex to match only abs path of file including any special characters
                regex_file = re.search(r'/[\w/%.\-\(\)&$\']+', file_loc)
                # decode url encoding to display ascii chars
                decoded_file_loc = parse.unquote(regex_file.group())
                # copy file to directory. Create directory if it doesn't exist already
                shutil.copy(decoded_file_loc, self.create_directory())
            print("\nDone!")
        return counter

    def create_directory(self):
        self.playlist_loc = '/Users/'+self.username+'/Music/AnyTransHelper'
        if not os.path.exists(self.playlist_loc):
            os.makedirs(self.playlist_loc)
            return(self.playlist_loc)
        return self.playlist_loc

if __name__ == '__main__':
    itunes = CopyPlaylist(settings.xml_playlist_loc, settings.music_folder_dir)
    itunes.copy_files()
