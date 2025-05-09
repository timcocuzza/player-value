from algorithms import hitter_value
from stat_reader import get_player_stats


def main():
    print("Welcome!!! Please choose an option \n 1. Observe a single hitter's stats \n (more to come in future)")
    choice = input("Choose an option: ")
    if choice == "1":
        single_hitter()



def single_hitter():
    player_name = input("Type a players name: ")
    player_year = int(input("Type a year: "))

    stats = get_player_stats(player_name, player_year)
    print(stats)
    if stats is None:
        print(f"No stats found for {player_name}.")
        return single_hitter()
    value = hitter_value(stats)
    print(f"{player_name} has a player value of {value}")

main()