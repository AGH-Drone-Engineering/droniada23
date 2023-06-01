import ray
from omegaconf import DictConfig
import grpc

from droniada23_drzewko.mavic import mavic_pb2
from droniada23_drzewko.mavic import mavic_pb2_grpc
from droniada23_drzewko.data.telemetry import Telemetry


@ray.remote
class TelemActor:
    def __init__(self, cfg: DictConfig):
        self.channel = grpc.insecure_channel(cfg.grpc_server)
        self.stub = mavic_pb2_grpc.TelemetryServiceStub(self.channel)

    def get_telemetry(self):
        resp = self.stub.GetTelemetry(mavic_pb2.Empty())
        return Telemetry(
            lat=resp.lat,
            lon=resp.long,
            alt=resp.altitude,
            hdg=resp.heading,
        )
