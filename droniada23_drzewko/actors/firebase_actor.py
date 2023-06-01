import ray
from omegaconf import DictConfig
import firebase_admin
from firebase_admin import credentials, firestore

from droniada23_drzewko.data.telemetry import Telemetry
from droniada23_drzewko.secrets import get_secret_path


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
