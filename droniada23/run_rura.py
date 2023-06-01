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


@ray.remote
def main_loop(cfg: DictConfig):
    camera_actor = CameraActor.remote(cfg)
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

        ray.get([
            firebase_actor.push_telemetry.remote(telemetry),
            logger_actor.log_stamped_frame.remote(stamped_frame),
        ])


@hydra.main(version_base=None, config_path='common/conf', config_name='config')
def main(cfg: DictConfig):
    ray.get(main_loop.remote(cfg))


if __name__ == '__main__':
    main()
