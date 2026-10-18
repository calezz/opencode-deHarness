from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.credential_external import CredentialExternal
  from ..models.credential_key import CredentialKey
  from ..models.credential_o_auth import CredentialOAuth





T = TypeVar("T", bound="CredentialEntry")



@_attrs_define
class CredentialEntry:
    """ 
        Attributes:
            active (bool):
            id (str):
            integration_id (str):
            label (str):
            value (CredentialExternal | CredentialKey | CredentialOAuth):
     """

    active: bool
    id: str
    integration_id: str
    label: str
    value: CredentialExternal | CredentialKey | CredentialOAuth





    def to_dict(self) -> dict[str, Any]:
        from ..models.credential_external import CredentialExternal # noqa: PLC0415
        from ..models.credential_key import CredentialKey # noqa: PLC0415
        from ..models.credential_o_auth import CredentialOAuth # noqa: PLC0415
        active = self.active

        id = self.id

        integration_id = self.integration_id

        label = self.label

        value: dict[str, Any]
        if isinstance(self.value, CredentialOAuth):
            value = self.value.to_dict()
        elif isinstance(self.value, CredentialKey):
            value = self.value.to_dict()
        else:
            value = self.value.to_dict()



        field_dict: dict[str, Any] = {}

        field_dict.update({
            "active": active,
            "id": id,
            "integrationID": integration_id,
            "label": label,
            "value": value,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.credential_external import CredentialExternal # noqa: PLC0415
        from ..models.credential_key import CredentialKey # noqa: PLC0415
        from ..models.credential_o_auth import CredentialOAuth # noqa: PLC0415
        d = dict(src_dict)
        active = d.pop("active")

        id = d.pop("id")

        integration_id = d.pop("integrationID")

        label = d.pop("label")

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


        credential_entry = cls(
            active=active,
            id=id,
            integration_id=integration_id,
            label=label,
            value=value,
        )

        return credential_entry

