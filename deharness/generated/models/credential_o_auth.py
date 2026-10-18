from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.credential_o_auth_type import CredentialOAuthType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.credential_o_auth_metadata import CredentialOAuthMetadata





T = TypeVar("T", bound="CredentialOAuth")



@_attrs_define
class CredentialOAuth:
    """ 
        Attributes:
            access (str):
            expires (int):
            method_id (str):
            refresh (str):
            type_ (CredentialOAuthType):
            metadata (CredentialOAuthMetadata | Unset):
     """

    access: str
    expires: int
    method_id: str
    refresh: str
    type_: CredentialOAuthType
    metadata: CredentialOAuthMetadata | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.credential_o_auth_metadata import CredentialOAuthMetadata # noqa: PLC0415
        access = self.access

        expires = self.expires

        method_id = self.method_id

        refresh = self.refresh

        type_ = self.type_.value

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "access": access,
            "expires": expires,
            "methodID": method_id,
            "refresh": refresh,
            "type": type_,
        })
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.credential_o_auth_metadata import CredentialOAuthMetadata # noqa: PLC0415
        d = dict(src_dict)
        access = d.pop("access")

        expires = d.pop("expires")

        method_id = d.pop("methodID")

        refresh = d.pop("refresh")

        type_ = CredentialOAuthType(d.pop("type"))




        _metadata = d.pop("metadata", UNSET)
        metadata: CredentialOAuthMetadata | Unset
        if isinstance(_metadata,  Unset):
            metadata = UNSET
        else:
            metadata = CredentialOAuthMetadata.from_dict(_metadata)




        credential_o_auth = cls(
            access=access,
            expires=expires,
            method_id=method_id,
            refresh=refresh,
            type_=type_,
            metadata=metadata,
        )

        return credential_o_auth

