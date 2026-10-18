from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="SessionShellBody")



@_attrs_define
class SessionShellBody:
    """ 
        Attributes:
            command (str):
            id (None | str | Unset):
     """

    command: str
    id: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        command = self.command

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "command": command,
        })
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        command = d.pop("command")

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))


        session_shell_body = cls(
            command=command,
            id=id,
        )

        return session_shell_body

