from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="WebSearchResultTime")



@_attrs_define
class WebSearchResultTime:
    """ 
        Attributes:
            published (float | Unset):
     """

    published: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        published = self.published


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if published is not UNSET:
            field_dict["published"] = published

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        published = d.pop("published", UNSET)

        web_search_result_time = cls(
            published=published,
        )

        return web_search_result_time

