import vlc
import time
import argparse
import playercl
import config
import signal

def main():
    argparser = argparse.ArgumentParser(description="Dusty Player & Organizer")
    argparser.add_argument("-f", "--file", help="Path to the media file to play")
    argparser.add_argument("-d", "--directory", help="Path to the folder to play all contained media files")

    args = argparser.parse_args()
    
    if args.file:
        player = playercl.Player()
        player.load(args.file)
        player.play()
    elif args.directory:
        player = playercl.Player()
        player.play_dir(args.directory)

if __name__ == "__main__":
    conf = config.load_config()
    music_path = conf["library"]["music_scan_dir"]
    main()
    if signal.getsignal(signal.SIGINT) == signal.default_int_handler:
        print("Exiting...")