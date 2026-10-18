from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.invalid_request_error_encoded_tag import InvalidRequestErrorEncodedTag
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="InvalidRequestErrorEncoded")



@_attrs_define
class InvalidRequestErrorEncoded:
    """ 
        Attributes:
            field_tag (InvalidRequestErrorEncodedTag):
            message (str):
            field (None | str | Unset):
            kind (None | str | Unset):
     """

    field_tag: InvalidRequestErrorEncodedTag
    message: str
    field: None | str | Unset = UNSET
    kind: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        field_tag = self.field_tag.value

        message = self.message

        field: None | str | Unset
        if isinstance(self.field, Unset):
            field = UNSET
        else:
            field = self.field

        kind: None | str | Unset
        if isinstance(self.kind, Unset):
            kind = UNSET
        else:
            kind = self.kind


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "_tag": field_tag,
            "message": message,
        })
        if field is not UNSET:
            field_dict["field"] = field
        if kind is not UNSET:
            field_dict["kind"] = kind

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_tag = InvalidRequestErrorEncodedTag(d.pop("_tag"))




        message = d.pop("message")

        def _parse_field(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        field = _parse_field(d.pop("field", UNSET))


        def _parse_kind(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        kind = _parse_kind(d.pop("kind", UNSET))


        invalid_request_error_encoded = cls(
            field_tag=field_tag,
            message=message,
            field=field,
            kind=kind,
        )

        return invalid_request_error_encoded

