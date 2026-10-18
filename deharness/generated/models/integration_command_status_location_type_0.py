from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="IntegrationCommandStatusLocationType0")



@_attrs_define
class IntegrationCommandStatusLocationType0:
    """ 
        Attributes:
            directory (None | str | Unset):
     """

    directory: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        directory: None | str | Unset
        if isinstance(self.directory, Unset):
            directory = UNSET
        else:
            directory = self.directory


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if directory is not UNSET:
            field_dict["directory"] = directory

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_directory(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        directory = _parse_directory(d.pop("directory", UNSET))


        integration_command_status_location_type_0 = cls(
            directory=directory,
        )

        return integration_command_status_location_type_0

