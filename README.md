# FEF Radio Tools

This script connects to Spotify and retrieves the currently playing track, updating local files with the track information and progress.

## Prerequisites

- Python >= 3.10
- `spotipy` library

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/chrsmrrtt/fef-radio-tools.git
    cd fef-radio-tools
    ```

2. Install the required Python packages:
    ```sh
    pip install spotipy
    ```

3. Create a file named `client_id.txt` in the same directory as the script and paste your Spotify client ID into it.

## Usage

Run the script:
```sh
python fefradio.py
```

The script will:
- Connect to Spotify using your client ID.
  - On first run you will be required to authorise the script to have access to your currently playing track on Spotify.
- Retrieve the currently playing track.
- Update `now_playing.txt` with the current track's artist and title.
- Update `playlist.txt` with a log of all tracks played.
- Update `progress.txt` with the current track's progress and duration.

## Files

- `client_id.txt`: Contains your Spotify client ID.
- `now_playing.txt`: Updated with the current track's artist and title.
- `playlist.txt`: Logs all tracks played with timestamps.
- `progress.txt`: Shows the current track's progress and duration.

## License

This project is licensed under the MIT License.
