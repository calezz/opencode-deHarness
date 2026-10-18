from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.conflict_error_encoded_tag import ConflictErrorEncodedTag
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ConflictErrorEncoded")



@_attrs_define
class ConflictErrorEncoded:
    """ 
        Attributes:
            field_tag (ConflictErrorEncodedTag):
            message (str):
            resource (None | str | Unset):
     """

    field_tag: ConflictErrorEncodedTag
    message: str
    resource: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        field_tag = self.field_tag.value

        message = self.message

        resource: None | str | Unset
        if isinstance(self.resource, Unset):
            resource = UNSET
        else:
            resource = self.resource


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "_tag": field_tag,
            "message": message,
        })
        if resource is not UNSET:
            field_dict["resource"] = resource

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_tag = ConflictErrorEncodedTag(d.pop("_tag"))




        message = d.pop("message")

        def _parse_resource(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource = _parse_resource(d.pop("resource", UNSET))


        conflict_error_encoded = cls(
            field_tag=field_tag,
            message=message,
            resource=resource,
        )

        return conflict_error_encoded

