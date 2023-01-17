import os
import argparse

from dotenv import find_dotenv, load_dotenv

DOTENV_PATH = find_dotenv()
if DOTENV_PATH:
    load_dotenv(DOTENV_PATH)


if __name__ == "__main__":
    # instantiate a parser
    parser = argparse.ArgumentParser()

    # required arguments
    parser.add_argument("video_id", help="ID of video to process.")

    # parse arguments
    args = parser.parse_args()
    video_id = args.video_id

    print(video_id)
