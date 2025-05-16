from algorithms import hitter_value
from stat_reader import get_player_stats


def main():
    print("Welcome!!! Please choose an option \n1. Observe a single hitter's stats \n2. Observe a single hitter's stats over time. \n3. Compare multiple hitter's stats \n(more to come in future)")
    choice = input("Choose an option: ")
    if choice == "1":
        player_name = input("Type a players name: ")
        player_year = int(input("Type a year: "))  
        name, value = single_hitter(player_name, player_year)
        if name == None:
            print(f"{player_name} has no stats in {player_year}")
        else:
            print(f"{name} has a hitter value of {value}")
    if choice == "2":
        player_name = input("Type a players name: ")
        begin = int(input("Type a year to begin: "))
        end = int(input("Type the last year you want to include: "))
        over_time = sh_over_time(player_name, begin, end)
        if over_time == None:
            print(f"No stats found for {player_name} in 1 or more years of the given interval.")
        for item in over_time:
            print(f"In {item[0]}, {item[1]} had a hitter value of {item[2]}")
    if choice == "3":
        comps = comparison()
        for item in comps:
            print(f"{item[0]} has a hitter value of {item[1]}")



def single_hitter(player_name, player_year):

    stats = get_player_stats(player_name, player_year)
    if stats is None:
        return None, None
    value = hitter_value(stats)
    return player_name, value

def comparison():
    comps = []

    while True:
        temp_name, temp_value = single_hitter(input("Type a players name: "), int(input("Type a year: ")))
        if temp_name == None:
            print(f"No stats found for {temp_name}")
            continue
        else:
            comps.append(temp_name, temp_value)
        print("1. Add another player \n2. Finalize and compare")
        cont = input("Choose an option: ")
        if cont == "2":
            break

    return comps

def sh_over_time(player_name, begin_year, end_year):
    res = []
    for i in range(begin_year, end_year + 1):
        temp_name, temp_value = single_hitter(player_name, i)
        if temp_name == None:
            return None
        res.append([i, temp_name, temp_value])
    return res

main()