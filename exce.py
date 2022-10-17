from PIL import Image
import math
from colormaa import fore
y=input('Put the file dircetiom e.g r file name')
ao=Image.open(y)
ww,hh=ao.size
print(fore.BLUE+ao.size,'the size pf the image by')
Osize=input('x as width eg 300')
Wsize=y=input('y as height eg 100')
try:
	fil=ao.resize((Osize,Wsizr),Image.ANTIALIAS)
loc=input('where to save the image if \n it was jpg or png you want to save it input rememberto put r')
fil.save(loc,quality=95)
Except :
	print('was not found',y+fore.RED)
	finally:
		print('finished')
		ao.close()
