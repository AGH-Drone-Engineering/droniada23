import ray
import numpy as np
from omegaconf import DictConfig

from droniada23.drzewko.models import load_model


@ray.remote
class DetectorActor:
    def __init__(self, cfg: DictConfig):
        self.model = load_model(cfg.detector.model)
        self.conf = cfg.detector.conf
        self.iou = cfg.detector.iou

    def detect(self, img: np.ndarray):
        results = self.model(img, conf=self.conf, iou=self.iou, verbose=False, show=True)[0]
        boxes = results.boxes
        xywhc = [(box.xywh.numpy().squeeze(0), box.cls.item()) for box in boxes]
        return xywhc
