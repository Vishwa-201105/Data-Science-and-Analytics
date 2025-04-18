from googleapiclient.discovery import build
from textblob import TextBlob
import pandas as pd
import time

api_key = 'AIzaSyDPO_s6xS7LeWnVoz3E4pDrEYW4fqYHb-0'
channel_id = 'UCV6KDgJskWaEckne5aPA0aQ' 

youtube = build('youtube', 'v3', developerKey=api_key)

def get_video_ids(channel_id):
    video_ids = []
    request = youtube.search().list(
        part="id",
        channelId=channel_id,
        maxResults=50,
        order="date",
        type="video"
    )
    response = request.execute()
    for item in response['items']:
        video_ids.append(item['id']['videoId'])
    return video_ids


def get_video_details(video_id):
    stats = youtube.videos().list(
        part="snippet,statistics",
        id=video_id
    ).execute()

    item = stats['items'][0]
    snippet = item['snippet']
    statistics = item['statistics']

    return {
        "video_id": video_id,
        "title": snippet['title'],
        "publishedAt": snippet['publishedAt'],
        "views": int(statistics.get("viewCount", 0)),
        "likes": int(statistics.get("likeCount", 0)),
        "comments": int(statistics.get("commentCount", 0))
    }


def get_comments(video_id, max_comments=50):
    comments = []
    try:
        request = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            maxResults=max_comments,
            textFormat="plainText"
        )
        response = request.execute()

        for item in response['items']:
            comment = item['snippet']['topLevelComment']['snippet']
            text = comment['textDisplay']
            sentiment = TextBlob(text).sentiment.polarity
            comments.append({
                "video_id": video_id,
                "comment": text,
                "sentiment": sentiment
            })
    except Exception as e:
        print(f"Error getting comments for {video_id}: {e}")

    return comments

print("Fetching video IDs...")
video_ids = get_video_ids(channel_id)

print("Fetching video details...")
video_data = [get_video_details(vid) for vid in video_ids]

print("Fetching comments and performing sentiment analysis...")
all_comments = []
for vid in video_ids:
    print(f"Processing video: {vid}")
    comments = get_comments(vid)
    all_comments.extend(comments)
    time.sleep(1)

print("Saving video data to video_data.csv...")
pd.DataFrame(video_data).to_csv("video_data.csv", index=False)

print("Saving comment data to comment_sentiment.csv...")
pd.DataFrame(all_comments).to_csv("comment_sentiment.csv", index=False, quoting=1)

print(" Data collection and saving completed successfully!")
