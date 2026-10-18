from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.mcp_status_disabled_status import McpStatusDisabledStatus






T = TypeVar("T", bound="McpStatusDisabled")



@_attrs_define
class McpStatusDisabled:
    """ 
        Attributes:
            status (McpStatusDisabledStatus):
     """

    status: McpStatusDisabledStatus





    def to_dict(self) -> dict[str, Any]:
        status = self.status.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "status": status,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = McpStatusDisabledStatus(d.pop("status"))




        mcp_status_disabled = cls(
            status=status,
        )

        return mcp_status_disabled

