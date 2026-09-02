from por_2022_analysis import portland_players_stats

def analyze_playing_time():

    print("----------------------------------- PLAYING TIME ANALYSIS ---------------------------------------")

    # players with the most playing minutes
    top_minutes = portland_players_stats.sort_values("minutes", ascending=False)

    print(top_minutes[["player_name", "player_position", "minutes"]].head(10))

    # players with more appearances and starts
    top_appearances = portland_players_stats.sort_values("appearances", ascending=False)

    print(top_appearances[["player_name", "player_position", "appearances", "starts"]].head(10))

    # players with the most substitute appearances
    top_substitutes = portland_players_stats.sort_values("sub_on", ascending=False)

    print(top_substitutes[["player_name", "player_position", "sub_on"]].head(10))

    # players who were substituted off the most
    sub_off = portland_players_stats.sort_values("sub_off", ascending=False)

    print(sub_off[["player_name", "player_position", "sub_off"]].head(10))