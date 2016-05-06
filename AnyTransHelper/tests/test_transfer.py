import os
from AnyTransHelper.Helper.copy_playlist import CopyPlaylist
from AnyTransHelper import settings


def test_file_exists():
    assert(open(settings.xml_playlist_loc))


def test_copy_files():
    music = CopyPlaylist(settings.xml_playlist_loc, settings.music_folder_dir)
    assert(music.copy_files() > 0)


def test_make_directory():
    music = CopyPlaylist(settings.xml_playlist_loc, settings.music_folder_dir)
    music_dir = music.create_directory()
    assert(os.path.exists(music_dir))
