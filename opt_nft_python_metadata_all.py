##OPTIONAL

# Generate Metadata for all Traits 
with open('/content/NFT_tutorial_python/metadata/metadata.json', 'w') as outfile:
    json.dump(all_images, outfile, indent=4)
