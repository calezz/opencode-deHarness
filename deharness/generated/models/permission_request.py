from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.permission_request_metadata import PermissionRequestMetadata
  from ..models.permission_source_type_0 import PermissionSourceType0





T = TypeVar("T", bound="PermissionRequest")



@_attrs_define
class PermissionRequest:
    """ 
        Attributes:
            action (str):
            id (str):
            resources (list[str]):
            session_id (str):
            message (str | Unset):
            metadata (PermissionRequestMetadata | Unset):
            save (list[str] | Unset):
            source (PermissionSourceType0 | Unset):
     """

    action: str
    id: str
    resources: list[str]
    session_id: str
    message: str | Unset = UNSET
    metadata: PermissionRequestMetadata | Unset = UNSET
    save: list[str] | Unset = UNSET
    source: PermissionSourceType0 | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.permission_request_metadata import PermissionRequestMetadata # noqa: PLC0415
        from ..models.permission_source_type_0 import PermissionSourceType0 # noqa: PLC0415
        action = self.action

        id = self.id

        resources = self.resources



        session_id = self.session_id

        message = self.message

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        save: list[str] | Unset = UNSET
        if not isinstance(self.save, Unset):
            save = self.save



        source: dict[str, Any] | Unset
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source.to_dict()



        field_dict: dict[str, Any] = {}

        field_dict.update({
            "action": action,
            "id": id,
            "resources": resources,
            "sessionID": session_id,
        })
        if message is not UNSET:
            field_dict["message"] = message
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if save is not UNSET:
            field_dict["save"] = save
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.permission_request_metadata import PermissionRequestMetadata # noqa: PLC0415
        from ..models.permission_source_type_0 import PermissionSourceType0 # noqa: PLC0415
        d = dict(src_dict)
        action = d.pop("action")

        id = d.pop("id")

        resources = cast(list[str], d.pop("resources"))


        session_id = d.pop("sessionID")

        message = d.pop("message", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: PermissionRequestMetadata | Unset
        if isinstance(_metadata,  Unset):
            metadata = UNSET
        else:
            metadata = PermissionRequestMetadata.from_dict(_metadata)




        save = cast(list[str], d.pop("save", UNSET))


        def _parse_source(data: object) -> PermissionSourceType0 | Unset:
            if isinstance(data, Unset):
                return data
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_permission_source_type_0 = PermissionSourceType0.from_dict(data)



            return componentsschemas_permission_source_type_0

        source = _parse_source(d.pop("source", UNSET))


        permission_request = cls(
            action=action,
            id=id,
            resources=resources,
            session_id=session_id,
            message=message,
            metadata=metadata,
            save=save,
            source=source,
        )

        return permission_request

