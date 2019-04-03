from gooey import Gooey, GooeyParser
import getpass
import youtube_dl
import os
username = getpass.getuser()
default_loc="C:\\Users\\"+username+"\\Downloads"


def if_it_is_playlist(ytlink):
    ydl_opts={
        'format':"bestvideo+bestaudio",
        'outtmpl':'%(autonumber)s-%(title)s.%(ext)s'
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([ytlink])


def notPlaylist(ytlink):
    ydl_opts={
        'format':"bestvideo+bestaudio",
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([ytlink])

@Gooey()
def main():
    parser = GooeyParser(description='YouTube Downloader both Playlist and video')
    parser.add_argument(
        'Link',
        help='Enter some youtube link!')
    parser.add_argument(
        '--Select_Directory',
        metavar='Download location',
        widget='DirChooser',
        help='Please Select the folder where you want to download',
        default=default_loc)
    args = parser.parse_args()
    
    ytlink=args.Link
    location_of_folder=args.Select_Directory
    try:
        os.chdir(location_of_folder)
    except:
        print ("error")

    if "playlist" in ytlink.lower():
        if_it_is_playlist(ytlink)
    else:
        notPlaylist(ytlink)

    
if __name__ == '__main__':
    main()
