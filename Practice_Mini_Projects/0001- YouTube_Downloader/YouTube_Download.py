import yt_dlp as yt

url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ' # input URL

quality = {
    'format': 'best',  # Set best quality
}

with yt.YoutubeDL(quality) as media:
    media.download([url])  # Downloads the video
