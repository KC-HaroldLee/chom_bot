from flask import Flask
import pytube
import os

app = Flask(__name__)

@app.route('/download')
def hello_world():
    print("download")

    yt_url = "https://www.youtube.com/watch?v=52ApW6NIjRA"
    source = pytube.YouTube(yt_url)
    source.streams.filter(only_audio=True).first().download("./music/", filename=f"s.mp4")
    print("성공")

    return "오케"

if __name__ == '__main__':
    app.run()