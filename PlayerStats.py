import requests
import json


class PlayerStats:
    @staticmethod
    def get_points_per_game(player_name, season):
        player_id = PlayerStats.get_player_id(player_name)
        if not player_id:
            return None

        url = f"https://www.balldontlie.io/api/v1/season_averages?player_ids[]={player_id}&season={season}"

        response = requests.get(url)
        response.raise_for_status()  # Check for errors in the response
        data = json.loads(response.text)["data"]

        if not data:
            return None

        ppg = data[0]["pts"]
        return ppg


    @staticmethod
    def get_player_id(player_name):
        url = f"https://www.balldontlie.io/api/v1/players?search={player_name}"
        response = requests.get(url)
        response.raise_for_status()  # Check for errors in the response
        data = json.loads(response.text)["data"]

        if not data:
            return None

        player_id = data[0]["id"]
        return player_id


player_name = "LeBron James"
season = "2019"
ppg = PlayerStats.get_points_per_game(player_name, season=season)
if ppg is not None:
    print(f"{player_name} had an average of {ppg:.1f} points per game in the {season} season.")
else:
    print(f"{player_name} did not play in the 2022 season or could not be found.")
