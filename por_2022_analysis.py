import nwslpy
import pandas as pd
from data import players

# contains team data and also analysis of the goals scored

print("------------------------------------ START OF THE PROJECT ----------------------------------------")
#looking for Portland Thorns team stats
team = "POR"
season = "2022"
portland_stats = nwslpy.load_player_season_stats(team, season)

print(portland_stats.head())
print(portland_stats.columns)
print(portland_stats[["player_id", "goals"]])

#looking for players at particular index
print(players[players.index == 496])
print(portland_stats["player_id"].head())
print(players.index[:5])

#resetting index into column player_id
player_info = players.reset_index()

#merging portland_stats with players
portland_players_stats = portland_stats.merge(player_info, on="player_id")
print(portland_players_stats[["player_id", "player_name", "goals"]])

#finding out top scorers for Portland Thorns
top_scorers = portland_players_stats.sort_values("goals", ascending=False)
print(top_scorers[["player_name", "goals"]].head())

#finding out most impactful attacking players for Portland Thorns
print(portland_players_stats[["player_name", "goals", "assists"]])

#creating new column from existing column(goal_contributions)
portland_players_stats["goal_contributions"] = (
        portland_players_stats["goals"] + portland_players_stats["assists"])

print(portland_players_stats[["player_name", "goals", "assists", "goal_contributions"]])

#    raise KeyError(key) from err
# KeyError: ('player_name', 'goals', 'assists', 'goal_contributions')
#check [] brackets

#checking top goal contributions
top_contributors = portland_players_stats.sort_values("goal_contributions",ascending=False)

print(
    top_contributors[["player_name", "goals", "assists", "goal_contributions"]].head(10))

#minutes played by top contributors
print(top_contributors[["player_name", "minutes", "goals", "assists", "goal_contributions"]].head(10))

#contributions per 90 mins
#goal contributions per 90 = goal contributions ÷ minutes × 90
portland_players_stats["contributions_per_90"] = (portland_players_stats["goal_contributions"]
                                                  / portland_players_stats["minutes"] * 90)

per_90 = portland_players_stats.sort_values("contributions_per_90", ascending=False)

print(per_90[["player_name", "minutes", "goals", "assists",
              "goal_contributions", "contributions_per_90"]].head(10))

#players with regular playing minutes
regular_players = portland_players_stats[portland_players_stats["minutes"] >= 500]

regular_players["contributions_per_90"] = (portland_players_stats["goal_contributions"]
                                           / portland_players_stats["minutes"] * 90)

regular_players = regular_players.sort_values("contributions_per_90", ascending=False)

print(regular_players[["player_name", "minutes", "goals", "assists",
                       "goal_contributions", "contributions_per_90"]].head(10))

# 5 goal players
five_goal_players = portland_players_stats[portland_players_stats["goals"] >= 5]

print(five_goal_players[["player_name", "minutes", "goals", "assists"]])

#players with 3 goals and 3 assists
creative_attackers = portland_players_stats[(portland_players_stats["goals"] >= 3)
                                            & (portland_players_stats["assists"] >= 3)]
print(creative_attackers[["player_name", "minutes", "goals", "assists"]].head(5))

#players with high contributions ( | is or operator)
high_contributors = portland_players_stats[(portland_players_stats["goals"] >= 10) |
                                           (portland_players_stats["assists"] >= 5)]
print(high_contributors[["player_name", "minutes", "goals", "assists"]].head(5))


#checking the info exists
print(player_info[["player_id", "player_name", "player_position"]].head())

# merge player_position with portland_stats
# portland_players_stats = portland_players_stats.merge(player_info[["player_id", "player_position"]],
#                                                       on="player_id",how="left")
#
# print(portland_players_stats[["player_name", "player_position", "goals", "assists"]].head(10))
print(portland_players_stats.columns)
#player_position already exists within portland_player_stats

print(portland_players_stats[["player_name", "player_position", "goals", "assists"]].head(10))

# number of players at each position
print(portland_players_stats["player_position"].value_counts())

# goals by each position
goals_by_position = portland_players_stats.groupby("player_position")["goals"].sum()
print(goals_by_position)

#goals per player
goals_by_position = portland_players_stats.groupby("player_position")["goals"].agg(["sum", "count"])
print(goals_by_position)

# adding an average column
goals_by_position["average_goals"] = (goals_by_position["sum"] / goals_by_position["count"])
print(goals_by_position)