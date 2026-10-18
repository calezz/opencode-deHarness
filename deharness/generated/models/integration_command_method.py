from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.integration_command_method_type import IntegrationCommandMethodType
from typing import cast






T = TypeVar("T", bound="IntegrationCommandMethod")



@_attrs_define
class IntegrationCommandMethod:
    """ 
        Attributes:
            command (list[str]):
            id (str):
            label (str):
            type_ (IntegrationCommandMethodType):
     """

    command: list[str]
    id: str
    label: str
    type_: IntegrationCommandMethodType





    def to_dict(self) -> dict[str, Any]:
        command = self.command



        id = self.id

        label = self.label

        type_ = self.type_.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "command": command,
            "id": id,
            "label": label,
            "type": type_,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        command = cast(list[str], d.pop("command"))


        id = d.pop("id")

        label = d.pop("label")

        type_ = IntegrationCommandMethodType(d.pop("type"))




        integration_command_method = cls(
            command=command,
            id=id,
            label=label,
            type_=type_,
        )

        return integration_command_method

