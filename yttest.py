from selenium_youtube import Youtube

# pip install selenium_chrome
from selenium_chrome import *

from multiprocessing import Process, freeze_support



if __name__ == "__main__":
    freeze_support()  # needed for Windows

    chrome = Chrome(headless=True)
    #chrome.add_cookie({"name": "key", "value": "value"})

    youtube = Youtube(
        browser=chrome # or firefox
    )
    print('1')
    upload_result = youtube.upload('path_to_video', 'title', 'description', ['tag1', 'tag2'])
    print('2')
    input("Press Enter to continue...")
