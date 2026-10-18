from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.integration_attempt_encoded_mode import IntegrationAttemptEncodedMode
from typing import cast

if TYPE_CHECKING:
  from ..models.integration_attempt_encoded_time import IntegrationAttemptEncodedTime





T = TypeVar("T", bound="IntegrationAttemptEncoded")



@_attrs_define
class IntegrationAttemptEncoded:
    """ 
        Attributes:
            attempt_id (str):
            instructions (str):
            mode (IntegrationAttemptEncodedMode):
            time (IntegrationAttemptEncodedTime):
            url (str):
     """

    attempt_id: str
    instructions: str
    mode: IntegrationAttemptEncodedMode
    time: IntegrationAttemptEncodedTime
    url: str





    def to_dict(self) -> dict[str, Any]:
        from ..models.integration_attempt_encoded_time import IntegrationAttemptEncodedTime # noqa: PLC0415
        attempt_id = self.attempt_id

        instructions = self.instructions

        mode = self.mode.value

        time = self.time.to_dict()

        url = self.url


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "attemptID": attempt_id,
            "instructions": instructions,
            "mode": mode,
            "time": time,
            "url": url,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.integration_attempt_encoded_time import IntegrationAttemptEncodedTime # noqa: PLC0415
        d = dict(src_dict)
        attempt_id = d.pop("attemptID")

        instructions = d.pop("instructions")

        mode = IntegrationAttemptEncodedMode(d.pop("mode"))




        time = IntegrationAttemptEncodedTime.from_dict(d.pop("time"))




        url = d.pop("url")

        integration_attempt_encoded = cls(
            attempt_id=attempt_id,
            instructions=instructions,
            mode=mode,
            time=time,
            url=url,
        )

        return integration_attempt_encoded

