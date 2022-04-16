import glob
from PIL import Image
import os

# change size for all image file
source_folder = 'C:/Users/DELL/Desktop/pics/New folder (2)/'
destination_folder = 'C:/Users/DELL/Desktop/pics/New folder (3)/'
directory = os.listdir(source_folder)
print(directory)

for item in directory:
    img = Image.open(source_folder + item)
    width, height = img.size
    ratio = width / height
    new_width = 900
    new_height = int(new_width/ratio)
    imgResize = img.resize((new_width, new_height), Image.ANTIALIAS)
    imgResize.save(destination_folder + item[:-4] + '.jpg', quality=100)

# # change name of file
# os.chdir("C:/Users/DELL/Desktop/pics/New folder")
# for index, oldfile in enumerate(glob.glob("*.jpg"), start=1):
#     print(list(enumerate(glob.glob("*.jpg"), start=1)))
#     newfile = '{}.jpg'.format(index)
#     os.rename(oldfile, newfile)

# change extensions of file
# os.chdir("C:/Users/DELL/Desktop/pics/New folder")
# for oldfile in glob.glob("*.*"):
#     print(os.path.splitext(oldfile))
#     base = os.path.splitext(oldfile)[0]
#     newfile = '.jpg'
#     os.rename(oldfile, base + newfile)