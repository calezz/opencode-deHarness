from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.config_formatter_entry_encoded_environment import ConfigFormatterEntryEncodedEnvironment





T = TypeVar("T", bound="ConfigFormatterEntryEncoded")



@_attrs_define
class ConfigFormatterEntryEncoded:
    """ 
        Attributes:
            command (list[str] | Unset):
            disabled (bool | Unset):
            environment (ConfigFormatterEntryEncodedEnvironment | Unset):
            extensions (list[str] | Unset):
     """

    command: list[str] | Unset = UNSET
    disabled: bool | Unset = UNSET
    environment: ConfigFormatterEntryEncodedEnvironment | Unset = UNSET
    extensions: list[str] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.config_formatter_entry_encoded_environment import ConfigFormatterEntryEncodedEnvironment # noqa: PLC0415
        command: list[str] | Unset = UNSET
        if not isinstance(self.command, Unset):
            command = self.command



        disabled = self.disabled

        environment: dict[str, Any] | Unset = UNSET
        if not isinstance(self.environment, Unset):
            environment = self.environment.to_dict()

        extensions: list[str] | Unset = UNSET
        if not isinstance(self.extensions, Unset):
            extensions = self.extensions




        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if command is not UNSET:
            field_dict["command"] = command
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if environment is not UNSET:
            field_dict["environment"] = environment
        if extensions is not UNSET:
            field_dict["extensions"] = extensions

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.config_formatter_entry_encoded_environment import ConfigFormatterEntryEncodedEnvironment # noqa: PLC0415
        d = dict(src_dict)
        command = cast(list[str], d.pop("command", UNSET))


        disabled = d.pop("disabled", UNSET)

        _environment = d.pop("environment", UNSET)
        environment: ConfigFormatterEntryEncodedEnvironment | Unset
        if isinstance(_environment,  Unset):
            environment = UNSET
        else:
            environment = ConfigFormatterEntryEncodedEnvironment.from_dict(_environment)




        extensions = cast(list[str], d.pop("extensions", UNSET))


        config_formatter_entry_encoded = cls(
            command=command,
            disabled=disabled,
            environment=environment,
            extensions=extensions,
        )

        return config_formatter_entry_encoded

