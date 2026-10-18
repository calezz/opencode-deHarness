from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.credential_entry import CredentialEntry





T = TypeVar("T", bound="CredentialCreateResponse200")



@_attrs_define
class CredentialCreateResponse200:
    """ 
        Attributes:
            data (CredentialEntry):
     """

    data: CredentialEntry





    def to_dict(self) -> dict[str, Any]:
        from ..models.credential_entry import CredentialEntry # noqa: PLC0415
        data = self.data.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "data": data,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.credential_entry import CredentialEntry # noqa: PLC0415
        d = dict(src_dict)
        data = CredentialEntry.from_dict(d.pop("data"))




        credential_create_response_200 = cls(
            data=data,
        )

        return credential_create_response_200

