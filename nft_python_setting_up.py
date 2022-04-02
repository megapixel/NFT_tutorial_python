## Main Snippet 1 

# Import necessary libraries 
from PIL import Image 
import random
import json
import os

# Connect to Github repo to load raw images and metadata file
!rm -r /content/NFT_tutorial_python
!git clone https://github.com/megapixel/NFT_tutorial_python.git
