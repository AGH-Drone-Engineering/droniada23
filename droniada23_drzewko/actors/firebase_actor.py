import ray
import cv2
from omegaconf import DictConfig


@ray.remote
class FirebaseActor:
    def __init__(self, cfg: DictConfig):
        pass
