from algorithms import hitter_value
from stat_reader import get_player_stats


def main():
    print("Welcome!!! Please choose an option \n1. Observe a single hitter's stats \n2. Compare multiple hitter's stats \n(more to come in future)")
    choice = input("Choose an option: ")
    if choice == "1":
        print(single_hitter())
    if choice == "2":
        comparison()



def single_hitter():
    player_name = input("Type a players name: ")
    player_year = int(input("Type a year: "))

    stats = get_player_stats(player_name, player_year)
    if stats is None:
        print(f"No stats found for {player_name}.")
        return single_hitter()
    value = hitter_value(stats)
    return f"{player_name} has a player value of {value}"

def comparison():
    comps = []

    while True:
        comps.append(single_hitter())
        print("1. Add another player \n2. Finalize and compare")
        cont = input("Choose an option: ")
        if cont == "2":
            break

    for item in comps:
        print(item)

main()