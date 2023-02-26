from pytube import YouTube

# Ask for the YouTube video URL
url = input("Enter the YouTube video URL: ")

# Create a YouTube object with the video URL
video = YouTube(url)

# Ask the user whether to download video or audio
choice = input("Do you want to download the video or the audio? Enter V for video, A for audio: ")

# Get the streams for the selected option
if choice.lower() == 'v':
    # Get all the available video streams
    streams = video.streams.filter(progressive=True)
    # Print out the available quality options
    for i in range(len(streams)):
        print(f"{i+1}. Resolution: {streams[i].resolution}, Format: {streams[i].mime_type}")
else:
    # Get all the available audio streams
    streams = video.streams.filter(only_audio=True)
    # Print out the available quality options
    for i in range(len(streams)):
        print(f"{i+1}. Bitrate: {streams[i].abr}, Format: {streams[i].mime_type}")

# Ask the user to select a quality option
selection = int(input("Enter the number of the preferred option: "))

# Get the stream for the user-selected quality option
stream = streams[selection - 1]

# Ask the user for the file name to save the stream as
filename = input("Enter the file name to save the stream as (without extension): ")

# Download the stream to the current directory with the user-specified file name
stream.download(output_path='.', filename_prefix='Wessam_', filename=filename)
