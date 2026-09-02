from por_2022_analysis import portland_players_stats

def analyze_passing():

    print("------------------------------ PASSING ANALYSIS -----------------------------------")

    # successful passes completed
    top_passers = portland_players_stats.sort_values("successful_passes_total", ascending=False)

    print(top_passers[["player_name", "player_position", "minutes", "successful_passes_total"]].head(10))

    # pass completion percentage
    # pass completion % = successful passes ÷ total passes × 100
    print(portland_players_stats[["player_name", "passes_total", "successful_passes_total"]].head(10))

    portland_players_stats["pass_completion_pct"] = (portland_players_stats["successful_passes_total"] /
                                                     portland_players_stats["passes_total"] * 100)

    print(portland_players_stats[["player_name", "passes_total",
                                  "successful_passes_total", "pass_completion_pct"]])

    # players with regular minutes
    regular_passers = portland_players_stats[portland_players_stats["passes_total"] >= 100]

    regular_passers = regular_passers.sort_values("pass_completion_pct", ascending=False)

    print(
        regular_passers[["player_name", "player_position", "passes_total",
                         "successful_passes_total", "pass_completion_pct"]].head(10))

    # completed passes by position (Group the players by position,
    # then calculate the mean pass completion percentage for each position.)
    passing_by_position = regular_passers.groupby("player_position")["pass_completion_pct"].mean()

    print(passing_by_position)