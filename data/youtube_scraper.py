from typing import List, Dict
from googleapiclient.discovery import Resource

def authenticate_youtube(api_key: str) -> Resource:
    """
    Authenticate YouTube API using the provided API key.

    :param api_key: YouTube API key
    :return: YouTube API resource object
    """
    from googleapiclient.discovery import build
    youtube: Resource = build('youtube', 'v3', developerKey=api_key)
    return youtube

def scrape_youtube_videos(youtube: Resource, search_query: str, max_results: int = 50) -> List[Dict[str, str]]:
    """
    Scrape YouTube videos for a given search query.

    :param youtube: Authenticated YouTube API resource
    :param search_query: Search term for querying videos
    :param max_results: Maximum number of results to retrieve
    :return: List of dictionaries containing video data
    """
    request = youtube.search().list(
        part="snippet",
        q=search_query,
        type="video",
        maxResults=max_results
    )
    response: Dict = request.execute()
    video_data: List[Dict[str, str]] = []
    for item in response['items']:
        video_data.append({
            'video_id': item['id']['videoId'],
            'title': item['snippet']['title'],
            'description': item['snippet']['description'],
            'published_at': item['snippet']['publishedAt']
        })
    return video_data
