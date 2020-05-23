import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
D="C:\\Users\\priyanshi burad\\Desktop\\colour"
CATEGORIES=["red","blue","green"]

img_size=50
training_data = []
def create_training_data():
    for category in CATEGORIES:
        path = os.path.join(D,category)
        class_num=CATEGORIES.index(category)
        for img in os.listdir(path):
            try:
                img_array=cv2.imread(os.path.join(path,img))
                img_size=50
                new_array=cv2.resize(img_array,(img_size,img_size))
                training_data.append([new_array,class_num])
            except Exception as e:
                pass
create_training_data()
print(len(training_data))



import random
random.shuffle(training_data)
for sample in training_data:
    print(sample[1])



X = []
y = []
for features,label in training_data:
    X.append(features)
    y.append(label)

#X = np.array(X).reshape(-1,img_size, img_size,1)
X = np.array(X)
y=np.array(y)


import pickle

pickle_out= open("X.pickle","wb")
pickle.dump(X, pickle_out)
pickle_out.close()

pickle_out= open("y.pickle","wb")
pickle.dump(y,pickle_out)
pickle_out.close()
pickle_in=open("X.pickle","rb")
X= pickle.load(pickle_in)
print(X[1])
