import cv2


class BaseManager(object):

    def __init__(self, transformer, path=None):
        if path is not None:
            self.path = path
        else:
            self.path = ""
        self.image = None
        self.transformer = transformer

    def __call__(self):
        return self.get_image()

    def get_image(self):
        if self.image is None:
            print("你没有读取图片")
        return self.image

    def read(self, image):
        raise NotImplementedError

    def save(self, file_path):
        raise NotImplementedError

    def render(self):
        """
        对图像进行处理和显示

        :return:
        """
        raise NotImplementedError


class CVManager(BaseManager):

    def __init__(self, transformer, path=None):
        super().__init__(transformer, path)
        self.show_num = 0
        self.vid = None

    def read(self, image):
        """

        :param image: 表示图片的numpy数组或图片路径
        :return: None
        """
        if isinstance(image, str):
            self.image = cv2.imread(self.path + image)
        else:
            self.image = image

    def save(self, file_path):
        cv2.imwrite(self.image, self.path + file_path)

    def render(self, delay=None):
        """

        :param delay: 延迟时间
        :return: 当前按下的键盘
        """
        out = self.transformer(self.image)
        cv2.imshow("CVManager 图片显示窗口", out)
        self.show_num += 1
        return cv2.waitKey(delay) & 0xFF

    def read_camera(self):
        if self.vid is None:
            self.vid = cv2.VideoCapture(0)
        _, self.image = self.vid.read()
