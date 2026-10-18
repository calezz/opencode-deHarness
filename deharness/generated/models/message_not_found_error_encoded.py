from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.message_not_found_error_encoded_tag import MessageNotFoundErrorEncodedTag






T = TypeVar("T", bound="MessageNotFoundErrorEncoded")



@_attrs_define
class MessageNotFoundErrorEncoded:
    """ 
        Attributes:
            field_tag (MessageNotFoundErrorEncodedTag):
            message (str):
            message_id (str):
            session_id (str):
     """

    field_tag: MessageNotFoundErrorEncodedTag
    message: str
    message_id: str
    session_id: str





    def to_dict(self) -> dict[str, Any]:
        field_tag = self.field_tag.value

        message = self.message

        message_id = self.message_id

        session_id = self.session_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "_tag": field_tag,
            "message": message,
            "messageID": message_id,
            "sessionID": session_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_tag = MessageNotFoundErrorEncodedTag(d.pop("_tag"))




        message = d.pop("message")

        message_id = d.pop("messageID")

        session_id = d.pop("sessionID")

        message_not_found_error_encoded = cls(
            field_tag=field_tag,
            message=message,
            message_id=message_id,
            session_id=session_id,
        )

        return message_not_found_error_encoded

