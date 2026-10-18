from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.permission_reply import PermissionReply
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="SessionPermissionReplyBody")



@_attrs_define
class SessionPermissionReplyBody:
    """ 
        Attributes:
            decision (PermissionReply):
            message (None | str | Unset):
     """

    decision: PermissionReply
    message: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        decision = self.decision.value

        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "decision": decision,
        })
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        decision = PermissionReply(d.pop("decision"))




        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))


        session_permission_reply_body = cls(
            decision=decision,
            message=message,
        )

        return session_permission_reply_body

