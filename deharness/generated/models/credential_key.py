from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.credential_key_type import CredentialKeyType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.credential_key_metadata import CredentialKeyMetadata
  from ..models.form_answer_1 import FormAnswer1





T = TypeVar("T", bound="CredentialKey")



@_attrs_define
class CredentialKey:
    """ 
        Attributes:
            key (str):
            type_ (CredentialKeyType):
            configuration (FormAnswer1 | Unset):
            metadata (CredentialKeyMetadata | Unset):
     """

    key: str
    type_: CredentialKeyType
    configuration: FormAnswer1 | Unset = UNSET
    metadata: CredentialKeyMetadata | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.credential_key_metadata import CredentialKeyMetadata # noqa: PLC0415
        from ..models.form_answer_1 import FormAnswer1 # noqa: PLC0415
        key = self.key

        type_ = self.type_.value

        configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.configuration, Unset):
            configuration = self.configuration.to_dict()

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "key": key,
            "type": type_,
        })
        if configuration is not UNSET:
            field_dict["configuration"] = configuration
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.credential_key_metadata import CredentialKeyMetadata # noqa: PLC0415
        from ..models.form_answer_1 import FormAnswer1 # noqa: PLC0415
        d = dict(src_dict)
        key = d.pop("key")

        type_ = CredentialKeyType(d.pop("type"))




        _configuration = d.pop("configuration", UNSET)
        configuration: FormAnswer1 | Unset
        if isinstance(_configuration,  Unset):
            configuration = UNSET
        else:
            configuration = FormAnswer1.from_dict(_configuration)




        _metadata = d.pop("metadata", UNSET)
        metadata: CredentialKeyMetadata | Unset
        if isinstance(_metadata,  Unset):
            metadata = UNSET
        else:
            metadata = CredentialKeyMetadata.from_dict(_metadata)




        credential_key = cls(
            key=key,
            type_=type_,
            configuration=configuration,
            metadata=metadata,
        )

        return credential_key

