from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.permission_source_type_0 import PermissionSourceType0
  from ..models.session_permission_create_body_metadata import SessionPermissionCreateBodyMetadata





T = TypeVar("T", bound="SessionPermissionCreateBody")



@_attrs_define
class SessionPermissionCreateBody:
    """ 
        Attributes:
            action (str):
            resources (list[str]):
            agent (None | str | Unset):
            id (None | str | Unset):
            metadata (SessionPermissionCreateBodyMetadata | Unset):
            save (list[str] | Unset):
            source (PermissionSourceType0 | Unset):
     """

    action: str
    resources: list[str]
    agent: None | str | Unset = UNSET
    id: None | str | Unset = UNSET
    metadata: SessionPermissionCreateBodyMetadata | Unset = UNSET
    save: list[str] | Unset = UNSET
    source: PermissionSourceType0 | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.permission_source_type_0 import PermissionSourceType0 # noqa: PLC0415
        from ..models.session_permission_create_body_metadata import SessionPermissionCreateBodyMetadata # noqa: PLC0415
        action = self.action

        resources = self.resources



        agent: None | str | Unset
        if isinstance(self.agent, Unset):
            agent = UNSET
        else:
            agent = self.agent

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

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
            "resources": resources,
        })
        if agent is not UNSET:
            field_dict["agent"] = agent
        if id is not UNSET:
            field_dict["id"] = id
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if save is not UNSET:
            field_dict["save"] = save
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.permission_source_type_0 import PermissionSourceType0 # noqa: PLC0415
        from ..models.session_permission_create_body_metadata import SessionPermissionCreateBodyMetadata # noqa: PLC0415
        d = dict(src_dict)
        action = d.pop("action")

        resources = cast(list[str], d.pop("resources"))


        def _parse_agent(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        agent = _parse_agent(d.pop("agent", UNSET))


        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))


        _metadata = d.pop("metadata", UNSET)
        metadata: SessionPermissionCreateBodyMetadata | Unset
        if isinstance(_metadata,  Unset):
            metadata = UNSET
        else:
            metadata = SessionPermissionCreateBodyMetadata.from_dict(_metadata)




        save = cast(list[str], d.pop("save", UNSET))


        def _parse_source(data: object) -> PermissionSourceType0 | Unset:
            if isinstance(data, Unset):
                return data
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_permission_source_type_0 = PermissionSourceType0.from_dict(data)



            return componentsschemas_permission_source_type_0

        source = _parse_source(d.pop("source", UNSET))


        session_permission_create_body = cls(
            action=action,
            resources=resources,
            agent=agent,
            id=id,
            metadata=metadata,
            save=save,
            source=source,
        )

        return session_permission_create_body

