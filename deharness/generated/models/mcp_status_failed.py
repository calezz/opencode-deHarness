from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.mcp_status_failed_status import McpStatusFailedStatus






T = TypeVar("T", bound="McpStatusFailed")



@_attrs_define
class McpStatusFailed:
    """ 
        Attributes:
            error (str):
            status (McpStatusFailedStatus):
     """

    error: str
    status: McpStatusFailedStatus





    def to_dict(self) -> dict[str, Any]:
        error = self.error

        status = self.status.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "error": error,
            "status": status,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        error = d.pop("error")

        status = McpStatusFailedStatus(d.pop("status"))




        mcp_status_failed = cls(
            error=error,
            status=status,
        )

        return mcp_status_failed

