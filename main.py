from dotenv import load_dotenv
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


def download_image(name, url):
    _, file_extension = os.path.splitext(url)
    file_name = f"{name}.{file_extension}"
    res = requests.get(url, stream=True)
    if res.status_code == 200:
        with open(file_name, "wb") as f:
            shutil.copyfileobj(res.raw, f)
        print("Image sucessfully Downloaded: ", file_name)
    else:
        print("Image Couldn't be retrieved")


reddit = praw.Reddit(
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("SECRET"),
    user_agent=os.getenv("USER_AGENT"),
)

# hot posts
hot_posts = reddit.subreddit(os.getenv("SUBREDDIT")).hot(limit=2)
for post in hot_posts:
    # post.over_18
    print(post.title)  # Post title
    print(post.selftext)  # Post text
    url = post.url
    file_name = convert_to_snake_case(post.title)
    download_image(file_name, url)
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
