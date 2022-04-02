# Import necessary libraries 
from PIL import Image
import random

# Connect to Github repo to load images for the collage
!rm -r /content/NFT_tutorial_python
!git clone https://github.com/megapixel/NFT_tutorial_python.git

# Define the size of the collage
collage = Image.new("RGBA", (5000,2500), color=(255,255,255,255))

# Declare the number of images and randomly shuffle them in a list 
max = 50
l = list(range(0, max))  
random.shuffle(l)

# Declare a variable 'C' to access the element in the list 
c=0

# Define a function to create the collage 
for i in range(0,5000,500):
    for j in range(0,2500,500):
        file = "/content/images/"+str(l[c])+".png"
        photo = Image.open(file).convert("RGBA")
        photo = photo.resize((500,500))        
        
        collage.paste(photo, (i,j))
        c+=1
        
# Make a directory to save the collage image 
collage.save("/content/collage.png")
