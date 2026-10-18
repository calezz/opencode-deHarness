from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.integration_attempt_encoded_time_created_type_1 import IntegrationAttemptEncodedTimeCreatedType1
from ..models.integration_attempt_encoded_time_expires_type_1 import IntegrationAttemptEncodedTimeExpiresType1
from typing import cast






T = TypeVar("T", bound="IntegrationAttemptEncodedTime")



@_attrs_define
class IntegrationAttemptEncodedTime:
    """ 
        Attributes:
            created (float | IntegrationAttemptEncodedTimeCreatedType1):
            expires (float | IntegrationAttemptEncodedTimeExpiresType1):
     """

    created: float | IntegrationAttemptEncodedTimeCreatedType1
    expires: float | IntegrationAttemptEncodedTimeExpiresType1





    def to_dict(self) -> dict[str, Any]:
        created: float | str
        if isinstance(self.created, IntegrationAttemptEncodedTimeCreatedType1):
            created = self.created.value
        else:
            created = self.created

        expires: float | str
        if isinstance(self.expires, IntegrationAttemptEncodedTimeExpiresType1):
            expires = self.expires.value
        else:
            expires = self.expires


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "created": created,
            "expires": expires,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_created(data: object) -> float | IntegrationAttemptEncodedTimeCreatedType1:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_type_1 = IntegrationAttemptEncodedTimeCreatedType1(data)



                return created_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(float | IntegrationAttemptEncodedTimeCreatedType1, data)

        created = _parse_created(d.pop("created"))


        def _parse_expires(data: object) -> float | IntegrationAttemptEncodedTimeExpiresType1:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_type_1 = IntegrationAttemptEncodedTimeExpiresType1(data)



                return expires_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(float | IntegrationAttemptEncodedTimeExpiresType1, data)

        expires = _parse_expires(d.pop("expires"))


        integration_attempt_encoded_time = cls(
            created=created,
            expires=expires,
        )

        return integration_attempt_encoded_time

