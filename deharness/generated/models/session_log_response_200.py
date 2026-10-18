from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="SessionLogResponse200")



@_attrs_define
class SessionLogResponse200:
    """ 
        Attributes:
            data (str):
            event (str):
            id (None | str | Unset):
     """

    data: str
    event: str
    id: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        data = self.data

        event = self.event

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "data": data,
            "event": event,
        })
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        data = d.pop("data")

        event = d.pop("event")

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))


        session_log_response_200 = cls(
            data=data,
            event=event,
            id=id,
        )

        return session_log_response_200

