# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import grpc_tuna_pb2 as grpc__tuna__pb2


class DataStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get_color = channel.unary_unary(
                '/data.Data/Get_color',
                request_serializer=grpc__tuna__pb2.Empty.SerializeToString,
                response_deserializer=grpc__tuna__pb2.Vision_color.FromString,
                )
        self.Count = channel.unary_unary(
                '/data.Data/Count',
                request_serializer=grpc__tuna__pb2.Empty.SerializeToString,
                response_deserializer=grpc__tuna__pb2.Counts.FromString,
                )
        self.Robot1_color = channel.unary_unary(
                '/data.Data/Robot1_color',
                request_serializer=grpc__tuna__pb2.Empty.SerializeToString,
                response_deserializer=grpc__tuna__pb2.robot1_color.FromString,
                )
        self.Remain = channel.unary_unary(
                '/data.Data/Remain',
                request_serializer=grpc__tuna__pb2.Empty.SerializeToString,
                response_deserializer=grpc__tuna__pb2.remain.FromString,
                )
        self.Maximum = channel.unary_unary(
                '/data.Data/Maximum',
                request_serializer=grpc__tuna__pb2.Empty.SerializeToString,
                response_deserializer=grpc__tuna__pb2.maximum.FromString,
                )
        self.Robot2_weight = channel.unary_unary(
                '/data.Data/Robot2_weight',
                request_serializer=grpc__tuna__pb2.Empty.SerializeToString,
                response_deserializer=grpc__tuna__pb2.robot2_weight.FromString,
                )
        self.Robot3_weight = channel.unary_unary(
                '/data.Data/Robot3_weight',
                request_serializer=grpc__tuna__pb2.Empty.SerializeToString,
                response_deserializer=grpc__tuna__pb2.robot3_weight.FromString,
                )


class DataServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Get_color(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Count(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Robot1_color(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Remain(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Maximum(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Robot2_weight(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Robot3_weight(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DataServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get_color': grpc.unary_unary_rpc_method_handler(
                    servicer.Get_color,
                    request_deserializer=grpc__tuna__pb2.Empty.FromString,
                    response_serializer=grpc__tuna__pb2.Vision_color.SerializeToString,
            ),
            'Count': grpc.unary_unary_rpc_method_handler(
                    servicer.Count,
                    request_deserializer=grpc__tuna__pb2.Empty.FromString,
                    response_serializer=grpc__tuna__pb2.Counts.SerializeToString,
            ),
            'Robot1_color': grpc.unary_unary_rpc_method_handler(
                    servicer.Robot1_color,
                    request_deserializer=grpc__tuna__pb2.Empty.FromString,
                    response_serializer=grpc__tuna__pb2.robot1_color.SerializeToString,
            ),
            'Remain': grpc.unary_unary_rpc_method_handler(
                    servicer.Remain,
                    request_deserializer=grpc__tuna__pb2.Empty.FromString,
                    response_serializer=grpc__tuna__pb2.remain.SerializeToString,
            ),
            'Maximum': grpc.unary_unary_rpc_method_handler(
                    servicer.Maximum,
                    request_deserializer=grpc__tuna__pb2.Empty.FromString,
                    response_serializer=grpc__tuna__pb2.maximum.SerializeToString,
            ),
            'Robot2_weight': grpc.unary_unary_rpc_method_handler(
                    servicer.Robot2_weight,
                    request_deserializer=grpc__tuna__pb2.Empty.FromString,
                    response_serializer=grpc__tuna__pb2.robot2_weight.SerializeToString,
            ),
            'Robot3_weight': grpc.unary_unary_rpc_method_handler(
                    servicer.Robot3_weight,
                    request_deserializer=grpc__tuna__pb2.Empty.FromString,
                    response_serializer=grpc__tuna__pb2.robot3_weight.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'data.Data', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Data(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Get_color(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/data.Data/Get_color',
            grpc__tuna__pb2.Empty.SerializeToString,
            grpc__tuna__pb2.Vision_color.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Count(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/data.Data/Count',
            grpc__tuna__pb2.Empty.SerializeToString,
            grpc__tuna__pb2.Counts.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Robot1_color(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/data.Data/Robot1_color',
            grpc__tuna__pb2.Empty.SerializeToString,
            grpc__tuna__pb2.robot1_color.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Remain(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/data.Data/Remain',
            grpc__tuna__pb2.Empty.SerializeToString,
            grpc__tuna__pb2.remain.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Maximum(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/data.Data/Maximum',
            grpc__tuna__pb2.Empty.SerializeToString,
            grpc__tuna__pb2.maximum.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Robot2_weight(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/data.Data/Robot2_weight',
            grpc__tuna__pb2.Empty.SerializeToString,
            grpc__tuna__pb2.robot2_weight.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Robot3_weight(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/data.Data/Robot3_weight',
            grpc__tuna__pb2.Empty.SerializeToString,
            grpc__tuna__pb2.robot3_weight.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
