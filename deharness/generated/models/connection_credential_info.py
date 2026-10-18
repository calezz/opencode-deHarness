from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.connection_credential_info_method import ConnectionCredentialInfoMethod
from ..models.connection_credential_info_type import ConnectionCredentialInfoType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.connection_status import ConnectionStatus





T = TypeVar("T", bound="ConnectionCredentialInfo")



@_attrs_define
class ConnectionCredentialInfo:
    """ 
        Attributes:
            id (str):
            label (str):
            method (ConnectionCredentialInfoMethod):
            type_ (ConnectionCredentialInfoType):
            status (ConnectionStatus | Unset):
     """

    id: str
    label: str
    method: ConnectionCredentialInfoMethod
    type_: ConnectionCredentialInfoType
    status: ConnectionStatus | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.connection_status import ConnectionStatus # noqa: PLC0415
        id = self.id

        label = self.label

        method = self.method.value

        type_ = self.type_.value

        status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "label": label,
            "method": method,
            "type": type_,
        })
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.connection_status import ConnectionStatus # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id")

        label = d.pop("label")

        method = ConnectionCredentialInfoMethod(d.pop("method"))




        type_ = ConnectionCredentialInfoType(d.pop("type"))




        _status = d.pop("status", UNSET)
        status: ConnectionStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = ConnectionStatus.from_dict(_status)




        connection_credential_info = cls(
            id=id,
            label=label,
            method=method,
            type_=type_,
            status=status,
        )

        return connection_credential_info

