from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ConfigInfoEncodedWatcher")



@_attrs_define
class ConfigInfoEncodedWatcher:
    """ 
        Attributes:
            ignore (list[str] | Unset):
     """

    ignore: list[str] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        ignore: list[str] | Unset = UNSET
        if not isinstance(self.ignore, Unset):
            ignore = self.ignore




        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if ignore is not UNSET:
            field_dict["ignore"] = ignore

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ignore = cast(list[str], d.pop("ignore", UNSET))


        config_info_encoded_watcher = cls(
            ignore=ignore,
        )

        return config_info_encoded_watcher

