# AutoInstaUnfollow

## Overview

**AutoInstaUnfollow** is a Python script that helps manage your Instagram followings by automatically unfollowing users who don't follow you back. This script utilizes the `Web` class from the Ensta library to interact with the Instagram API and streamline the process of maintaining a more balanced follower-following ratio.

## Features

- Fetches the list of users you follow and your followers.
- Identifies users who don't follow you back.
- Provides options to automatically unfollow users who don't follow you back, print their usernames, or take no action.
- Simple and efficient code, ideal for educational purposes.


## Requirements

- Python 3.6+
- `ensta` library

## Installation

1. Clone this repository

2. Install the required libraries:

    ```bash
    brew install ensta
    ```
    ```bash
    brew install ffmpeg
    ```

- ## Prerequisites

- Ensure you have the appropriate prerequisites for the Ensta library. Refer to the [Ensta library documentation]([#](https://github.com/diezo/Ensta)) for detailed information.
- Turn off two-factor authentication on your Instagram account if not handled by the script.

## Usage

1. Run the script:

    ```bash
    python AutoUnfollower.py
    ```
2. Enter instagram credientials when prompted.
3. The script will output the progress and provide options to unfollow users who don't follow you back, print their usernames, or take no action.

## Cautions

- **Use this script responsibly**: Be aware of Instagram's rate limits and policies regarding automation.
- **Personal Accounts**: Using your personal account with automation scripts can lead to your account being flagged or banned. It is recommended to use a secondary account for testing purposes.
- **Educational Purposes**: This script is intended for educational purposes only. Please comply with Instagram's terms of service and use the script at your own risk.

## Contributing

If you have any ideas, suggestions, or improvements, feel free to open an issue or submit a pull request.

## Acknowledgments

- Thanks to the creators of the Ensta library and its dependencies for providing a way to interact with the Instagram API.
