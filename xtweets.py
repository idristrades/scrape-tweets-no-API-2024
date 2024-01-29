#First, open the terminal and run: 'pip install ntscraper'
from ntscraper import Nitter
import json

#Get the latest 100 tweets from a single user (@elonmusk in this example)
tweets = Nitter().get_tweets("elonmusk", mode='user', number=100)

#Export the data in json format
with open("elon.json", "w") as file:
    json.dump(tweets, file, indent=4)
