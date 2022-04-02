##OPTIONAL 

#To download generated NFT arts locally 
from google.colab import files
!zip -r /content/nft_images.zip /content/images/
files.download("/content/nft_images.zip")
