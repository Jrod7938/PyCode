from typing import DefaultDict
import scrapetube
import urllib.request
import json
import urllib
import pprint
from pytube import YouTube
import os
import os.path
from os import path



from apiclient.discovery import build
from apiclient.errors import HttpError
from apiclient.http import MediaFileUpload
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import argparser, run_flow

#Gets the path of where the file will be downloaded
cwd = os.getcwd()

#Someones channel ID you'd like to copy
other_videos = scrapetube.get_channel("UCC7DOE3N7s6RfC-j3pYkEew")

#Your chanenel ID
my_videos = scrapetube.get_channel("UCu7Pwn8HPrt6C2Tk9YKI4RQ")

my_videos_list = []

for video in my_videos:
    id = video['videoId']
    params = {"format": "json", "url": "https://www.youtube.com/watch?v=%s" % id}
    url = "https://www.youtube.com/oembed"
    query_string = urllib.parse.urlencode(params)
    url = url + "?" + query_string

    with urllib.request.urlopen(url) as response:
        response_text = response.read()
        data = json.loads(response_text.decode())
        my_title = data['title']
        my_videos_list.append(my_title)

for video in other_videos:
    id = video['videoId']
    params = {"format": "json", "url": "https://www.youtube.com/watch?v=%s" % id}
    url = "https://www.youtube.com/oembed"
    query_string = urllib.parse.urlencode(params)
    url = url + "?" + query_string

    with urllib.request.urlopen(url) as response:
        response_text = response.read()
        data = json.loads(response_text.decode())
        other_title = data['title']
        if other_title not in my_videos_list and path.exists(f"{other_title}.jpg") == False:
            try:
                my_video = YouTube(f"https://www.youtube.com/watch?v={id}")
                urllib.request.urlretrieve(my_video.thumbnail_url, f"{other_title}.jpg")
                my_video = my_video.streams.get_highest_resolution()
                print(f"Downloading\n{other_title}")
                my_video.download()
                print(f"{other_title} finished downloading in {cwd}\n")

            except Exception as e:
                print(f"An error occured while downloading video\n{e}")
                exit()


    
    


