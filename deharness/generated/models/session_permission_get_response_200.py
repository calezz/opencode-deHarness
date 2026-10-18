from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.permission_request import PermissionRequest





T = TypeVar("T", bound="SessionPermissionGetResponse200")



@_attrs_define
class SessionPermissionGetResponse200:
    """ 
        Attributes:
            data (PermissionRequest):
     """

    data: PermissionRequest





    def to_dict(self) -> dict[str, Any]:
        from ..models.permission_request import PermissionRequest # noqa: PLC0415
        data = self.data.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "data": data,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.permission_request import PermissionRequest # noqa: PLC0415
        d = dict(src_dict)
        data = PermissionRequest.from_dict(d.pop("data"))




        session_permission_get_response_200 = cls(
            data=data,
        )

        return session_permission_get_response_200

