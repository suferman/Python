# Download ffmpeg for format conversion (https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-full.7z).
# Go to C:\ and add folder "ffmpeg" 
# Extract all to C:\ffmpeg. Copy path "C:\ffmpeg\ffmpeg-7.1-full_build\bin"
# Go to "My Computer" or "This PC" and right-click on the drive (from the left-pane)
# Search for and click on "Edit environment variables" > "Environment Variables"
# Click on "Path" > "Edit" > "New" > Paste path "C:\ffmpeg\ffmpeg-7.1-full_build\bin" > "OK" > "OK" > "OK"
# open cmd and enter "ffmpeg". If not recognized, restart
# Download and use VLC

import yt_dlp as yt

def download_video(url, download_path):
    # Define quality format
    quality = {
        'format': 'bestvideo+bestaudio',  # Choose the best format that includes both video and audio
        'merge_output_format': 'mp4',  # output format
        'outtmpl': download_path + r'\%(title)s.%(ext)s',   # Set title and format of file
        }

    # Use yt-dlp to download the video
    with yt.YoutubeDL(quality) as ydl:
        ydl.download([url])

# Call the download function
download_video('https://www.youtube.com/watch?v=dQw4w9WgXcQ', r'C:\Users\ferdg\OneDrive\Desktop\PYTHON_PROJECTS\Project_0001 - YouTube Video Downloader')
