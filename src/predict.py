import processImage
import searchArray
import keras;
import tensorflow as tf;
import numpy as np



model = keras.models.load_model('my_model.h5')




img = processImage. loadImage ("0.jpg")

img = processImage. resizeImage (img)

img = processImage. arrayImage (img)

img = processImage. retypeImage (img)

#img = processImage. normalizeImage (img)


ex = model. predict (img)




elem = max (ex [0])


index = searchArray. index (ex [0], elem)


print (index)
