import youtube_dl

def download_video(url):
    # Set download options
    options = {
        'format': 'bestvideo+bestaudio/best',  # Choose the best video and audio quality available
        'outtmpl': '%(title)s.%(ext)s',        # Output file name format
    }

    # Create a YoutubeDL object with the specified options
    with youtube_dl.YoutubeDL(options) as ydl:
        # Download the video with the given URL
        ydl.download([url])

# Main function
if __name__ == "__main__":
    # Get the video URL from the user
    video_url = input("Enter the video URL: ")
    
    # Call the download_video function with the provided URL
    download_video(video_url)