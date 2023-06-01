import ray
import hydra
from omegaconf import DictConfig
import time

from droniada23.common.actors.firebase_actor import FirebaseActor
from droniada23.common.actors.camera_actor import CameraActor
from droniada23.common.actors.logger_actor import LoggerActor
from droniada23.common.actors.telem_actor import TelemActor
from droniada23.common.data.telemetry import Telemetry
from droniada23.common.data.stamped_frame import StampedFrame

from droniada23.drzewko.actors.detector_actor import DetectorActor


@ray.remote
def main_loop(cfg: DictConfig):
    camera_actor = CameraActor.remote(cfg)
    detector_actor = DetectorActor.remote(cfg)
    telem_actor = TelemActor.remote(cfg)
    logger_actor = LoggerActor.remote(cfg)
    firebase_actor = FirebaseActor.remote(cfg)

    while True:
        frame, telemetry = ray.get([
            camera_actor.get_frame.remote(),
            telem_actor.get_telemetry.remote(),
        ])
        stamped_frame = StampedFrame(
            timestamp=time.time(),
            frame=frame,
            telemetry=telemetry,
        )

        xywhc, _, _ = ray.get([
            detector_actor.detect.remote(frame),
            firebase_actor.push_telemetry.remote(telemetry),
            logger_actor.log_stamped_frame.remote(stamped_frame),
        ])

        refs = []
        for xywh, cls in xywhc:
            lat, lon = telemetry.lat, telemetry.lon
            if cls == 'white_square':
                name = 'Zdrowe'
                type_ = 'white'
            elif cls == 'brown_square':
                name = 'Podatne'
                type_ = 'brown'
            elif cls == 'gold_circle':
                name = 'Parch'
                type_ = 'gold'
            elif cls == 'white_circle':
                name = 'Mączniak'
                type_ = 'beige'
            else:
                name = 'Nieznany'
                type_ = 'unknown'
            x1, y1, w, h = xywh
            x2, y2 = x1 + w, y1 + h
            img = frame[y1:y2, x1:x2]
            refs.append(firebase_actor.push_detection.remote(lat, lon, name, type_, img))


@hydra.main(version_base=None, config_path='common/conf', config_name='config')
def main(cfg: DictConfig):
    ray.get(main_loop.remote(cfg))


if __name__ == '__main__':
    main()
