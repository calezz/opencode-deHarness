from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.integration_attempt_not_found_error_encoded_tag import IntegrationAttemptNotFoundErrorEncodedTag






T = TypeVar("T", bound="IntegrationAttemptNotFoundErrorEncoded")



@_attrs_define
class IntegrationAttemptNotFoundErrorEncoded:
    """ 
        Attributes:
            field_tag (IntegrationAttemptNotFoundErrorEncodedTag):
            attempt_id (str):
            integration_id (str):
            message (str):
     """

    field_tag: IntegrationAttemptNotFoundErrorEncodedTag
    attempt_id: str
    integration_id: str
    message: str





    def to_dict(self) -> dict[str, Any]:
        field_tag = self.field_tag.value

        attempt_id = self.attempt_id

        integration_id = self.integration_id

        message = self.message


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "_tag": field_tag,
            "attemptID": attempt_id,
            "integrationID": integration_id,
            "message": message,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_tag = IntegrationAttemptNotFoundErrorEncodedTag(d.pop("_tag"))




        attempt_id = d.pop("attemptID")

        integration_id = d.pop("integrationID")

        message = d.pop("message")

        integration_attempt_not_found_error_encoded = cls(
            field_tag=field_tag,
            attempt_id=attempt_id,
            integration_id=integration_id,
            message=message,
        )

        return integration_attempt_not_found_error_encoded

