import ray
from omegaconf import DictConfig
import os
import cv2
import time

from droniada23.common.data.stamped_frame import StampedFrame


@ray.remote
class LoggerActor:
    def __init__(self, cfg: DictConfig):
        self.log_dir = os.path.join(cfg.logger.dir, time.strftime('%Y-%m-%d_%H-%M-%S'))
        os.makedirs(self.log_dir)

        self.frames_dir = os.path.join(self.log_dir, 'frames')
        os.makedirs(self.frames_dir)

        self.telemetry_file = os.path.join(self.log_dir, 'telemetry.csv')

    def log_stamped_frame(self, stamped_frame: StampedFrame):
        timestamp = stamped_frame.timestamp
        telemetry = stamped_frame.telemetry
        frame = stamped_frame.frame
        frame_path = os.path.join(self.frames_dir, f'{timestamp}.jpg')
        with open(self.telemetry_file, 'a') as f:
            f.write(telemetry.to_csv_line(timestamp))
        cv2.imwrite(frame_path, frame)
