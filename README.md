# Spotify Ads Free

Spotify Ads Free is a Python web application that allows users to convert Spotify playlist tracks into MP3 format and play them without ads. It uses the Spotify API to fetch track information from a playlist, searches for corresponding tracks on YouTube, downloads them as MP3 files, and provides a simple web-based music player for playing the converted tracks.

## Features

- Convert Spotify playlist tracks to MP3 format.
- Play the converted tracks using a web-based music player.
- Random play mode for added variety.
- Repeat track option for listening to your favorite songs repeatedly.
- Seek slider for tracking progress.
- Volume control slider.
- Automatic update of track information.

## Installation
   1) git clone the reposoitories
   2) Install the required Python packages:
   3) Copy code
   4) pip install -r requirements.txt
   5) Create a Spotify Developer application and obtain your client ID and client secret. Replace the client_id and client_secret variables in app.py with your credentials.

## To Start the application:

  1) Type python app.py in the terminal
  2) Open a web browser and visit http://localhost:5000 to access the application.

## Usage
1) Enter the URL of a Spotify playlist in the provided input field and click the "Convert" button.
2) The application will convert the tracks and display the results, including links to the converted tracks on YouTube.
3) Click the "Open Music Player" button to launch the music player.
4) Use the player controls to play, pause, skip, and repeat tracks.

## Acknowledgments
- This project was created using the Flask web framework and various Python libraries.
- It relies on the Spotify API for fetching playlist information and the YouTube Data API for searching for tracks.
- The web player is built with HTML, CSS, and JavaScript.
- Special thanks to the Spotify and YouTube communities for their support and inspiration.

Enjoy your Spotify playlist without ads!


