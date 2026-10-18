from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.unknown_error_encoded_tag import UnknownErrorEncodedTag
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="UnknownErrorEncoded")



@_attrs_define
class UnknownErrorEncoded:
    """ 
        Attributes:
            field_tag (UnknownErrorEncodedTag):
            message (str):
            ref (None | str | Unset):
     """

    field_tag: UnknownErrorEncodedTag
    message: str
    ref: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        field_tag = self.field_tag.value

        message = self.message

        ref: None | str | Unset
        if isinstance(self.ref, Unset):
            ref = UNSET
        else:
            ref = self.ref


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "_tag": field_tag,
            "message": message,
        })
        if ref is not UNSET:
            field_dict["ref"] = ref

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_tag = UnknownErrorEncodedTag(d.pop("_tag"))




        message = d.pop("message")

        def _parse_ref(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ref = _parse_ref(d.pop("ref", UNSET))


        unknown_error_encoded = cls(
            field_tag=field_tag,
            message=message,
            ref=ref,
        )

        return unknown_error_encoded

