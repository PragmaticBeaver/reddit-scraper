from dotenv import load_dotenv
import os
import praw

load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("SECRET"),
    user_agent=os.getenv("USER_AGENT"),
)

hot_posts = reddit.subreddit("AskReddit").hot(limit=10)
for post in hot_posts:
    print(post.title)
