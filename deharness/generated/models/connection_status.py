from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.connection_status_status_type_0 import ConnectionStatusStatusType0
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ConnectionStatus")



@_attrs_define
class ConnectionStatus:
    """ 
        Attributes:
            message (str):
            status (ConnectionStatusStatusType0):
            url (str | Unset):
     """

    message: str
    status: ConnectionStatusStatusType0
    url: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        message = self.message

        status: str
        if isinstance(self.status, ConnectionStatusStatusType0):
            status = self.status.value


        url = self.url


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "message": message,
            "status": status,
        })
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message = d.pop("message")

        def _parse_status(data: object) -> ConnectionStatusStatusType0:
            if not isinstance(data, str):
                raise TypeError()
            status_type_0 = ConnectionStatusStatusType0(data)



            return status_type_0

        status = _parse_status(d.pop("status"))


        url = d.pop("url", UNSET)

        connection_status = cls(
            message=message,
            status=status,
            url=url,
        )

        return connection_status

