import praw
from keys import CLIENT_ID, CLIENT_SECRET

user_agent = "Reddit Scraper"
reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    user_agent=user_agent
)

for submission in reddit.subreddit("onlyconnect").hot(limit=20):
    print(submission.title) #Subreddit Title

