os.system("pip2 install requests lolcat")
	os.system("python2 background.py")
from PIL import Image
from rembg import remove
real=input('input file to remove background')
bg=input('input background to change')
rel=Image.open(real)
rem=remove(rel)
bg.save(rem)
print('succesfully')
