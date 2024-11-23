import csv
import json

def load_players(file_path):
    players = []
    with open(file_path, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            players.append({
                "name": row["name"],
                "gender": row["gender"],
                "level": int(row["level"])
            })
    return players

def save_teams(file_path, week_identifier, teams):
    try:
        with open(file_path, mode="r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    data[week_identifier] = [[player["name"] for player in team] for team in teams]

    with open(file_path, mode="w") as file:
        json.dump(data, file, indent=4)

def load_previous_teams(file_path):
    try:
        with open(file_path, mode="r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}