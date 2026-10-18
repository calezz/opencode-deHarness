from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="WebsearchQueryBody")



@_attrs_define
class WebsearchQueryBody:
    """ 
        Attributes:
            query (str):
            provider_id (str | Unset):
     """

    query: str
    provider_id: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        query = self.query

        provider_id = self.provider_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "query": query,
        })
        if provider_id is not UNSET:
            field_dict["providerID"] = provider_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        query = d.pop("query")

        provider_id = d.pop("providerID", UNSET)

        websearch_query_body = cls(
            query=query,
            provider_id=provider_id,
        )

        return websearch_query_body

