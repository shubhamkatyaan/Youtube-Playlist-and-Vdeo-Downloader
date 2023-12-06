import os
from pytube import Playlist, YouTube

def download_playlist(playlist_url):
    try:
        # Create Playlist object
        playlist = Playlist(playlist_url)
        
        # Get the videos in the playlist
        videos = playlist.video_urls
        
        # Get the current working directory
        current_directory = os.getcwd()
        
        # Create the download directory
        download_directory = os.path.join(current_directory, "downloads")
        
        # Create the download directory if it doesn't exist
        if not os.path.exists(download_directory):
            os.makedirs(download_directory)

        # Download each video in 720p resolution
        for video_url in videos:
            yt = YouTube(video_url)
            
            # Filter streams for 720p resolution
            video = yt.streams.filter(res="720p").first()
            
            if video:
                print(f"Downloading 720p video: {yt.title}")
                # Download the video to the specified directory
                video.download(output_path=download_directory)
            else:
                print(f"No 720p stream available for: {yt.title}")

        print("Download complete!")

    except Exception as e:
        print(f"Error: {e}")

# Main function
if __name__ == "__main__":
    # Get the YouTube Playlist URL from the user
    playlist_url = input("Enter YouTube Playlist URL: ")
    
    # Call the download_playlist function with the provided URL
    download_playlist(playlist_url)

