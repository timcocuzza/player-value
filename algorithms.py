import numpy as np
import cases as test

means_hitters = {

    "OBP": .330,
    "SLG": np.log(.437), #adjust for accuracy
    "K%": -.24,
    "wRC+": 100,
    "RBI/PA": .13

}


sd_hitters = {

    "OBP": 0.035,
    "SLG": 0.0995, #min/max considered .995 of area, z-scores found *this is for ln model
    "K%": .04,
    "wRC+": 25, #for future, this figure could be improved. not normally distributed
    "RBI/PA": 0.03

}


weights_hitters = { #sum to length of dict

    "OBP": 1.4,
    "SLG": 1,
    "K%": .4,
    "wRC+": .8,
    "RBI/PA": .6

}


perfect_player_modifier = 3.3 #adjusts what deviation per criteria would be a perfect player
perfect_player_modifier = perfect_player_modifier * (sum(weights_hitters.values()) / len(weights_hitters)) #generalizes so weights are proportional




def weigh_hitter_stats(hitter_stats):

    if "SLG" in hitter_stats: #modify passed data to fit adj slg model
        hitter_stats["SLG"] = np.log(hitter_stats["SLG"])

    return {key: ((hitter_stats[key] - means_hitters[key]) / sd_hitters[key]) * weights_hitters[key] for key in hitter_stats if key in means_hitters and key in sd_hitters}

    
def hitter_value(hitter_stats):
    hv = 0

    weighted = weigh_hitter_stats(hitter_stats)

    mult = 50 / (len(weighted) * perfect_player_modifier)

    for x in weighted.values():
        hv += x
    return hv * mult + 50

