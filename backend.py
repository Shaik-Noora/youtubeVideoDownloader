from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins, change to specific domains if needed
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods, change to specific methods if needed
    allow_headers=["*"],  # Allows all headers
)

import os 
import yt_dlp 

cur_dir=os.getcwd()

@app.post('/download')
def download_video(link: str = Form(...)):
    youtube_dl_options = {
        'format': 'best',
        'outtmpl': os.path.join(cur_dir, "ABCsample.mp4")
    }
    with yt_dlp.YoutubeDL(youtube_dl_options) as ydl:
        ydl.download([link])
    return {"status": "Download complete"}


