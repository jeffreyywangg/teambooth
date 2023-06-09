# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import service_pb2 as service__pb2


class MessageServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RaftRequestVote = channel.unary_unary(
                '/MessageService/RaftRequestVote',
                request_serializer=service__pb2.RaftRequestVoteRequest.SerializeToString,
                response_deserializer=service__pb2.RaftRequestVoteResponse.FromString,
                )
        self.RaftUpdateState = channel.unary_unary(
                '/MessageService/RaftUpdateState',
                request_serializer=service__pb2.RaftUpdateStateRequest.SerializeToString,
                response_deserializer=service__pb2.EmptyResponse.FromString,
                )
        self.Merge = channel.unary_unary(
                '/MessageService/Merge',
                request_serializer=service__pb2.MergeRequest.SerializeToString,
                response_deserializer=service__pb2.ModelResponse.FromString,
                )
        self.Get = channel.unary_unary(
                '/MessageService/Get',
                request_serializer=service__pb2.GetRequest.SerializeToString,
                response_deserializer=service__pb2.ModelResponse.FromString,
                )


class MessageServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def RaftRequestVote(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RaftUpdateState(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Merge(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Get(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MessageServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RaftRequestVote': grpc.unary_unary_rpc_method_handler(
                    servicer.RaftRequestVote,
                    request_deserializer=service__pb2.RaftRequestVoteRequest.FromString,
                    response_serializer=service__pb2.RaftRequestVoteResponse.SerializeToString,
            ),
            'RaftUpdateState': grpc.unary_unary_rpc_method_handler(
                    servicer.RaftUpdateState,
                    request_deserializer=service__pb2.RaftUpdateStateRequest.FromString,
                    response_serializer=service__pb2.EmptyResponse.SerializeToString,
            ),
            'Merge': grpc.unary_unary_rpc_method_handler(
                    servicer.Merge,
                    request_deserializer=service__pb2.MergeRequest.FromString,
                    response_serializer=service__pb2.ModelResponse.SerializeToString,
            ),
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=service__pb2.GetRequest.FromString,
                    response_serializer=service__pb2.ModelResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'MessageService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MessageService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def RaftRequestVote(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/MessageService/RaftRequestVote',
            service__pb2.RaftRequestVoteRequest.SerializeToString,
            service__pb2.RaftRequestVoteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RaftUpdateState(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/MessageService/RaftUpdateState',
            service__pb2.RaftUpdateStateRequest.SerializeToString,
            service__pb2.EmptyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Merge(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/MessageService/Merge',
            service__pb2.MergeRequest.SerializeToString,
            service__pb2.ModelResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/MessageService/Get',
            service__pb2.GetRequest.SerializeToString,
            service__pb2.ModelResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
