import ray
import cv2
from omegaconf import DictConfig


@ray.remote
class CameraActor:
    def __init__(self, cfg: DictConfig):
        self.camera = cv2.VideoCapture(cfg.camera.id)
        if cfg.camera.skip_sec is not None:
            self.camera.set(cv2.CAP_PROP_POS_MSEC, int(cfg.camera.skip_sec * 1000))

    def get_frame(self):
        ret, frame = self.camera.read()
        assert ret
        return frame
