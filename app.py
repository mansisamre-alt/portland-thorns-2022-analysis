
from por_2022_analysis import portland_players_stats
from defensive_analysis import analyze_defence
from shooting_analysis import analyze_shooting
import streamlit as st

# adding a gui
st.title("Portland Thorns 2022 Player Analysis")

st.write("Welcome to my NWSL player analytics dashboard.")

analysis = st.sidebar.selectbox("choose an analysis:",
                                ["overview", "passing", "defence", "shooting",
                                 "playing time", "Player Profile"])

st.write(f"you selected: {analysis}")

# OVERVIEW SECTION
if analysis == "overview":
    # st.header("Portland Thorns 2022 squad")
    # st.write("Player statistics from 2022 season")
    # st.dataframe(portland_players_stats)

# creating readable data
    total_players = len(portland_players_stats)
    total_goals = portland_players_stats["goals"].sum()
    total_assists = portland_players_stats["assists"].sum()
    total_minutes = portland_players_stats["minutes"].sum()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Players", total_players)
    col2.metric("Goals", total_players)
    col3.metric("Assists", total_assists)
    col4.metric("Minutes", total_minutes)

# bar chart of the top goal scorers
    st.subheader("Top Scorers")

    top_scorers = (portland_players_stats.sort_values("goals", ascending=False).head(10))

    st.bar_chart(top_scorers.set_index("player_name")["goals"])

# top assists chart
    st.subheader("Top Assists")

    top_assists = (portland_players_stats.sort_values("assists", ascending=False).head(10))

    st.bar_chart(top_assists.set_index("player_name")["assists"])

# key stats for the player
    st.subheader("Player Overview")

    selected_player = st.selectbox("select a player", portland_players_stats["player_name"])

    player_data = portland_players_stats[portland_players_stats["player_name"] == selected_player].iloc[0]

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Goals", player_data["goals"])
    col2.metric("Assists", player_data["assists"])
    col3.metric("Minutes", player_data["minutes"])
    col4.metric("Shots", player_data["shots_total"])

# PASSING SECTION
if analysis == "passing":
    st.header("Passing Analysis")

# top passers
    st.subheader("Top Passers")

    top_passers = portland_players_stats.sort_values("successful_passes_total",ascending=False).head(10)

    st.dataframe(top_passers[["player_name", "player_position", "minutes", "successful_passes_total"]])

# pass completion percentage of players with more than 100 passes
    st.subheader("Pass completion")

    regular_passers = portland_players_stats[portland_players_stats["passes_total"]>= 100].copy()

    regular_passers["pass_completion_pct"] = (regular_passers["successful_passes_total"] /
                                              regular_passers["passes_total"] * 100)

    regular_passers = regular_passers.sort_values("pass_completion_pct", ascending=False).head(10)

    st.dataframe(regular_passers[["player_name", "player_position", "passes_total",
                                  "successful_passes_total", "pass_completion_pct"]].head(10))

# pass completion chart
    st.subheader("Pass Completion Comparison")

    chart_data = regular_passers[["player_name", "pass_completion_pct"]].head(10)

    st.bar_chart(chart_data.set_index("player_name"))

# DEFENSIVE SECTION
if analysis == "defence":

    st.header("Defensive Analysis")

    (top_tacklers, regular_tacklers, top_interceptors, top_clearances,
     top_blockers, defensive_summary, defensive_by_position) = analyze_defence()

# top tacklers using defensive_analysis.py
    st.subheader("Top Tacklers")

    st.dataframe(top_tacklers[["player_name", "player_position", "tackles_total", "tackles_won"]].head(10))

# top successful tackles
    st.subheader("Tackle Success")

    st.dataframe(regular_tacklers[["player_name", "player_position", "tackles_total",
                                   "tackles_won", "tackle_success_pct"]].head(10))

# top interceptors
    st.subheader("Top Interceptors")

    st.dataframe(top_interceptors[["player_name", "player_position", "interceptions"]].head(10))

# top clearances
    st.subheader("Top Clearances")

    st.dataframe(top_clearances[["player_name", "player_position", "clearances_total"]].head(10))

# top blocks
    st.subheader("Top Blocks")

    st.dataframe(top_blockers[["player_name", "player_position", "blocks"]].head(10))

# defensive score
    st.subheader("Defensive Score")

    defensive_ranking = defensive_summary.copy()

    defensive_ranking["defensive_score"] = (defensive_ranking["tackles_won"] + defensive_ranking["interceptions"]
                                            + defensive_ranking["clearances_total"] + defensive_ranking["blocks"])

    defensive_ranking = defensive_ranking.sort_values("defensive_score", ascending=False)

    st.dataframe(defensive_ranking[["player_name", "player_position",  "tackles_won", "interceptions",
                                    "clearances_total", "blocks", "defensive_score"]])

    st.subheader("Top Defensive Players")

    chart_data = defensive_ranking[["player_name", "defensive_score"]].head(10)

    st.bar_chart(chart_data.set_index("player_name"))

# SHOOTING ANALYSIS
if analysis == "shooting":
    st.header("Shooting Analysis")

    (top_shooters, regular_shooters, regular_players) = analyze_shooting()

# players with the most shots
    st.subheader("Most Shots")

    st.dataframe(top_shooters[["player_name", "player_position", "shots_total"]].head(10))


# shooting accuracy of the players
    st.subheader("Shot Accuracy")

    st.dataframe(regular_shooters[["player_name", "player_position", "shots_total",
                                   "shots_on_target", "shot_accuracy"]].head(10))

# goals from shots
    st.subheader("Goals From Shots")

    goals_from_shots = regular_shooters.sort_values("goals", ascending=False)

    st.dataframe(goals_from_shots[["player_name", "shots_total", "shots_on_target", "goals"]].head(10))

# shot conversion rate
    st.subheader("Shot Conversion Rate")

    conversion_ranking = regular_shooters.sort_values("shot_conversion_rate", ascending=False)

    st.dataframe(conversion_ranking[["player_name", "shots_total", "goals", "shot_conversion_rate"]].head(10))

# goals per 90 mins
    st.subheader("Goals per 90 minutes")

    goals_per_90 = regular_players.sort_values("goals_per_90", ascending=False)

    st.dataframe(goals_per_90[["player_name", "minutes", "goals", "goals_per_90"]].head(10))

# PLAYING TIME ANALYSIS
if analysis == "playing time":
    st.header("Playing Time Analysis")

# minutes played
    st.subheader("Minutes Played")

    top_minutes = portland_players_stats.sort_values("minutes", ascending=False)

    st.bar_chart(top_minutes.set_index("player_name")["minutes"])

# appearances for games
    st.subheader("Player Appearances")

    top_appearances = portland_players_stats.sort_values("appearances", ascending=False)

    st.dataframe(top_appearances[["player_name", "player_position", "appearances"]].head(10))

# top players substituted in
    st.subheader("Top Substitutions On")

    top_substitutions = portland_players_stats.sort_values("sub_on", ascending=False)

    st.dataframe(top_substitutions[["player_name", "player_position", "sub_on"]].head(10))

# top players substituted out
    st.subheader("Top Substitutions Off")

    top_substitutions_out = portland_players_stats.sort_values("sub_off", ascending=False)

    st.dataframe(top_substitutions[["player_name", "player_position", "sub_off"]].head(10))

# PLAYER PROFILE
if analysis == "Player Profile":
    st.header("Player Profile")

    selected_player = st.selectbox("Select a player", portland_players_stats["player_name"])

    player_data = portland_players_stats[portland_players_stats["player_name"] == selected_player].iloc[0]

    st.title(player_data["player_name"])
    st.caption(f"Position: {player_data['player_position']}")
    st.divider()

    st.subheader("Player Summary")

    st.write(
        f"{player_data['player_name']} made "
        f"{player_data['appearances']} appearances and scored "
        f"{player_data['goals']} goals."
    )
    st.divider()

# data about playing time
    st.subheader("Playing Time")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Minutes Played:", player_data["minutes"])
    col2.metric("Appearances:", player_data["appearances"])
    col3.metric("Starts:", player_data["starts"])
    col4.metric("Substitutions On:", player_data["sub_on"])

    st.metric("Substitutions Off:", player_data["sub_off"])
    st.divider()

# data about attacking statistics
    st.subheader("Attacking Statistics")

    col1, col2, col3, col4, col5, col6 = st.columns(6)

    col1.metric("Goals:", player_data["goals"])
    col2.metric("Shots:", player_data["shots_total"])
    col3.metric("Shots on Target:", player_data["shots_on_target"])
    shot_accuracy = (player_data["shots_on_target"]/ player_data["shots_total"]* 100)
    col4.metric("Shot Accuracy:", f"{shot_accuracy:.1f}%")
    goals_per_90 = (player_data["goals"] / player_data["minutes"] * 90)
    col5.metric("Goals per 90:", f"{goals_per_90:.2f}%")
    shot_conversion_rate = (player_data["goals"] / player_data["shots_total"] * 100)
    col6.metric("Shot Conversion Rate:", f"{shot_conversion_rate:.1f}%")
    st.divider()

# data about passing statistics
    st.subheader("Passing Statistics")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Passes:", player_data["passes_total"])
    col2.metric("Successful Passes:", player_data["successful_passes_total"])
    pass_completion_pct = (player_data["successful_passes_total"] / player_data["passes_total"] * 100)
    col3.metric("Pass Completion Percentage:", f"{pass_completion_pct:.2f}%")
    st.divider()

# data about the defending statistics
    st.subheader("Defensive Statistics")

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric("Tackles Won:", player_data["tackles_won"])
    col2.metric("Interceptions:", player_data["interceptions"])
    col3.metric("Clearances:", player_data["clearances_total"])
    col4.metric("Blocks:", player_data["blocks"])
    defensive_score = (player_data["tackles_won"] + player_data["interceptions"] +
                       player_data["clearances_total"] + player_data["blocks"])
    col5.metric("Defensive Score:", defensive_score)
    st.divider()




