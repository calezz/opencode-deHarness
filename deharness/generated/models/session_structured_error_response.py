from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="SessionStructuredErrorResponse")



@_attrs_define
class SessionStructuredErrorResponse:
    """ 
        Attributes:
            body (str):
     """

    body: str





    def to_dict(self) -> dict[str, Any]:
        body = self.body


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "body": body,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        body = d.pop("body")

        session_structured_error_response = cls(
            body=body,
        )

        return session_structured_error_response

