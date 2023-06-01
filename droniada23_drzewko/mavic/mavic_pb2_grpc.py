# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import mavic_pb2 as mavic__pb2


class TelemetryServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetTelemetry = channel.unary_unary(
                '/mavic.TelemetryService/GetTelemetry',
                request_serializer=mavic__pb2.Empty.SerializeToString,
                response_deserializer=mavic__pb2.Telemetry.FromString,
                )


class TelemetryServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetTelemetry(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TelemetryServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetTelemetry': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTelemetry,
                    request_deserializer=mavic__pb2.Empty.FromString,
                    response_serializer=mavic__pb2.Telemetry.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'mavic.TelemetryService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TelemetryService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetTelemetry(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mavic.TelemetryService/GetTelemetry',
            mavic__pb2.Empty.SerializeToString,
            mavic__pb2.Telemetry.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)