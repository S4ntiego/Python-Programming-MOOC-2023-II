import json


def read_data(file_name):
    with open(file_name) as file:
        data = json.load(file)
    return data


def search_player(data, name):
    for player in data:
        if player["name"] == name:
            return player
    return None


def list_team_abbreviations(data):
    abbreviations = set()
    for player in data:
        abbreviations.add(player["team"])
    return sorted(abbreviations)


def list_country_abbreviations(data):
    abbreviations = set()
    for player in data:
        abbreviations.add(player["nationality"])
    return sorted(abbreviations)


def list_players_in_team(data, team):
    players = []
    for player in data:
        if player["team"] == team:
            players.append(player)
    return sorted(players, key=lambda p: p["goals"] + p["assists"], reverse=True)


def list_players_from_country(data, country):
    players = []
    for player in data:
        if player["nationality"] == country:
            players.append(player)
    return sorted(players, key=lambda p: p["goals"] + p["assists"], reverse=True)


def list_top_players_by_points(data, n):
    sorted_players = sorted(
        data, key=lambda p: (p["goals"] + p["assists"], p["goals"]), reverse=True
    )
    return sorted_players[:n]


def list_top_players_by_goals(data, n):
    sorted_players = sorted(data, key=lambda x: (x["goals"], -x["games"]), reverse=True)
    return sorted_players[:n]


def print_player(player):
    name = player["name"]
    team = player["team"]
    goals = player["goals"]
    assists = player["assists"]
    points = goals + assists

    print(f"{name:21s}{team:5s}{goals:2d} + {assists:2d} = {points:3d}")


def execute():
    file_name = input("file name: ")
    data = read_data(file_name)
    print(f"read the data of {len(data)} players")
    print("commands:")
    print("0 quit")
    print("1 search for player")
    print("2 teams")
    print("3 countries")
    print("4 players in team")
    print("5 players from country")
    print("6 most points")
    print("7 most goals")

    while True:
        command = input("command: ")

        if command == "0":
            break

        elif command == "1":
            name = input("name: ")
            player = search_player(data, name)
            if player:
                print_player(player)
            else:
                print("Player not found.")
            print()

        elif command == "2":
            abbreviations = list_team_abbreviations(data)
            for abbreviation in abbreviations:
                print(abbreviation)
            print()

        elif command == "3":
            abbreviations = list_country_abbreviations(data)
            for abbreviation in abbreviations:
                print(abbreviation)
            print()

        elif command == "4":
            team = input("team: ")
            players = list_players_in_team(data, team)
            for player in players:
                print_player(player)
            print()

        elif command == "5":
            country = input("country: ")
            players = list_players_from_country(data, country)
            for player in players:
                print_player(player)
            print()

        elif command == "6":
            n = int(input("how many: "))
            players = list_top_players_by_points(data, n)
            for player in players:
                print_player(player)

        elif command == "7":
            n = int(input("how many: "))
            players = list_top_players_by_goals(data, n)
            for player in players:
                print_player(player)

        else:
            print("Invalid command. Please try again.")


execute()
