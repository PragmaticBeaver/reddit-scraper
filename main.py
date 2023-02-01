from dotenv import load_dotenv
from pathlib import Path
from datetime import datetime
import os
import praw
import requests
import shutil

load_dotenv()


def convert_to_snake_case(text):
    length = len(text)
    characters = list(text)
    for i in range(length):
        if characters[i] == " ":
            characters[i] = "_"
        else:
            characters[i] = characters[i].lower()
    return "".join(characters)


def download_image(file_path, url):
    res = requests.get(url, stream=True)
    if res.status_code == 200:
        with open(file_path, "wb") as f:
            shutil.copyfileobj(res.raw, f)
        print("Image sucessfully Downloaded: ", file_path)
    else:
        print("Image Couldn't be retrieved")


reddit = praw.Reddit(
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("SECRET"),
    user_agent=os.getenv("USER_AGENT"),
)

# create dir
dir_path = os.path.join("./downloads", datetime.now().isoformat())
Path(dir_path).mkdir(parents=True, exist_ok=True)

# hot posts
hot_posts = reddit.subreddit(os.getenv("SUBREDDIT")).hot(limit=2)
for post in hot_posts:
    # post.over_18
    print(post.title)  # Post title
    print(post.selftext)  # Post text
    url = post.url
    name = convert_to_snake_case(post.title)
    _, file_extension = os.path.splitext(url)
    file_name = f"{name}.{file_extension}"
    file_path = os.path.join(dir_path, file_name)
    download_image(file_path, url)
    # post.created_utc

    # # comments of post
    # max_comment_count = post.comment_limit
    # comment_limit = int(os.getenv("COMMENT_LIMIT"))
    # counter = max_comment_count if max_comment_count < comment_limit else comment_limit
    # for x in range(counter):
    #     comment = post.comments[x]
    #     print(x, comment.body)
    #     # comment.body
    #     # comment.ups
    #     # comment.over_18
    print("<== END ==>")
