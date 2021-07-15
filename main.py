import requests
import json
import urllib.request
import shutil
from tkinter import *
from PIL import ImageTk, Image

#funcionality 1
def main():
    global hdurl
    img_date = date_input.get()
    if img_date == "":
        raw_response = requests.get(f'https://api.nasa.gov/planetary/apod?api_key=6ZbAOVVP4E5zhVRFZipWUJx6M0pR6AahfZqHmdhR').text
    else:
        #functionality 3
        raw_response = requests.get(f'https://api.nasa.gov/planetary/apod?api_key=6ZbAOVVP4E5zhVRFZipWUJx6M0pR6AahfZqHmdhR&date={img_date}').text  

    response = json.loads(raw_response)
    explanation = response['explanation']
    explanation_text.delete(1.0, "end")
    explanation_text.insert(1.0, explanation)
    title = response['title']
    title_text.delete(1.0, "end")
    title_text.insert(1.0, title)
    hdurl = response['hdurl']
    print(hdurl)
    urllib.request.urlretrieve(hdurl,"apod.png")
    img = Image.open("apod.png")
    resized_img = img.resize((300,300))
    photo = ImageTk.PhotoImage(resized_img)
    picture = Label(window, image=photo)
    picture.image = photo
    picture.place(x=300,y=80)


#functionality 2
def download():
    global hdurl
    r = requests.get(hdurl, stream=True)
    file = hdurl.split("/")[-1]
    if r.status_code == 200:
        r.raw.decode_content = True
        with open(file, 'wb') as f:
            shutil.copyfileobj(r.raw, f)


window = Tk()
window.configure(background='white')
window.title('NASA Astronomy Picture of the Day')
window.geometry("1000x500")

date_input = Entry(window)
date_input.place(x=10,y=20)
date_input.configure(background='light grey')

enter_btn = Button(window, text="Enter", command=main)
enter_btn.place(x=140,y=16)

title_text = Text(window,height=1,width=35,font=("Helvetica", 18))
title_text.place(x=300,y=20)

explanation_text = Text(window, height = 22, width=35,font=("Helvetica", 12))
explanation_text.place(x=650,y=80)


download_btn = Button(window, text="Download", command=download)
download_btn.place(x=425,y=400)








window.mainloop()