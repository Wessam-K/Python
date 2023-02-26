from pytube import YouTube

# Ask for the YouTube video URL
url = input("Enter the YouTube video URL: ")

# Create a YouTube object with the video URL
video = YouTube(url)

# Get all the available video streams
streams = video.streams.filter(progressive=True)

# Print out the available quality options
for i in range(len(streams)):
    print(f"{i+1}. Resolution: {streams[i].resolution}, Format: {streams[i].mime_type}")

# Ask the user to select a quality option
selection = int(input("Enter the number of the preferred quality option: "))

# Get the stream for the user-selected quality option
stream = streams[selection - 1]

# Download the video to the current directory
stream.download()