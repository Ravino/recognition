import sys
import processImage
import searchArray
import keras;
import tensorflow as tf;
import numpy as np



model = keras.models.load_model('my_model.h5')




pathImg = "0.jpg"



if len (sys. argv) > 1:

  pathImg = "img/" + sys. argv [1]




img = processImage. loadImage (pathImg)

img = processImage. resizeImage (img)

img = processImage. arrayImage (img)

img = processImage. retypeImage (img)

#img = processImage. normalizeImage (img)


ex = model. predict (img)




elem = max (ex [0])


index = searchArray. index (ex [0], elem)


print ("Result recognition image: {}". format (index))
