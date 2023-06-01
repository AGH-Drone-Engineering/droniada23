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
        results = self.model(img, conf=self.conf, iou=self.iou, verbose=False)[0]
        boxes = results.boxes.numpy()
        xywhc = [(box.xywh, box.cls) for box in boxes]
        return xywhc
