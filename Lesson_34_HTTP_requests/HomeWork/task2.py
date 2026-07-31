import praw
from datetime import datetime
import json
import html


reddit = praw.Reddit(
    client_id='IkJwFr_YcGLsRnc1g6216A',
    client_secret='1LKXge1Ze7SjZn8h0OIYZmO43n2j4w',
    user_agent='script:comment_scraper:v1.0'
)

all_comments = []

for comment in reddit.subreddit("PythonLearning").comments(limit=25):

    data = {
        "id": comment.id,
        "author": str(comment.author),
        "text": html.unescape(comment.body),
        "created": datetime.fromtimestamp(comment.created_utc).isoformat()
    }

    all_comments.append(data)

    # сортування по часу
    all_comments.sort(key=lambda x: x["created"])

    # запис у JSON
    with open("reddit_comments.json","w",encoding="utf-8") as file:
        json.dump(all_comments, file,indent=4)

    print(f"Збережено {len(all_comments)} коментар")

