from ultralytics import YOLO
import os


def load_model(name: str):
    model = YOLO(os.path.join(os.path.dirname(__file__), name))
    return model
