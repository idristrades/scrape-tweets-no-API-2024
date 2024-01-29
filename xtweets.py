from ntscraper import Nitter
import json

scraper = Nitter(log_level=1, skip_instance_check=False)

tweets = scraper.get_tweets("elonmusk", mode='user', number=100)

with open("twts.json", "w") as file:
    json.dump(tweets, file, indent=4)

#first, run: pip install ntscraper
