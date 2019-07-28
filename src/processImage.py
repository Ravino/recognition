from PIL import Image
import numpy as np




def loadImage (path):

  img = Image. open (path). convert ("L")


  return img




def resizeImage (image):

  img = image. resize ((28, 28))


  return img




def arrayImage (image):

  img = image. getdata ()


  imgArr = np. array ([img])


  return imgArr




def retypeImage (image):

  img = image. astype ("float32")


  return img




def normalizeImage (image):

  img = image / 255


  return img
