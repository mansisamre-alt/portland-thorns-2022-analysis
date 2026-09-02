from por_2022_analysis import portland_players_stats

def analyze_shooting():

    print("------------------------------ SHOOTING ANALYSIS ----------------------------------")

    # finding the players with the most shots
    top_shooters = portland_players_stats.sort_values("shots_total", ascending=False)

    print(top_shooters[["player_name", "player_position", "shots_total"]].head(10))

    # shots on target
    print(portland_players_stats[["player_name", "shots_total", "shots_on_target"]])

    # shot accuracy
    portland_players_stats["shot_accuracy"] = (portland_players_stats["shots_on_target"] /
                                               portland_players_stats["shots_total"] * 100)

    print(portland_players_stats[["player_name", "shots_total", "shots_on_target", "shot_accuracy"]])

    # shooting analysis of players who took more than 10 shots
    regular_shooters = portland_players_stats[portland_players_stats["shots_total"] > 10]

    regular_shooters = regular_shooters.sort_values("shot_accuracy", ascending=False)

    print(regular_shooters[["player_name", "shots_total", "shots_on_target", "shot_accuracy"]].head(10))

    # shots converted into goals
    print(regular_shooters[["player_name", "shots_total", "shots_on_target",
                            "goals"]].sort_values("goals", ascending=False).head(10))

    # goal conversion rate
    # goals / shots * 100
    portland_players_stats["shot_conversion_rate"] = (portland_players_stats["goals"] /
                                                      portland_players_stats["shots_total"] * 100)

    # goal conversion of players with minimum 10 shots
    regular_shooters = portland_players_stats[portland_players_stats["shots_total"] > 10]

    regular_shooters = regular_shooters.sort_values("shot_conversion_rate", ascending=False)

    print(regular_shooters[["player_name", "shots_total", "goals", "shot_conversion_rate"]].head(10))

    # goals per 90 mins
    # goals ÷ minutes × 90
    portland_players_stats["goals_per_90"] = (portland_players_stats["goals"] /
                                              portland_players_stats["minutes"] * 90)

    # players with at least 500 mins
    regular_players = portland_players_stats[portland_players_stats["minutes"] > 500]

    regular_players = regular_players.sort_values("goals_per_90", ascending=False)

    print(regular_players[["player_name", "minutes", "goals", "goals_per_90"]].head(10))

    return (
        top_shooters,
        regular_shooters,
        regular_players
    )



