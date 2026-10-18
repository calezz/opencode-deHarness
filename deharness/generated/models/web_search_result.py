from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.web_search_result_time import WebSearchResultTime





T = TypeVar("T", bound="WebSearchResult")



@_attrs_define
class WebSearchResult:
    """ 
        Attributes:
            time (WebSearchResultTime):
            url (str):
            content (str | Unset):
            title (str | Unset):
     """

    time: WebSearchResultTime
    url: str
    content: str | Unset = UNSET
    title: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.web_search_result_time import WebSearchResultTime # noqa: PLC0415
        time = self.time.to_dict()

        url = self.url

        content = self.content

        title = self.title


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "time": time,
            "url": url,
        })
        if content is not UNSET:
            field_dict["content"] = content
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.web_search_result_time import WebSearchResultTime # noqa: PLC0415
        d = dict(src_dict)
        time = WebSearchResultTime.from_dict(d.pop("time"))




        url = d.pop("url")

        content = d.pop("content", UNSET)

        title = d.pop("title", UNSET)

        web_search_result = cls(
            time=time,
            url=url,
            content=content,
            title=title,
        )

        return web_search_result

