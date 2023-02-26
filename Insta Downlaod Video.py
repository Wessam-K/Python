import instaloader

# Create an instance of Instaloader class
L = instaloader.Instaloader()

# Obtain the post URL from the user
url = input("Enter the Instagram post URL: ")

# Retrieve the post details
post = instaloader.Post.from_shortcode(L.context, url.split("/")[-2])

# Retrieve the video stream of the post
video_stream = post.get_video_streams()[0]

# Download the video to the current directory
L.download_video(video_stream, filename="instagram_video")