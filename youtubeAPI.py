from apiclient.discovery import build

DEVELOPER_KEY = "your_api_key"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtubeSearch(searchtext):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey = DEVELOPER_KEY)
    search_response = youtube.search().list(
        q = searchtext,
        type = "video",
        part = "id,snippet",
        maxResults = 3
    ).execute()

    search_videos = []

    for search_result in search_response.get("items", []):
        # print(search_result)		# ------ print search results
        search_videos.append(search_result["id"]["videoId"])
    video_ids = ",".join(search_videos)

    video_response = youtube.videos().list(
        id = video_ids,
        part = 'statistics'
    ).execute()

    viewCount = likeCount = dislikeCount = 0

    for video in video_response.get("items"):
        try:
            viewCount += int(video["statistics"]["viewCount"])
            likeCount += int(video["statistics"]["likeCount"])
            dislikeCount += int(video["statistics"]["dislikeCount"])
        except KeyError:
            pass

    return {'viewCount':viewCount, 'likeCount': likeCount, 'dislikeCount': dislikeCount}
