from flask import Flask, render_template, request, redirect, url_for, send_file, jsonify
import json
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from youtubesearchpython import VideosSearch
from pytube import YouTube

app = Flask(__name__)
server = app.server

# Replace with your Spotify Developer credentials
client_id = '27466a21fc434a538a1bc7ca6b59ed47'
client_secret = 'f3e29c9448ce40c9b40ac6a6dfa73380'

# Initialize the Spotipy client
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

def get_playlist_track_info(playlist_uri):
    track_info = []

    results = sp.playlist_tracks(playlist_uri)

    for track in results['items']:
        track_name = track['track']['name']
        artist_name = track['track']['artists'][0]['name']  # Assuming the first artist is sufficient

        track_info.append({'track_name': track_name, 'artist_name': artist_name})

    return track_info

def search_on_yt(track_info):
    video_urls = []
    for info in track_info:
        search_query = f'{info["track_name"]} {info["artist_name"]}'
        videos_search = VideosSearch(search_query, limit=1)
        results = videos_search.result()
        if results['result']:
            video_urls.append(results['result'][0]['link'])

    return video_urls

def convert_youtube_to_mp3(video_urls, output_path):
    for i in video_urls:
        yt = YouTube(i)
        audio_stream = yt.streams.filter(only_audio=True).first()
        audio_stream.download(output_path=output_path)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        playlist_uri = request.form["playlist_uri"]
        output_path = "static/music"

        # Call your existing functions here
        track_info = get_playlist_track_info(playlist_uri)
        video_urls = search_on_yt(track_info)
        convert_youtube_to_mp3(video_urls, output_path)

        second_server()

        return render_template("results.html", track_info=track_info, video_urls=video_urls)

    return render_template("index.html")

@app.route("/player.html")
def serve_player():
    return send_file("player.html")


@app.route("/second_server", methods=["GET"])
def second_server():
    # Add your second server code here
    # Directory where music files and metadata are stored
    music_directory = "static/music"

    # Initialize an empty list to store music data
    music_list = []

    # Loop through files in the music directory
    for filename in os.listdir(music_directory):
        if filename.endswith(".mp4"):
            # Extract metadata from the filename
            music_name = filename.replace(".mp4", "")
            artist = ""

            # Create a dictionary for the music data
            music_data = {
                "img": "static/bg.jpg",
                "name": music_name,
                "artist": artist,
                "music": f"{music_directory}/{filename}",
            }

            # Append the music data to the list
            music_list.append(music_data)

    # Update the JSON file with the new music data
    with open("static/music_list.json", "w") as json_file:
        json.dump(music_list, json_file, indent=4)

    return jsonify({"message": "Second server data updated."})

    

if __name__ == "__main__":
    app.run(debug=True)
