from googleapiclient.discovery import build
import json
import sys
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get("YTAPI")

def tutorial_vid(topic, save_directory):
    """
    Searches for tutorial videos on YouTube based on the given topic and saves the video URLs in a JSON file.
    @param:
        topic (str): The topic to search for tutorial videos.
        save_directory (str): The directory where the JSON file will be saved.
    Returns:
        None
    """

    youtube = build('youtube', 'v3', developerKey=api_key)
    request = youtube.search().list(
        q=topic,
        part='snippet',
        type='video',
        relevanceLanguage='en',  # Ensures videos are relevant to English language
        regionCode='US',  # Restricts the search results to a specific country
        maxResults=10,  # Limit the number of results
        videoDuration = "long"
    )
    response = request.execute()
    
    videos = []
    for item in response['items']:
        video_id = item['id']['videoId']
        video_url = f"https://www.youtube.com/embed/{video_id}" # Storing the video URL
        videos.append({"url": video_url})
    
    json_file_path = os.path.join(save_directory, f"{topic}.json")
    with open(json_file_path, "w") as f:
        json.dump(videos, f)

def news_vid(topic, save_directory):
    """
    Searches for YouTube videos related to a given topic and saves the video URLs in a JSON file.
    @param:
        topic (str): The topic to search for.
        save_directory (str): The directory where the JSON file will be saved.
    Returns:
        None
    """

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
    
    videos = []
    for item in response['items']:
        video_id = item['id']['videoId']
        video_url = f"https://www.youtube.com/embed/{video_id}"
        videos.append({"url": video_url})
    
    json_file_path = os.path.join(save_directory, f"{topic}.json")
    with open(json_file_path, "w") as f:
        json.dump(videos, f)

# topic = input("Enter a topic: ")
# topic += " Tutorial"
# videos = get_videos_via_api(topic, api_key)

if __name__ == '__main__':
    topic = sys.argv[1]
    save_directory = sys.argv[2]
    topic_tutorial = topic + " Tutorial"
    topic_news = topic + " Latest News"
    tutorial_json = tutorial_vid(topic_tutorial, save_directory)
    news_json = news_vid(topic_news, save_directory)