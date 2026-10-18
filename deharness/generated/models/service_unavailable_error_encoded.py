from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.service_unavailable_error_encoded_tag import ServiceUnavailableErrorEncodedTag
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ServiceUnavailableErrorEncoded")



@_attrs_define
class ServiceUnavailableErrorEncoded:
    """ 
        Attributes:
            field_tag (ServiceUnavailableErrorEncodedTag):
            message (str):
            service (None | str | Unset):
     """

    field_tag: ServiceUnavailableErrorEncodedTag
    message: str
    service: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        field_tag = self.field_tag.value

        message = self.message

        service: None | str | Unset
        if isinstance(self.service, Unset):
            service = UNSET
        else:
            service = self.service


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "_tag": field_tag,
            "message": message,
        })
        if service is not UNSET:
            field_dict["service"] = service

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_tag = ServiceUnavailableErrorEncodedTag(d.pop("_tag"))




        message = d.pop("message")

        def _parse_service(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        service = _parse_service(d.pop("service", UNSET))


        service_unavailable_error_encoded = cls(
            field_tag=field_tag,
            message=message,
            service=service,
        )

        return service_unavailable_error_encoded

