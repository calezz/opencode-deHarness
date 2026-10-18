from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.persistent_pty_handoff_expires_at_type_1 import PersistentPtyHandoffExpiresAtType1
from typing import cast






T = TypeVar("T", bound="PersistentPtyHandoff")



@_attrs_define
class PersistentPtyHandoff:
    """ 
        Attributes:
            directory (str):
            expires_at (float | PersistentPtyHandoffExpiresAtType1):
            instance_id (str):
            ticket (str):
     """

    directory: str
    expires_at: float | PersistentPtyHandoffExpiresAtType1
    instance_id: str
    ticket: str





    def to_dict(self) -> dict[str, Any]:
        directory = self.directory

        expires_at: float | str
        if isinstance(self.expires_at, PersistentPtyHandoffExpiresAtType1):
            expires_at = self.expires_at.value
        else:
            expires_at = self.expires_at

        instance_id = self.instance_id

        ticket = self.ticket


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "directory": directory,
            "expiresAt": expires_at,
            "instanceID": instance_id,
            "ticket": ticket,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        directory = d.pop("directory")

        def _parse_expires_at(data: object) -> float | PersistentPtyHandoffExpiresAtType1:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_at_type_1 = PersistentPtyHandoffExpiresAtType1(data)



                return expires_at_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(float | PersistentPtyHandoffExpiresAtType1, data)

        expires_at = _parse_expires_at(d.pop("expiresAt"))


        instance_id = d.pop("instanceID")

        ticket = d.pop("ticket")

        persistent_pty_handoff = cls(
            directory=directory,
            expires_at=expires_at,
            instance_id=instance_id,
            ticket=ticket,
        )

        return persistent_pty_handoff

