import csv
from ensta import Mobile 

mobile = Mobile("USERNAME", "PASSWORD")

followers = mobile.followers("USERNAME")
followings = mobile.followings("USERNAME")

# Fetching next chunk
followers = mobile.followers("USERNAME", next_cursor=followers.next_cursor)

# Convert followers and followings to sets for faster lookup
followers_usernames = set(follower.username for follower in followers.list)
followings_usernames = set(following.username for following in followings.list)
non_followers = followings_usernames - followers_usernames

print("Following and Follower lists processed successfully!")
# Ask the user what they want to do with the result
print("What would you like to do with the users who don't follow back?")
print("1: Unfollow them")
print("2: Print their usernames")
print("3: Do nothing")
user_choice = input("Enter your choice (1, 2, or 3): ")

if user_choice == '1':
    # Unfollow users who don't follow back
    for username in non_followers:
        mobile.unfollow(username)
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