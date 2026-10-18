from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.command_not_found_error_encoded_tag import CommandNotFoundErrorEncodedTag






T = TypeVar("T", bound="CommandNotFoundErrorEncoded")



@_attrs_define
class CommandNotFoundErrorEncoded:
    """ 
        Attributes:
            field_tag (CommandNotFoundErrorEncodedTag):
            command (str):
            message (str):
     """

    field_tag: CommandNotFoundErrorEncodedTag
    command: str
    message: str





    def to_dict(self) -> dict[str, Any]:
        field_tag = self.field_tag.value

        command = self.command

        message = self.message


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "_tag": field_tag,
            "command": command,
            "message": message,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_tag = CommandNotFoundErrorEncodedTag(d.pop("_tag"))




        command = d.pop("command")

        message = d.pop("message")

        command_not_found_error_encoded = cls(
            field_tag=field_tag,
            command=command,
            message=message,
        )

        return command_not_found_error_encoded

