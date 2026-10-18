from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.rpc_internal_error_encoded_tag import RpcInternalErrorEncodedTag
from ..models.rpc_internal_error_encoded_type import RpcInternalErrorEncodedType
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="RpcInternalErrorEncoded")



@_attrs_define
class RpcInternalErrorEncoded:
    """ 
        Attributes:
            field_tag (RpcInternalErrorEncodedTag):
            message (str):
            type_ (RpcInternalErrorEncodedType):
            data (Any | None | Unset):
     """

    field_tag: RpcInternalErrorEncodedTag
    message: str
    type_: RpcInternalErrorEncodedType
    data: Any | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        field_tag = self.field_tag.value

        message = self.message

        type_ = self.type_.value

        data: Any | None | Unset
        if isinstance(self.data, Unset):
            data = UNSET
        else:
            data = self.data


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "_tag": field_tag,
            "message": message,
            "type": type_,
        })
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_tag = RpcInternalErrorEncodedTag(d.pop("_tag"))




        message = d.pop("message")

        type_ = RpcInternalErrorEncodedType(d.pop("type"))




        def _parse_data(data: object) -> Any | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Any | None | Unset, data)

        data = _parse_data(d.pop("data", UNSET))


        rpc_internal_error_encoded = cls(
            field_tag=field_tag,
            message=message,
            type_=type_,
            data=data,
        )

        return rpc_internal_error_encoded

