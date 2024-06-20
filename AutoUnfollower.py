import csv
from ensta import Mobile 

momobile = Mobile("USERNAME", "PASSWORD")

followers = mobile.followers("USERNAME")
followings = mobile.followings("USERNAME")

# Fetching next chunk
followers = mobile.followers("USERNAME", next_cursor=followers.next_cursor)

# Convert followers and followings to sets for faster lookup
followers_usernames = set(follower.username for follower in followers.list)
followings_usernames = set(following.username for following in followings.list)

print("Following and Follower lists processed successfully!")

# Unfollow users who don't follow back
for username in followings_usernames:
    if username not in followers_usernames:
        mobile.unfollow(username)