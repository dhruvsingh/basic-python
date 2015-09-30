import Image
import sys

# Will only convert first frame of gif to jpeg
def gifToJpg(infile):
    file_name = infile[:infile.rfind('.')]
    
    try:
        im = Image.open(infile)
    except IOError:
        return False
    
    mypalette = im.getpalette()

    im.putpalette(mypalette)
    new_im = Image.new("RGBA", im.size)
    new_im.paste(im)
    new_im.save(file_name + '.jpg', 'JPEG')

def bmpToJpg(infile):
    file_name = infile[:infile.rfind('.')]
    
    try:
        im = Image.open(infile)
    except IOError:
        return False

    im.save(file_name + '.jpg', "JPEG")
