from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.connection_env_info_type import ConnectionEnvInfoType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.connection_status import ConnectionStatus





T = TypeVar("T", bound="ConnectionEnvInfo")



@_attrs_define
class ConnectionEnvInfo:
    """ 
        Attributes:
            name (str):
            type_ (ConnectionEnvInfoType):
            status (ConnectionStatus | Unset):
     """

    name: str
    type_: ConnectionEnvInfoType
    status: ConnectionStatus | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.connection_status import ConnectionStatus # noqa: PLC0415
        name = self.name

        type_ = self.type_.value

        status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "name": name,
            "type": type_,
        })
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.connection_status import ConnectionStatus # noqa: PLC0415
        d = dict(src_dict)
        name = d.pop("name")

        type_ = ConnectionEnvInfoType(d.pop("type"))




        _status = d.pop("status", UNSET)
        status: ConnectionStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = ConnectionStatus.from_dict(_status)




        connection_env_info = cls(
            name=name,
            type_=type_,
            status=status,
        )

        return connection_env_info

