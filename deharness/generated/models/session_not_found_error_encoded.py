from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.session_not_found_error_encoded_tag import SessionNotFoundErrorEncodedTag






T = TypeVar("T", bound="SessionNotFoundErrorEncoded")



@_attrs_define
class SessionNotFoundErrorEncoded:
    """ 
        Attributes:
            field_tag (SessionNotFoundErrorEncodedTag):
            message (str):
            session_id (str):
     """

    field_tag: SessionNotFoundErrorEncodedTag
    message: str
    session_id: str





    def to_dict(self) -> dict[str, Any]:
        field_tag = self.field_tag.value

        message = self.message

        session_id = self.session_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "_tag": field_tag,
            "message": message,
            "sessionID": session_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_tag = SessionNotFoundErrorEncodedTag(d.pop("_tag"))




        message = d.pop("message")

        session_id = d.pop("sessionID")

        session_not_found_error_encoded = cls(
            field_tag=field_tag,
            message=message,
            session_id=session_id,
        )

        return session_not_found_error_encoded

