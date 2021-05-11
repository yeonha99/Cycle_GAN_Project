# 해당 코드는 jupyter lab에서 실행한 코드입니다. 

import os
import glob 
from PIL import Image

files = glob.glob('./human/human_test/*.jpg')

for f in files:
    img = Image.open(f)
    img_resize = img.resize((256,256))
    title, ext = os.path.splitext(f)
    img_resize.save(title+"__"+ext)
