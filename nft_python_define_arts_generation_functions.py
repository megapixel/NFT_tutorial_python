## Main Snippet 3

# Generate Traits
# Number of random unique images to be generated
TOTAL_IMAGES = 50

all_images = [] 

# A recursive function to generate unique image combinations
def create_new_image():
    
    new_image = {} #

    # For each trait category, select a random trait based on the weightings 
    new_image ["Background"] = random.choices(background, background_weights)[0]
    new_image ["Rice"] = random.choices(rice, rice_weights)[0]
    new_image ["Toppings"] = random.choices(topping, topping_weights)[0]
    new_image ["Face"] = random.choices(face, face_weights)[0]
    
    if new_image in all_images:
        return create_new_image()
    else:
        return new_image
    
    
# Generate the unique combinations based on trait weightings
for i in range(TOTAL_IMAGES): 
    
    new_trait_image = create_new_image()
    
    all_images.append(new_trait_image)

# Add token Id to each image
i = 0
for item in all_images:
    item["tokenId"] = i
    i = i + 1
