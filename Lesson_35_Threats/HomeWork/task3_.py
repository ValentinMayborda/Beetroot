import praw
import threading
import json
import html
from datetime import datetime


reddit = praw.Reddit(
    client_id='IkJwFr_YcGLsRnc1g6216A',
    client_secret='1LKXge1Ze7SjZn8h0OIYZmO43n2j4w',
    user_agent='script:comment_scraper:v1.0'
)

all_comments = []
lock = threading.Lock()

def load_comments(subreddit_name, limit=50):
    subreddit = reddit.subreddit(subreddit_name)
    comments = []

    for comment in subreddit.comments(limit=limit):

        data = {
            "id": comment.id,
            "subreddit": subreddit_name,
            "author": str(comment.author),
            "text": html.unescape(comment.body),
            "created": datetime.fromtimestamp(comment.created_utc).isoformat()
        }

        comments.append(data)

    with lock:
        all_comments.extend(comments)


    print(
        f"{threading.current_thread().name}: "
        f"отримано {len(comments)} коментарів "
        f"з {subreddit_name}"
    )

subreddits = ["PythonLearning", "learnpython", "programming"]
threads = []

for subreddit in subreddits:
    thread = threading.Thread(target=load_comments,args=(subreddit, 50))
    threads.append(thread)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

all_comments.sort(key=lambda x: x["created"])

with open("reddit_comments.json","w", encoding="utf-8") as file:

    json.dump(all_comments,file, indent=4)

print(f"Збережено {len(all_comments)} коментарів")