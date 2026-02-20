# Made by Luboš Kulhan | alias: Adam Kaiser

import random as r
def random_choice(x):
    try:
        pure_list = []
        i = 0
        while i < len(x): # Loop to get rid of empty strings
            if x[i] != "":
                pure_list.append(x[i]) # Adds string to new list
            i += 1
        list_random = r.choice(pure_list) # Chooses random string from list
        return list_random
    except TypeError:
        print("ERROR - make sure input is a list")

# Test - uncomment for test
#my_list = ["Tempus", "Lux", "Morr", "Solis", "Gaia",""]
#print(random_choice(my_list))