from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.integration_command_attempt_time import IntegrationCommandAttemptTime





T = TypeVar("T", bound="IntegrationCommandAttempt")



@_attrs_define
class IntegrationCommandAttempt:
    """ 
        Attributes:
            attempt_id (str):
            time (IntegrationCommandAttemptTime):
     """

    attempt_id: str
    time: IntegrationCommandAttemptTime





    def to_dict(self) -> dict[str, Any]:
        from ..models.integration_command_attempt_time import IntegrationCommandAttemptTime # noqa: PLC0415
        attempt_id = self.attempt_id

        time = self.time.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "attemptID": attempt_id,
            "time": time,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.integration_command_attempt_time import IntegrationCommandAttemptTime # noqa: PLC0415
        d = dict(src_dict)
        attempt_id = d.pop("attemptID")

        time = IntegrationCommandAttemptTime.from_dict(d.pop("time"))




        integration_command_attempt = cls(
            attempt_id=attempt_id,
            time=time,
        )

        return integration_command_attempt

