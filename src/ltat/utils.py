import matplotlib.animation
import matplotlib.pyplot
import matplotlib.artist
import numpy
import PIL.Image
import typing

image_type : typing.Any = typing.Union[numpy.ndarray, PIL.Image.Image]

def show_image(image : image_type) -> None:
  """Display the image onto the terminal"""
  matplotlib.pyplot.imshow(image)
  matplotlib.pyplot.show()
  return

class CustomAnim:
  """Custom animation class for the specifed thing"""
  """Waving animation"""

  # TODO : To implement both ones
  def __init__(self, image : image_type) -> None:
    if (type(image) == PIL.Image.Image):
      image = numpy.asarray(image)
    self.image : numpy.ndarray = image

  def get_shape(self) -> typing.Tuple[int,...]:
    return self.image.shape

  def get_video(self, func : typing.Callable[[image_type], image_type], number_of_frames = -1) -> matplotlib.animation.Animation:
    fig, ax =matplotlib.pyplot.subplots()
    img_frames_numpy : list[image_type] = self.generate_images(func, number_of_frames = number_of_frames)
    # Artist requires mnatplotlib.artist.Artist frames
    print(f"Number of frames : {len(img_frames_numpy)}")
    img_frames_artist : list[matplotlib.artist.Artist] = [
      [ax.imshow(img, animated = True)]
      for img in img_frames_numpy
    ]
    anim_temp : matplotlib.animation.ArtistAnimation = matplotlib.animation.ArtistAnimation(fig, img_frames_artist, interval=50)
    # Show the video for now
    matplotlib.pyplot.show()
    return anim_temp

  def generate_images(self, func: typing.Callable[[image_type], image_type], number_of_frames : int = -1) -> list[image_type]:
    """Generates the image list to be passed into the animation

    Paramaters:
    func : typing.Callable[[image_type], image_type]
    """
    image_list : list[image_type] = [self.image]
    next_image : numpy.ndarray = self.image
    prev_image : numpy.ndarray = numpy.zeros(self.image.shape)
    
    # TODO : Maybe asserting this is degrading generative functionality
    assert((next_image == prev_image).all() == False), "Initial image should not be complete zeros"
    counter : int = number_of_frames
    while ((next_image == prev_image).all() == False and counter != 0):
      prev_image = next_image
      next_image = func(next_image)
      image_list.append(next_image)
      counter -= 1
    # else:

    return image_list
    
  def show_video(self) -> None:
    self.get_video()
    matplotlib.pyplot.show()
    return
