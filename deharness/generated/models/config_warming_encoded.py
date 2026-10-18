from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ConfigWarmingEncoded")



@_attrs_define
class ConfigWarmingEncoded:
    """ 
        Attributes:
            duration (str | Unset):
            interval (str | Unset):
            prompt (str | Unset):
     """

    duration: str | Unset = UNSET
    interval: str | Unset = UNSET
    prompt: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        duration = self.duration

        interval = self.interval

        prompt = self.prompt


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if duration is not UNSET:
            field_dict["duration"] = duration
        if interval is not UNSET:
            field_dict["interval"] = interval
        if prompt is not UNSET:
            field_dict["prompt"] = prompt

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        duration = d.pop("duration", UNSET)

        interval = d.pop("interval", UNSET)

        prompt = d.pop("prompt", UNSET)

        config_warming_encoded = cls(
            duration=duration,
            interval=interval,
            prompt=prompt,
        )

        return config_warming_encoded

