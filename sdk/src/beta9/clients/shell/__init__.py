# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: shell.proto
# plugin: python-betterproto
# This file has been @generated

from dataclasses import dataclass
from typing import (
    TYPE_CHECKING,
    Dict,
    Optional,
)

import betterproto
import grpc
from betterproto.grpcstub.grpcio_client import SyncServiceStub
from betterproto.grpcstub.grpclib_server import ServiceBase


if TYPE_CHECKING:
    import grpclib.server
    from betterproto.grpcstub.grpclib_client import MetadataLike
    from grpclib.metadata import Deadline


@dataclass(eq=False, repr=False)
class CreateShellRequest(betterproto.Message):
    stub_id: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class CreateShellResponse(betterproto.Message):
    ok: bool = betterproto.bool_field(1)
    container_id: str = betterproto.string_field(2)
    token: str = betterproto.string_field(3)
    err_msg: str = betterproto.string_field(4)


class ShellServiceStub(SyncServiceStub):
    def create_shell(
        self, create_shell_request: "CreateShellRequest"
    ) -> "CreateShellResponse":
        return self._unary_unary(
            "/shell.ShellService/CreateShell",
            CreateShellRequest,
            CreateShellResponse,
        )(create_shell_request)
