import cv2
import numpy as np
import csv
from .utils import predict, resize_img


class BaseTransformer(object):

    def __init__(self, width=None):
        """

        :param width: 图片的标准宽度
        """
        self.width = width

    def __call__(self, img: np.ndarray) -> np.ndarray:
        raise NotImplementedError


class StyleTransformer(BaseTransformer):

    def __init__(self, width=None, model=None):
        super().__init__(width)
        self.net = None
        self.models = list(csv.reader(open('models/label.csv')))
        if model is not None:
            self.set_model(model)

    def __call__(self, img):
        if self.width is not None:
            img = resize_img(img, self.width)
        h, w = img.shape[:2]
        out = predict(img, h, w, self.net)
        return out

    def set_model(self, model=0):
        if isinstance(model, str):
            self.net = cv2.dnn.readNetFromTorch(model)
        else:
            self.net = cv2.dnn.readNetFromTorch(self.models[model][0])
