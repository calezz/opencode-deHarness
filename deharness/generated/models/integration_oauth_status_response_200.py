from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.integration_attempt_status_type_0 import IntegrationAttemptStatusType0
  from ..models.integration_attempt_status_type_1 import IntegrationAttemptStatusType1
  from ..models.integration_attempt_status_type_2 import IntegrationAttemptStatusType2
  from ..models.integration_attempt_status_type_3 import IntegrationAttemptStatusType3
  from ..models.location_public_ref import LocationPublicRef





T = TypeVar("T", bound="IntegrationOauthStatusResponse200")



@_attrs_define
class IntegrationOauthStatusResponse200:
    """ 
        Attributes:
            data (IntegrationAttemptStatusType0 | IntegrationAttemptStatusType1 | IntegrationAttemptStatusType2 |
                IntegrationAttemptStatusType3):
            location (LocationPublicRef):
     """

    data: IntegrationAttemptStatusType0 | IntegrationAttemptStatusType1 | IntegrationAttemptStatusType2 | IntegrationAttemptStatusType3
    location: LocationPublicRef





    def to_dict(self) -> dict[str, Any]:
        from ..models.integration_attempt_status_type_0 import IntegrationAttemptStatusType0 # noqa: PLC0415
        from ..models.integration_attempt_status_type_1 import IntegrationAttemptStatusType1 # noqa: PLC0415
        from ..models.integration_attempt_status_type_2 import IntegrationAttemptStatusType2 # noqa: PLC0415
        from ..models.integration_attempt_status_type_3 import IntegrationAttemptStatusType3 # noqa: PLC0415
        from ..models.location_public_ref import LocationPublicRef # noqa: PLC0415
        data: dict[str, Any]
        if isinstance(self.data, IntegrationAttemptStatusType0):
            data = self.data.to_dict()
        elif isinstance(self.data, IntegrationAttemptStatusType1):
            data = self.data.to_dict()
        elif isinstance(self.data, IntegrationAttemptStatusType2):
            data = self.data.to_dict()
        else:
            data = self.data.to_dict()


        location = self.location.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "data": data,
            "location": location,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.integration_attempt_status_type_0 import IntegrationAttemptStatusType0 # noqa: PLC0415
        from ..models.integration_attempt_status_type_1 import IntegrationAttemptStatusType1 # noqa: PLC0415
        from ..models.integration_attempt_status_type_2 import IntegrationAttemptStatusType2 # noqa: PLC0415
        from ..models.integration_attempt_status_type_3 import IntegrationAttemptStatusType3 # noqa: PLC0415
        from ..models.location_public_ref import LocationPublicRef # noqa: PLC0415
        d = dict(src_dict)
        def _parse_data(data: object) -> IntegrationAttemptStatusType0 | IntegrationAttemptStatusType1 | IntegrationAttemptStatusType2 | IntegrationAttemptStatusType3:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_integration_attempt_status_type_0 = IntegrationAttemptStatusType0.from_dict(data)



                return componentsschemas_integration_attempt_status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_integration_attempt_status_type_1 = IntegrationAttemptStatusType1.from_dict(data)



                return componentsschemas_integration_attempt_status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_integration_attempt_status_type_2 = IntegrationAttemptStatusType2.from_dict(data)



                return componentsschemas_integration_attempt_status_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_integration_attempt_status_type_3 = IntegrationAttemptStatusType3.from_dict(data)



            return componentsschemas_integration_attempt_status_type_3

        data = _parse_data(d.pop("data"))


        location = LocationPublicRef.from_dict(d.pop("location"))




        integration_oauth_status_response_200 = cls(
            data=data,
            location=location,
        )

        return integration_oauth_status_response_200

