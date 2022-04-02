## Main Snippet 4

# Create a directory for output images 
os.mkdir("/content/images/") 

# Generate Images    
for item in all_images:

    im1 = Image.open(f'/content/NFT_tutorial_python/nft_raw_images/backgrounds/{background_files[item["Background"]]}.png').convert('RGBA')
    im2 = Image.open(f'/content/NFT_tutorial_python/nft_raw_images/rice/{rice_files[item["Rice"]]}.png').convert('RGBA')
    im3 = Image.open(f'/content/NFT_tutorial_python/nft_raw_images/topping/{topping_files[item["Toppings"]]}.png').convert('RGBA')
    im4 = Image.open(f'/content/NFT_tutorial_python/nft_raw_images/face/{face_files[item["Face"]]}.png').convert('RGBA')

    #Create each composite
    com1 = Image.alpha_composite(im1, im2)
    com2 = Image.alpha_composite(com1, im3)
    com3 = Image.alpha_composite(com2, im4)

    #Convert to RGB
    rgb_im = com3.convert('RGB')
    file_name = str(item["tokenId"]) + ".png"
    rgb_im.save("/content/images/" + file_name)
