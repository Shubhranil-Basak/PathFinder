from googleapiclient.discovery import build
import json
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.environ.get("YTAPI")

def news_vid(topic, api_key):
    youtube = build('youtube', 'v3', developerKey=api_key)
    request = youtube.search().list(
        q=topic,
        part='snippet',
        type='video',
        relevanceLanguage='en',  # Ensures videos are relevant to English language
        regionCode='US',  # Restricts the search results to a specific country
        maxResults=10  # Limit the number of results
    )
    response = request.execute()
    
    videos = {}
    for item in response['items']:
        video_id = item['id']['videoId']
        video_title = item['snippet']['title']
        video_url = f"https://www.youtube.com/embed/{video_id}"
        videos[video_title] = video_url
    
    return json.dumps(videos)

# topic = input("Enter a topic: ")
# topic += " Latest News"
# videos = news_vid(topic, api_key)

if __name__ == '__main__':
    import sys
    topic = sys.argv[1]
    topic += " Latest News"
    videos_json = news_vid(topic, api_key)