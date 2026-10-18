from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.credential_external import CredentialExternal
  from ..models.credential_key import CredentialKey
  from ..models.credential_o_auth import CredentialOAuth





T = TypeVar("T", bound="CredentialCreateInput")



@_attrs_define
class CredentialCreateInput:
    """ 
        Attributes:
            integration_id (str):
            value (CredentialExternal | CredentialKey | CredentialOAuth):
            activate (bool | Unset):
            id (str | Unset):
            label (str | Unset):
     """

    integration_id: str
    value: CredentialExternal | CredentialKey | CredentialOAuth
    activate: bool | Unset = UNSET
    id: str | Unset = UNSET
    label: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.credential_external import CredentialExternal # noqa: PLC0415
        from ..models.credential_key import CredentialKey # noqa: PLC0415
        from ..models.credential_o_auth import CredentialOAuth # noqa: PLC0415
        integration_id = self.integration_id

        value: dict[str, Any]
        if isinstance(self.value, CredentialOAuth):
            value = self.value.to_dict()
        elif isinstance(self.value, CredentialKey):
            value = self.value.to_dict()
        else:
            value = self.value.to_dict()


        activate = self.activate

        id = self.id

        label = self.label


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "integrationID": integration_id,
            "value": value,
        })
        if activate is not UNSET:
            field_dict["activate"] = activate
        if id is not UNSET:
            field_dict["id"] = id
        if label is not UNSET:
            field_dict["label"] = label

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.credential_external import CredentialExternal # noqa: PLC0415
        from ..models.credential_key import CredentialKey # noqa: PLC0415
        from ..models.credential_o_auth import CredentialOAuth # noqa: PLC0415
        d = dict(src_dict)
        integration_id = d.pop("integrationID")

        def _parse_value(data: object) -> CredentialExternal | CredentialKey | CredentialOAuth:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_credential_value_type_0 = CredentialOAuth.from_dict(data)



                return componentsschemas_credential_value_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_credential_value_type_1 = CredentialKey.from_dict(data)



                return componentsschemas_credential_value_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_credential_value_type_2 = CredentialExternal.from_dict(data)



            return componentsschemas_credential_value_type_2

        value = _parse_value(d.pop("value"))


        activate = d.pop("activate", UNSET)

        id = d.pop("id", UNSET)

        label = d.pop("label", UNSET)

        credential_create_input = cls(
            integration_id=integration_id,
            value=value,
            activate=activate,
            id=id,
            label=label,
        )

        return credential_create_input

