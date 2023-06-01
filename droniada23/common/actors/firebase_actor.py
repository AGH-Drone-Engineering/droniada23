import ray
import numpy as np
import cv2
import base64
from omegaconf import DictConfig
import firebase_admin
from firebase_admin import credentials, firestore

from droniada23.common.data.telemetry import Telemetry
from droniada23.common.secrets import get_secret_path


@ray.remote
class FirebaseActor:
    def __init__(self, cfg: DictConfig):
        cred = credentials.Certificate(get_secret_path('firebase.json'))
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()

    def push_telemetry(self, telemetry: Telemetry):
        self.db.collection('drone-path').add({
            'timestamp': firestore.SERVER_TIMESTAMP,
            'location': firestore.GeoPoint(telemetry.lat, telemetry.lon),
            'altitude': telemetry.alt,
        })

    def push_detection(self, lat: float, lon: float, name: str, type_: str, img: np.ndarray):
        _, buf = cv2.imencode('.jpg', img)
        img_base = base64.b64encode(buf).decode('utf-8')
        
        self.db.collection('tree-points').add({
            'img': img_base,
            'location': firestore.GeoPoint(lat, lon),
            'name': name,
            'shooted': False,
            'timestamp': firestore.SERVER_TIMESTAMP,
            'type': type_,
        })
