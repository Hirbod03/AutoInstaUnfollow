# AutoInstaUnfollow

## Overview

**AutoInstaUnfollow** is a Python script that helps manage your Instagram followings by automatically unfollowing users who don't follow you back. This script utilizes the `ensta` library to interact with the Instagram API and streamline the process of maintaining a more balanced follower-following ratio.

## Features

- Fetches the list of users you follow and your followers.
- Identifies users who don't follow you back.
- Automatically unfollows users who don't follow you back.
- Simple and efficient code, ideal for personal use.

## Requirements

- Python 3.6+
- `ensta` library

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/hirbod03/AutoInstaUnfollow.git
    cd AutoInstaUnfollow
    ```

2. Install the required libraries:

    ```bash
    pip install ensta
    brew install ffmpeg
    ```

## Usage

1. Open the `igtrack.py` script and replace `"USERNAME"` and `"PASSWORD"` with your Instagram username and password.
2. Run the script:

    ```bash
    python igtrack.py
    ```

3. The script will output the progress and automatically unfollow users who don't follow you back.

## Notes

- Use this script responsibly and be aware of Instagram's rate limits and policies.
- Ensure that you have the necessary permissions and comply with Instagram's terms of service.

## Contributing

If you have any ideas, suggestions, or improvements, feel free to open an issue or submit a pull request.


## Acknowledgments

- Thanks to the creators of the `ensta` library for providing a simple way to interact with the Instagram API.
