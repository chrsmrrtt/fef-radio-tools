import pathlib
import time

import spotipy
import spotipy.oauth2


def connect() -> spotipy.Spotify:
    client_id_path = pathlib.Path("client_id.txt")
    client_id = client_id_path.read_text().strip()
    
    scope = "user-read-currently-playing"

    auth_manager = spotipy.oauth2.SpotifyPKCE(
        client_id=client_id,
        redirect_uri="http://localhost:8080",
        scope=scope,
        open_browser=True,
        cache_path=".spotipyoauthcache",
    )

    spotify = spotipy.Spotify(auth_manager=auth_manager)

    return spotify


def format_milliseconds(ms: int) -> str:
  seconds = int(ms / 1000)
  minutes = int(seconds / 60)
  seconds = seconds % 60
  return f"{minutes:02d}:{seconds:02d}"


def clear_playlist():
    with open("playlist.txt", "w") as file:
        file.write("")


def get_now_playing(spotify: spotipy.Spotify) -> dict | None:
    try:
        now_playing = spotify.current_user_playing_track()
    except:
        return get_now_playing(spotify)

    if now_playing:
        track = now_playing["item"]
        
        return {
            "track_id": track["id"],
            "artists": ", ".join(artist["name"] for artist in track["artists"]),
            "title": track["name"],
            "duration": format_milliseconds(track["duration_ms"]),
            "progress": format_milliseconds(now_playing["progress_ms"]),
        }
    else:
        return None    
    

def update_now_playing(track: dict):
    with open("now_playing.txt", "w") as file:
        file.write(f"{track['artists']} - {track['title']}")


def update_playlist(track: dict):
    with open("playlist.txt", "a") as file:
        file.write(f"{track['artists']} - {track['title']}\n")


def update_progress(track: dict):
    with open("progress.txt", "w") as file:
        file.write(f"{track['progress']} / {track['duration']}")


def run():
    print("FEF Radio Tools is running... Ctrl-C to stop.")
    
    clear_playlist()

    spotify = connect()
    
    now_playing_id = None

    while True:
        now_playing = get_now_playing(spotify)

        if now_playing:
            update_progress(now_playing)

            if now_playing["track_id"] != now_playing_id:
                update_now_playing(now_playing)
                update_playlist(now_playing)
                now_playing_id = now_playing["track_id"]
                click.echo(f"Now playing: {now_playing['artists']} - {now_playing['title']}")

        time.sleep(1)


if __name__ == "__main__":
    run()
