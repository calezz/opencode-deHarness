from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.pty_not_found_error_encoded_tag import PtyNotFoundErrorEncodedTag






T = TypeVar("T", bound="PtyNotFoundErrorEncoded")



@_attrs_define
class PtyNotFoundErrorEncoded:
    """ 
        Attributes:
            field_tag (PtyNotFoundErrorEncodedTag):
            message (str):
            pty_id (str):
     """

    field_tag: PtyNotFoundErrorEncodedTag
    message: str
    pty_id: str





    def to_dict(self) -> dict[str, Any]:
        field_tag = self.field_tag.value

        message = self.message

        pty_id = self.pty_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "_tag": field_tag,
            "message": message,
            "ptyID": pty_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_tag = PtyNotFoundErrorEncodedTag(d.pop("_tag"))




        message = d.pop("message")

        pty_id = d.pop("ptyID")

        pty_not_found_error_encoded = cls(
            field_tag=field_tag,
            message=message,
            pty_id=pty_id,
        )

        return pty_not_found_error_encoded

