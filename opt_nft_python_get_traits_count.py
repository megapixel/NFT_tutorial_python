##OPTIONAL 

# Get Trait Counts
background_count = {}
for item in background:
    background_count[item] = 0

rice_count = {}
for item in rice:
    rice_count[item] = 0
    
topping_count = {}
for item in topping:
    topping_count[item] = 0

face_count = {}
for item in face:
    face_count[item] = 0

for image in all_images:
    background_count[image["Background"]] += 1
    rice_count[image["Rice"]] += 1
    topping_count[image["Toppings"]] += 1
    face_count[image["Face"]] += 1
    
print(background_count)
print(rice_count)
print(topping_count)
print(face_count)
