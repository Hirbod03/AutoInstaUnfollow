import csv
from ensta import Web 

# Your Instagram username
loginUsername = input("Enter login username: ") 
# Your Instagram password
password = input("Enter password: ")
# Username of the account whose followers and followings you want to check
username = input("Enter the username of the account you want to check: ")

web = None

# Login to Instagram
try:
    web = Web(loginUsername, password)
except Exception as e:
    print("Login failed.")
    print(f"Error details: {e}")
    exit()

# Get followers and followings of the specified account
followers = web.followers(username)
followings = web.followings(username)

# Convert followers and followings to sets for faster lookup
followers_usernames = set(follower.username for follower in followers)
followings_usernames = set(following.username for following in followings)
non_followers = followings_usernames - followers_usernames

# Print the number of users who don't follow back
print("Following and Follower lists processed successfully!")
print("What would you like to do with the users who don't follow back?")
print("1: Unfollow them")
print("2: Print their usernames")
print("3: Do nothing")

# Ask the user for their choice
user_choice = input("Enter your choice (1, 2, or 3): ")
if user_choice == '1':
    # Unfollow users who don't follow back
    for user in non_followers:
        web.unfollow(user)
    print(f"Unfollowed {len(non_followers)} users.")
elif user_choice == '2':
    # Print usernames of users who don't follow back
    print("Users who don't follow back:")
    for user in non_followers:
        print(user.username)
elif user_choice == '3':
    # Do nothing
    print("No action taken.")
else:
    print("Invalid choice. Exiting.")