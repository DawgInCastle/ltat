import src.ltat.utils as utils
import typing
import numpy
import PIL.Image

image_type = typing.Union[numpy.ndarray, PIL.Image.Image]

def base_working(image : image_type):
  return utils.CustomAnim(image=image)

def base_video_1_frame(image : image_type):
  return utils.CustomAnim(image = image).generate_images(lambda x : x)

def test_load_numpy():
  assert base_working(numpy.asarray(PIL.Image.open("images/starry2.jfif"))).get_shape() == (1080, 1920, 3), "Size of image should be (1080, 1920, 3)"

# def test_load_PIL():
#   assert base_working(PIL.Image.open("images/starry2.jfif")).get_shape() == (1080, 1920, 3)

def test_run_video():
  assert base_video_1_frame(numpy.asarray(PIL.Image.open("images/starry2.jfif"))).__len__() == 2, "Should be a 2 frame image sequence"
