import numpy as np
import cases as test

means_hitters = {

    "obp": .330,
    "slg": np.log(.437), #adjust for accuracy
    "k%": -.24,
    "wrc+": 100,
    "risp": .242

}


sd_hitters = {

    "obp": 0.035,
    "slg": 0.0995, #min/max considered .995 of area, z-scores found *this is for ln model
    "k%": .04,
    "wrc+": 25, #for future, this figure could be improved. not normally distributed
    "risp": 0.032

}


weights_hitters = { #sum to length of dict

    "obp": 1.4,
    "slg": 1,
    "k%": .4,
    "wrc+": .8,
    "risp": .6

}


perfect_player_modifier = 3.3 #adjusts what deviation per criteria would be a perfect player
perfect_player_modifier = perfect_player_modifier * (sum(weights_hitters.values()) / len(weights_hitters)) #generalizes so weights are proportional




def weigh_hitter_stats(hitter_stats):

    if "slg" in hitter_stats: #modify passed data to fit adj slg model
        hitter_stats["slg"] = np.log(hitter_stats["slg"])

    return {key: ((hitter_stats[key] - means_hitters[key]) / sd_hitters[key]) * weights_hitters[key] for key in hitter_stats if key in means_hitters and key in sd_hitters}

    
def hitter_value(hitter_stats):
    hv = 0

    mult = 50 / (len(hitter_stats) * perfect_player_modifier)

    tester = weigh_hitter_stats(hitter_stats)
    print(tester)

    for x in tester.values():
        hv += x
    return hv * mult + 50



print(hitter_value(test.bonds_2001))
print(hitter_value(test.judge_2024))
print(hitter_value(test.santander_2024))
print(hitter_value(test.mean_case))
print(hitter_value(test.mantle_1957))