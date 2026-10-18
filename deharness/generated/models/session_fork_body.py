from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="SessionForkBody")



@_attrs_define
class SessionForkBody:
    """ 
        Attributes:
            before (None | str | Unset):
     """

    before: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        before: None | str | Unset
        if isinstance(self.before, Unset):
            before = UNSET
        else:
            before = self.before


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if before is not UNSET:
            field_dict["before"] = before

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_before(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        before = _parse_before(d.pop("before", UNSET))


        session_fork_body = cls(
            before=before,
        )

        return session_fork_body

