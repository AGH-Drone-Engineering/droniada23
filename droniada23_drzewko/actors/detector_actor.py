import ray
import cv2
from ultralytics import YOLO
from omegaconf import DictConfig


@ray.remote
class DetectorActor:
    def __init__(self, cfg: DictConfig):
        pass
