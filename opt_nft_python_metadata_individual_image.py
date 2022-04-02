##OPTIONAL 
# Generate Metadata for each Image    

f = open('/content/NFT_tutorial_python/metadata/metadata.json',) 
data = json.load(f)

IMAGES_BASE_URI = "ADD_IMAGES_BASE_URI_HERE"
PROJECT_NAME = "ADD_PROJECT_NAME_HERE"

def getAttribute(key, value):
    return {
        "trait_type": key,
        "value": value
    }
for i in data:
    token_id = i['tokenId']
    token = {
        "image": IMAGES_BASE_URI + str(token_id) + '.png',
        "tokenId": token_id,
        "name": PROJECT_NAME + ' ' + str(token_id),
        "attributes": []
    }
    token["attributes"].append(getAttribute("Background", i["Background"]))
    token["attributes"].append(getAttribute("Rice", i["Rice"]))
    token["attributes"].append(getAttribute("Toppings", i["Toppings"]))
    token["attributes"].append(getAttribute("Face", i["Face"]))

    with open('/content/NFT_tutorial_python/metadata/' + str(token_id), 'w') as outfile:
        json.dump(token, outfile, indent=4)
f.close()
