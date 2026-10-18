from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.credential_external_type import CredentialExternalType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.credential_external_metadata import CredentialExternalMetadata





T = TypeVar("T", bound="CredentialExternal")



@_attrs_define
class CredentialExternal:
    """ 
        Attributes:
            method_id (str):
            type_ (CredentialExternalType):
            metadata (CredentialExternalMetadata | Unset):
     """

    method_id: str
    type_: CredentialExternalType
    metadata: CredentialExternalMetadata | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.credential_external_metadata import CredentialExternalMetadata # noqa: PLC0415
        method_id = self.method_id

        type_ = self.type_.value

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "methodID": method_id,
            "type": type_,
        })
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.credential_external_metadata import CredentialExternalMetadata # noqa: PLC0415
        d = dict(src_dict)
        method_id = d.pop("methodID")

        type_ = CredentialExternalType(d.pop("type"))




        _metadata = d.pop("metadata", UNSET)
        metadata: CredentialExternalMetadata | Unset
        if isinstance(_metadata,  Unset):
            metadata = UNSET
        else:
            metadata = CredentialExternalMetadata.from_dict(_metadata)




        credential_external = cls(
            method_id=method_id,
            type_=type_,
            metadata=metadata,
        )

        return credential_external

