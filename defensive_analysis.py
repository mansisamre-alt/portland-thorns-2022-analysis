from por_2022_analysis import portland_players_stats

def analyze_defence():

    print("----------------------------- DEFENSIVE ANALYSIS ----------------------------------")

    # finding players with the most successful tackles
    top_tacklers = portland_players_stats.sort_values("tackles_won", ascending=False)

    print(top_tacklers[["player_name", "player_position", "tackles_total", "tackles_won"]].head(10))

    #tackle success % = tackles won ÷ tackles total × 100

    portland_players_stats["tackle_success_pct"] = (portland_players_stats["tackles_won"]
                                                    / portland_players_stats["tackles_total"] *100)

    # tackle success rate of players having more than 10 tackles
    regular_tacklers = portland_players_stats[portland_players_stats["tackles_total"] >= 10]

    regular_tacklers = regular_tacklers.sort_values("tackle_success_pct", ascending=False)

    print(regular_tacklers[["player_name", "player_position", "tackles_total",
                            "tackles_won", "tackle_success_pct"]].head(10))

    # finding top interceptors
    top_interceptors = portland_players_stats.sort_values("interceptions", ascending=False)

    print(top_interceptors[["player_name", "player_position", "interceptions"]].head(10))

    # players with most clearances
    top_clearances = portland_players_stats.sort_values("clearances_total", ascending=False)

    print(top_clearances[["player_name", "player_position", "clearances_total"]].head(10))

    # players with most blocks
    top_blockers = portland_players_stats.sort_values("blocks", ascending=False)

    print(top_blockers[["player_name", "player_position", "blocks"]].head(10))

    # defensive summary
    defensive_summary = portland_players_stats[["player_name","player_position","tackles_won",
                                                "interceptions","clearances_total","blocks"]]

    print(defensive_summary)

    portland_players_stats["defensive_score"] = (portland_players_stats["tackles_won"] +
                                                 portland_players_stats["interceptions"] +
                                                 portland_players_stats["clearances_total"] +
                                                 portland_players_stats["blocks"])

    print(portland_players_stats[["player_name", "defensive_score"]])

    # grouping by position
    defensive_by_position = portland_players_stats.groupby("player_position")[["tackles_won", "interceptions",
                                                            "clearances_total", "blocks"]].mean()

    print(defensive_by_position)

    return (
        top_tacklers,
        regular_tacklers,
        top_interceptors,
        top_clearances,
        top_blockers,
        defensive_summary,
        defensive_by_position
    )