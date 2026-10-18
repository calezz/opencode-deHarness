from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.mcp_status_connected import McpStatusConnected
  from ..models.mcp_status_disabled import McpStatusDisabled
  from ..models.mcp_status_failed import McpStatusFailed
  from ..models.mcp_status_needs_auth import McpStatusNeedsAuth
  from ..models.mcp_status_pending import McpStatusPending





T = TypeVar("T", bound="McpServer")



@_attrs_define
class McpServer:
    """ 
        Attributes:
            name (str):
            status (McpStatusConnected | McpStatusDisabled | McpStatusFailed | McpStatusNeedsAuth | McpStatusPending):
            integration_id (str | Unset):
     """

    name: str
    status: McpStatusConnected | McpStatusDisabled | McpStatusFailed | McpStatusNeedsAuth | McpStatusPending
    integration_id: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.mcp_status_connected import McpStatusConnected # noqa: PLC0415
        from ..models.mcp_status_disabled import McpStatusDisabled # noqa: PLC0415
        from ..models.mcp_status_failed import McpStatusFailed # noqa: PLC0415
        from ..models.mcp_status_needs_auth import McpStatusNeedsAuth # noqa: PLC0415
        from ..models.mcp_status_pending import McpStatusPending # noqa: PLC0415
        name = self.name

        status: dict[str, Any]
        if isinstance(self.status, McpStatusConnected):
            status = self.status.to_dict()
        elif isinstance(self.status, McpStatusPending):
            status = self.status.to_dict()
        elif isinstance(self.status, McpStatusDisabled):
            status = self.status.to_dict()
        elif isinstance(self.status, McpStatusFailed):
            status = self.status.to_dict()
        else:
            status = self.status.to_dict()


        integration_id = self.integration_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "name": name,
            "status": status,
        })
        if integration_id is not UNSET:
            field_dict["integrationID"] = integration_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mcp_status_connected import McpStatusConnected # noqa: PLC0415
        from ..models.mcp_status_disabled import McpStatusDisabled # noqa: PLC0415
        from ..models.mcp_status_failed import McpStatusFailed # noqa: PLC0415
        from ..models.mcp_status_needs_auth import McpStatusNeedsAuth # noqa: PLC0415
        from ..models.mcp_status_pending import McpStatusPending # noqa: PLC0415
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_status(data: object) -> McpStatusConnected | McpStatusDisabled | McpStatusFailed | McpStatusNeedsAuth | McpStatusPending:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                status_type_0 = McpStatusConnected.from_dict(data)



                return status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                status_type_1 = McpStatusPending.from_dict(data)



                return status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                status_type_2 = McpStatusDisabled.from_dict(data)



                return status_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                status_type_3 = McpStatusFailed.from_dict(data)



                return status_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            status_type_4 = McpStatusNeedsAuth.from_dict(data)



            return status_type_4

        status = _parse_status(d.pop("status"))


        integration_id = d.pop("integrationID", UNSET)

        mcp_server = cls(
            name=name,
            status=status,
            integration_id=integration_id,
        )

        return mcp_server

