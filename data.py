import nwslpy

players = nwslpy.load_players()

#get hold of first 5 rows
print(players.head())

#get hold of columns in a data frame
print(players.columns)

#creating a new column
players["player_name"] = players["player_first_name"] + " " + players["player_last_name"]

#printing column player_name
print(players["player_name"].head())

#seeing different player positions
print(players["player_position"].unique())

#counting players in each positions
print(players["player_position"].value_counts())

#getting hold of midfielders and printing player_names of midfielders
midfielders = players[players["player_position"] == "Midfielder"]
print(midfielders)
print(midfielders["player_name"])

#     print(midfielders["player_name"])
#           ~~~~~~~~~~~^^^^^^^^^^^^^^^
# TypeError: list indices must be integers or slices, not str
#check df[df[""]]


#sort players alphabetically
sorted_players = players.sort_values("player_name")
print(sorted_players.head(10))

#names/functions/objects are available inside this package
print(dir(nwslpy))
help(nwslpy.load_player_season_stats)

teams = nwslpy.load_teams()

#get hold of columns in a data frame
print(teams.head())
print(teams.columns)

#finding specific teams
gotham = teams[teams["team_name"] == "NJ/NY Gotham FC"]
print(gotham)
print(gotham.index)

# loading data about the team
gotham_id = "NJY"
season = "2023"
gotham_stats = nwslpy.load_player_season_stats(gotham_id, season)
print(gotham_stats.head())
print(gotham_stats.columns)

for column in gotham_stats.columns:
    print(column)


