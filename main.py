from dotenv import load_dotenv
import os
import praw

load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("SECRET"),
    user_agent=os.getenv("USER_AGENT"),
)

# hot posts
hot_posts = reddit.subreddit(os.getenv("SUBREDDIT")).hot(limit=10)
for post in hot_posts:
    # post.over_18
    print(post.title)  # Post title
    print(post.selftext)  # Post text
    # post.created_utc

    # comments of post
    comment_limit = post.comment_limit
    counter = comment_limit if comment_limit < 25 else 25
    for x in range(counter):
        comment = post.comments[x]
        print(x, comment.body)
        # comment.body
        # comment.ups
        # comment.over_18

    print("<== END ==>")
