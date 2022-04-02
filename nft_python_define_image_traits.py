## Main Snippet 2

# Each image is made up a series of traits
# The weitages for each trait distribute the rarity and add up to 100%

background = ["Blue", "Green", "Red", "Yellow"] 
background_weights = [40, 30, 20, 10]

rice = ["White", "Blue", "Yellow"] 
rice_weights = [50, 35, 15]

topping = ["Hiromi", "Roe", "Unagi", "Salmon"] 
topping_weights = [40, 30, 20, 10]

face = ["DarkSad", "DarkHappy", "PinkSad", "PinkHappy"] 
face_weights = [40, 30, 20, 10]

# Dictionary variable for each trait. 
# Each trait corresponds to its file name (from raw images from Github)

background_files = {
    "Blue": "background-blue",
    "Green": "background-green",
    "Red": "background-red",
    "Yellow": "background-yellow",
}

rice_files = {
    "White": "rice-white",
    "Blue": "rice-blue",
    "Yellow": "rice-yellow",
}
topping_files = {
    "Hiromi": "topping-hiromi",
    "Roe": "topping-roe",
    "Unagi": "topping-unagi",
    "Salmon": "topping-salmon",
}

face_files = {
    "DarkSad": "face-darksad",
    "DarkHappy": "face-darkhappy",
    "PinkSad": "face-pinksad",
    "PinkHappy": "face-pinkhappy",
          
}
