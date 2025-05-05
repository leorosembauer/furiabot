import requests
from bs4 import BeautifulSoup

YOUTUBE_URL = "https://www.youtube.com/@FURIA/videos"

def get_recent_clips(limit=5):
    response = requests.get(YOUTUBE_URL)
    soup = BeautifulSoup(response.text, 'html.parser')

    clips = []
    for video in soup.select('a#video-title')[:limit]:
        title = video.text.strip()
        url = "https://www.youtube.com" + video['href']
        clips.append(f"{title}\n{url}")
    
    return clips
