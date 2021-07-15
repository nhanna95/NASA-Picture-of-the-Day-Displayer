import requests
import json
import urllib.request
from PIL import Image

raw_response = requests.get(f'https://api.nasa.gov/planetary/apod?api_key=6ZbAOVVP4E5zhVRFZipWUJx6M0pR6AahfZqHmdhR').text
response = json.loads(raw_response)
explanation = response['explanation']
hdurl = response['hdurl']

urllib.request.urlretrieve(hdurl,"apod.png")
img = Image.open("apod.png")
img.show()
print(explanation)