from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.session_info import SessionInfo
  from ..models.sessions_response_cursor import SessionsResponseCursor





T = TypeVar("T", bound="SessionsResponse")



@_attrs_define
class SessionsResponse:
    """ 
        Attributes:
            cursor (SessionsResponseCursor):
            data (list[SessionInfo]):
     """

    cursor: SessionsResponseCursor
    data: list[SessionInfo]





    def to_dict(self) -> dict[str, Any]:
        from ..models.session_info import SessionInfo # noqa: PLC0415
        from ..models.sessions_response_cursor import SessionsResponseCursor # noqa: PLC0415
        cursor = self.cursor.to_dict()

        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "cursor": cursor,
            "data": data,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.session_info import SessionInfo # noqa: PLC0415
        from ..models.sessions_response_cursor import SessionsResponseCursor # noqa: PLC0415
        d = dict(src_dict)
        cursor = SessionsResponseCursor.from_dict(d.pop("cursor"))




        data = []
        _data = d.pop("data")
        for data_item_data in (_data):
            data_item = SessionInfo.from_dict(data_item_data)



            data.append(data_item)


        sessions_response = cls(
            cursor=cursor,
            data=data,
        )

        return sessions_response

