from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.pty_ticket_connect_token import PtyTicketConnectToken





T = TypeVar("T", bound="ServerExperimentalPersistentPtyConnectTokenResponse200")



@_attrs_define
class ServerExperimentalPersistentPtyConnectTokenResponse200:
    """ 
        Attributes:
            data (PtyTicketConnectToken):
     """

    data: PtyTicketConnectToken





    def to_dict(self) -> dict[str, Any]:
        from ..models.pty_ticket_connect_token import PtyTicketConnectToken # noqa: PLC0415
        data = self.data.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "data": data,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pty_ticket_connect_token import PtyTicketConnectToken # noqa: PLC0415
        d = dict(src_dict)
        data = PtyTicketConnectToken.from_dict(d.pop("data"))




        server_experimental_persistent_pty_connect_token_response_200 = cls(
            data=data,
        )

        return server_experimental_persistent_pty_connect_token_response_200

