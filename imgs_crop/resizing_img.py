import PIL
import os
import os.path
from PIL import Image

f = r'/home/mobaxterm/pythons/imgs_crop/pics'
for file in os.listdir(f):
	f_img = f+"/"+file
	img = Image.open(f_img)
	img = img.resize((2296,1724))
	img.save(f_img)
