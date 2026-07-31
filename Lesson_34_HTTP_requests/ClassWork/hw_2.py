# Для даного завдання можете використати бібліотеку: https://praw.readthedocs.io/en/stable/getting_started/quick_start.html
# Щось такого плану:
import praw
from datetime import datetime
import json
import html


reddit = praw.Reddit(
    client_id="something....",
    client_secret="something....",
    user_agent="something...."
)

all_comments = []
for comment in reddit.subreddit("PythonLearning").comments(limit=25):
    # put your logic here
    pass