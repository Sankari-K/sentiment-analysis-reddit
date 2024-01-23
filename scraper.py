import praw
import pandas as pd
import numpy as np
import re 
from keys import CLIENT_ID, CLIENT_SECRET

FILE = "data.txt"

user_agent = "Reddit Scraper"
reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    user_agent=user_agent
)

def fetch_data(reddit, file):
    headlines = []
    for submission in reddit.subreddit("apple").top(time_filter="year", limit=500):
        headlines.append(submission.title) # subreddit title

    with open(file, "w") as f:
        for headline in headlines:
            f.writelines(headline)
            f.write("\n")

def load_data(file):
    with open(file, "r") as f:
        headlines = f.read().split("\n")
        return headlines

def clean_text(text):
    text = re.sub(r"@[A-Za-z0-9]+", "", text) # remove @mentions replace with blank
    text = re.sub(r"#", "", text) # remove the # symbol, replace with blank
    text = re.sub(r"RT[\s]+", "", text) # removing RT, replace with blank
    text = re.sub(r"https?:\/\/\S+", "", text) # remove the hyperlinks
    text = re.sub(r":", "", text) # remove :
    return text

def remove_emoji(string):
    emoji_pattern = re.compile("["
    u"\U0001F600-\U0001F64F" # emoticons
    u"\U0001F300-\U0001F5FF" # symbols & pictographs
    u"\U0001F680-\U0001F6FF" # transport & map symbols
    u"\U0001F1E0-\U0001F1FF" # flags (iOS)
    u"\U00002500-\U00002BEF" # chinese char
    u"\U00002702-\U000027B0"
    u"\U00002702-\U000027B0"
    u"\U000024C2-\U0001F251"
    u"\U0001f926-\U0001f937"
    u"\U00010000-\U0010ffff"
    u"\u2640-\u2642"
    u"\u2600-\u2B55"
    u"\u200d"
    u"\u23cf"
    u"\u23e9"
    u"\u231a"
    u"\ufe0f"
    u"\u3030"
    "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r"", string)

# fetch_data(reddit, FILE)
headlines = load_data(FILE)

# create a data frame
apple_df = pd.DataFrame(headlines)
apple_df.columns = ["Titles"]

# data cleaning and transformation
apple_df.Titles.duplicated().sum()
apple_df["Titles"]= apple_df["Titles"].apply(clean_text)
     
# cleaning the text
apple_df["Titles"]= apple_df["Titles"].apply(remove_emoji)

# show the clean text
print(apple_df.head())

