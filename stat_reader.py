from pybaseball import batting_stats

def get_player_stats(name, year):
    
    stats = batting_stats(year, qual=50) #50 PA minimum
    stats_filtered = stats[["Name", "OBP", "SLG", "K%", "wRC+", "RBI", "PA"]]

    player_row = stats_filtered[stats_filtered["Name"].str.lower() == name.lower()]
    if player_row.empty:
        return None
    player_stats = player_row.iloc[0].to_dict()
    player_stats["RBI/PA"] = player_stats["RBI"]/player_stats["PA"]
    player_stats["K%"] = -player_stats["K%"]
    del player_stats["RBI"]
    del player_stats["PA"]
    return player_stats