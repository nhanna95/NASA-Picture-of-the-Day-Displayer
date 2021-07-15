import requests
import json
import urllib.request
import shutil
from PIL import Image

#funcionality 3
def main(img_date):
    if img_date == "":
        raw_response = requests.get(f'https://api.nasa.gov/planetary/apod?api_key=6ZbAOVVP4E5zhVRFZipWUJx6M0pR6AahfZqHmdhR').text
    else:
        raw_response = requests.get(f'https://api.nasa.gov/planetary/apod?api_key=6ZbAOVVP4E5zhVRFZipWUJx6M0pR6AahfZqHmdhR&date={img_date}').text  
    
    response = json.loads(raw_response)
    print(response)
    explanation = response['explanation']
    hdurl = response['hdurl']

    urllib.request.urlretrieve(hdurl,"apod.png")
    img = Image.open("apod.png")
    img.show()
    print(explanation)

    #functionality 2
    r = requests.get(hdurl, stream=True)
    file = hdurl.split("/")[-1]
    if r.status_code == 200:
        r.raw.decode_content = True

        with open(file, 'wb') as f:
            shutil.copyfileobj(r.raw, f)
