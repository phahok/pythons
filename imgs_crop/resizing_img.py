import PIL
import os
import os.path
from PIL import Image

f = r'/workspace/pythons/imgs_crop/pics'
for file in os.listdir(f):
	f_img = f+"/"+file
	img = Image.open(f_img)
	img = img.resize((550,420))
	img.save(f_img)