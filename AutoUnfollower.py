import csv
from ensta import Web 

username = "INSET_USERNAME_HERE"
password = "INSET_PASSWORD_HERE"

web = None

try:
    web = Web(username, password)
except Exception as e:
    print("Login failed.")
    print(f"Error details: {e}")
    exit()

followers = web.followers(username)
followings = web.followings(username)

# Fetching next chunk
# followers = mobile.followers(username, next_cursor=followers.next_cursor)

# Convert followers and followings to sets for faster lookup
followers_usernames = set(follower.username for follower in followers)
followings_usernames = set(following.username for following in followings)
non_followers = followings_usernames - followers_usernames

print("Following and Follower lists processed successfully!")
print("What would you like to do with the users who don't follow back?")
print("1: Unfollow them")
print("2: Print their usernames")
print("3: Do nothing")

user_choice = input("Enter your choice (1, 2, or 3): ")

if user_choice == '1':
    # Unfollow users who don't follow back
    for username in non_followers:
        web.unfollow(username)
    print(f"Unfollowed {len(non_followers)} users.")

elif user_choice == '2':
    # Print usernames of users who don't follow back
    print("Users who don't follow back:")
    for username in non_followers:
        print(username)

elif user_choice == '3':
    # Do nothing
    print("No action taken.")

else:
    print("Invalid choice. Exiting.")