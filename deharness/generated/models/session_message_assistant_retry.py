from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.session_structured_error import SessionStructuredError





T = TypeVar("T", bound="SessionMessageAssistantRetry")



@_attrs_define
class SessionMessageAssistantRetry:
    """ 
        Attributes:
            at (float):
            attempt (int):
            error (SessionStructuredError):
     """

    at: float
    attempt: int
    error: SessionStructuredError





    def to_dict(self) -> dict[str, Any]:
        from ..models.session_structured_error import SessionStructuredError # noqa: PLC0415
        at = self.at

        attempt = self.attempt

        error = self.error.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "at": at,
            "attempt": attempt,
            "error": error,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.session_structured_error import SessionStructuredError # noqa: PLC0415
        d = dict(src_dict)
        at = d.pop("at")

        attempt = d.pop("attempt")

        error = SessionStructuredError.from_dict(d.pop("error"))




        session_message_assistant_retry = cls(
            at=at,
            attempt=attempt,
            error=error,
        )

        return session_message_assistant_retry

