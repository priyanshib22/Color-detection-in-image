import cv2
import tensorflow as tf

CATEGORIES = ["red","blue","green"]

def prepare(filepath):
    img_size=70
    img_array = cv2.imread(filepath)
    new_array = cv2.resize(img_array, (img_size,img_size))
    return new_array.reshape(3, img_size, img_size,1)
model = tf.keras.models.load_model("64x3-CNN.model")

prediction = model.predict([prepare('C:\\Users\\priyanshi burad\\Desktop\\train.jpg')])
print(prediction)
    
