import cv2
import ray
import numpy as np


MAX_HEIGHT = 720


@ray.remote
class ViewerActor:
    def __init__(self, window_name: str):
        self.window_name = window_name
        cv2.namedWindow(self.window_name, cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO | cv2.WINDOW_GUI_EXPANDED)

    def show(self, image: np.ndarray):
        height = image.shape[0]
        if height > MAX_HEIGHT:
            scale = MAX_HEIGHT / height
            image = cv2.resize(image, (0, 0), fx=scale, fy=scale)
        cv2.imshow(self.window_name, image)
        cv2.waitKey(1)
