from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.integration_attempt_status_type_2_time_created_type_1 import IntegrationAttemptStatusType2TimeCreatedType1
from ..models.integration_attempt_status_type_2_time_expires_type_1 import IntegrationAttemptStatusType2TimeExpiresType1
from typing import cast






T = TypeVar("T", bound="IntegrationAttemptStatusType2Time")



@_attrs_define
class IntegrationAttemptStatusType2Time:
    """ 
        Attributes:
            created (float | IntegrationAttemptStatusType2TimeCreatedType1):
            expires (float | IntegrationAttemptStatusType2TimeExpiresType1):
     """

    created: float | IntegrationAttemptStatusType2TimeCreatedType1
    expires: float | IntegrationAttemptStatusType2TimeExpiresType1





    def to_dict(self) -> dict[str, Any]:
        created: float | str
        if isinstance(self.created, IntegrationAttemptStatusType2TimeCreatedType1):
            created = self.created.value
        else:
            created = self.created

        expires: float | str
        if isinstance(self.expires, IntegrationAttemptStatusType2TimeExpiresType1):
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
        def _parse_created(data: object) -> float | IntegrationAttemptStatusType2TimeCreatedType1:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_type_1 = IntegrationAttemptStatusType2TimeCreatedType1(data)



                return created_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(float | IntegrationAttemptStatusType2TimeCreatedType1, data)

        created = _parse_created(d.pop("created"))


        def _parse_expires(data: object) -> float | IntegrationAttemptStatusType2TimeExpiresType1:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_type_1 = IntegrationAttemptStatusType2TimeExpiresType1(data)



                return expires_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(float | IntegrationAttemptStatusType2TimeExpiresType1, data)

        expires = _parse_expires(d.pop("expires"))


        integration_attempt_status_type_2_time = cls(
            created=created,
            expires=expires,
        )

        return integration_attempt_status_type_2_time

