import praw
import json
import html
from datetime import datetime
from concurrent.futures import ProcessPoolExecutor


CLIENT_ID = "IkJwFr_YcGLsRnc1g6216A"
CLIENT_SECRET = "1LKXge1Ze7SjZn8h0OIYZmO43n2j4w"
USER_AGENT = "script:comment_scraper:v1.0"

def load_comments(subreddit_name, limit=50):

    reddit = praw.Reddit(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        user_agent=USER_AGENT
    )

    comments = []

    subreddit = reddit.subreddit(subreddit_name)

    for comment in subreddit.comments(limit=limit):
        comments.append({
            "id": comment.id,
            "subreddit": subreddit_name,
            "author": str(comment.author),
            "text": html.unescape(comment.body),
            "created": datetime.fromtimestamp(comment.created_utc).isoformat()
        })

    print(f"{subreddit_name}: отримано {len(comments)} коментарів")

    return comments


def main():
    subreddits = ["PythonLearning", "learnpython", "programming"]
    all_comments = []

    with ProcessPoolExecutor() as executor:
        results = executor.map(load_comments, subreddits)
        for comment in results:
            all_comments.extend(comment)

    all_comments.sort(key=lambda x: x["created"])

    with open("reddit_comments.json", "w", encoding="utf-8") as file:
        json.dump(all_comments, file, indent=4)

    print(f"Збережено {len(all_comments)} коментарів")

if __name__ == "__main__":
    main()