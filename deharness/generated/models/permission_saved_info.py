from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.permission_saved_info_time import PermissionSavedInfoTime





T = TypeVar("T", bound="PermissionSavedInfo")



@_attrs_define
class PermissionSavedInfo:
    """ 
        Attributes:
            action (str):
            id (str):
            project_id (str):
            resource (str):
            time (PermissionSavedInfoTime):
     """

    action: str
    id: str
    project_id: str
    resource: str
    time: PermissionSavedInfoTime





    def to_dict(self) -> dict[str, Any]:
        from ..models.permission_saved_info_time import PermissionSavedInfoTime # noqa: PLC0415
        action = self.action

        id = self.id

        project_id = self.project_id

        resource = self.resource

        time = self.time.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "action": action,
            "id": id,
            "projectID": project_id,
            "resource": resource,
            "time": time,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.permission_saved_info_time import PermissionSavedInfoTime # noqa: PLC0415
        d = dict(src_dict)
        action = d.pop("action")

        id = d.pop("id")

        project_id = d.pop("projectID")

        resource = d.pop("resource")

        time = PermissionSavedInfoTime.from_dict(d.pop("time"))




        permission_saved_info = cls(
            action=action,
            id=id,
            project_id=project_id,
            resource=resource,
            time=time,
        )

        return permission_saved_info

