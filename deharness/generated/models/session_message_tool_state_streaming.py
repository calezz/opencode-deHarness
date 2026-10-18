from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.session_message_tool_state_streaming_status import SessionMessageToolStateStreamingStatus






T = TypeVar("T", bound="SessionMessageToolStateStreaming")



@_attrs_define
class SessionMessageToolStateStreaming:
    """ 
        Attributes:
            input_ (str):
            status (SessionMessageToolStateStreamingStatus):
     """

    input_: str
    status: SessionMessageToolStateStreamingStatus





    def to_dict(self) -> dict[str, Any]:
        input_ = self.input_

        status = self.status.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "input": input_,
            "status": status,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        input_ = d.pop("input")

        status = SessionMessageToolStateStreamingStatus(d.pop("status"))




        session_message_tool_state_streaming = cls(
            input_=input_,
            status=status,
        )

        return session_message_tool_state_streaming

