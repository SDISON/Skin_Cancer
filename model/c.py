import numpy as np
from PIL import Image
from tqdm import tqdm
import os
import cv2
import tensorflow
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense,Dropout,BatchNormalization

resnet_weights_path = '/home/i_am_groot/PycharmProjects/minor2/cancer/model/resnet50_weights_tf_dim_ordering_tf_kernels_notop.h5'

class checker:
    def Dataset_loader(self,DIR, RESIZE):
        IMG = []
        read = lambda imname: np.asarray(Image.open(imname).convert("RGB"))
        for IMAGE_NAME in tqdm(os.listdir(DIR)):
            PATH = os.path.join(DIR, IMAGE_NAME)
            _, ftype = os.path.splitext(PATH)
            if ftype == ".jpg":
                img = read(PATH)
                img = cv2.resize(img, (RESIZE, RESIZE))
                IMG.append(np.array(img) / 255.)
        return IMG

    def run(self):

        self.model = Sequential()
        self.model.add(ResNet50(include_top=False, input_tensor=None, input_shape=(224, 224, 3), pooling='avg', classes=2,
                       weights=resnet_weights_path))
        #print(self.model.output)
        self.model.add(Flatten())
        self.model.add(Dense(512, activation='relu'))
        self.model.add(Dropout(0.5))
        self.model.add(BatchNormalization())
        self.model.add(Dense(256, activation='relu'))
        self.model.add(Dropout(0.5))
        self.model.add(BatchNormalization())
        self.model.add(Dense(1, activation='sigmoid'))
        self.model.load_weights('/home/i_am_groot/PycharmProjects/minor2/cancer/model/modelll.h5')
        self.model.layers[0].trainable = False
        self.graph = tensorflow.get_default_graph()
        #self.session = tensorflow.InteractiveSession()
        self.model.add(BatchNormalization())

    def testing(self):
        #init = tensorflow.global_variables_initializer()
        #(self.session).run(init)
        X = np.array(self.Dataset_loader('/home/i_am_groot/PycharmProjects/minor2/cancer/media', 224))
        with self.graph.as_default():
            y_pred = (self.model).predict(X)
            return y_pred
