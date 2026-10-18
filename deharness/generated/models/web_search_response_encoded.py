from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.web_search_result import WebSearchResult





T = TypeVar("T", bound="WebSearchResponseEncoded")



@_attrs_define
class WebSearchResponseEncoded:
    """ 
        Attributes:
            provider_id (str):
            results (list[WebSearchResult]):
     """

    provider_id: str
    results: list[WebSearchResult]





    def to_dict(self) -> dict[str, Any]:
        from ..models.web_search_result import WebSearchResult # noqa: PLC0415
        provider_id = self.provider_id

        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "providerID": provider_id,
            "results": results,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.web_search_result import WebSearchResult # noqa: PLC0415
        d = dict(src_dict)
        provider_id = d.pop("providerID")

        results = []
        _results = d.pop("results")
        for results_item_data in (_results):
            results_item = WebSearchResult.from_dict(results_item_data)



            results.append(results_item)


        web_search_response_encoded = cls(
            provider_id=provider_id,
            results=results,
        )

        return web_search_response_encoded

