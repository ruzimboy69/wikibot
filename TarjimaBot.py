import requests
from pprint import pprint as print
import json

words = "watch?v=bKWOhdzXljE"
url ="https://www.googleapis.com/youtube/v3/"+words

respond = requests.get(url)
data = respond.json()
print(data)