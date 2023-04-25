import ltat.utils as utils
import numpy
import PIL.Image

# Shows the correct code always
print("MakinPancakes has the G")

# This filewas created for the purposes of visualization tests will be removed
image_type = utils.image_type

img : image_type = numpy.asarray(PIL.Image.open("images/starry2.jfif"))

# Should show side burned starry night
utils.show_image(img)

# Shuld generate 30 frames of starry night losing its color to white
anim = utils.CustomAnim(img)

def lose_half(img : image_type):
  # Expecting RGB images only in numpy.ndarray format
  return img*0.5

anim.get_video(lose_half, 30)

