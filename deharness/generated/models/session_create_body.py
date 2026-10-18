from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.location_public_ref import LocationPublicRef
  from ..models.model_ref import ModelRef
  from ..models.permission_rule import PermissionRule
  from ..models.session_metadata import SessionMetadata





T = TypeVar("T", bound="SessionCreateBody")



@_attrs_define
class SessionCreateBody:
    """ 
        Attributes:
            agent (None | str | Unset):
            id (None | str | Unset):
            location (LocationPublicRef | None | Unset):
            metadata (None | SessionMetadata | Unset):
            model (ModelRef | None | Unset):
            parent_id (None | str | Unset):
            permissions (list[PermissionRule] | None | Unset):
            title (None | str | Unset):
     """

    agent: None | str | Unset = UNSET
    id: None | str | Unset = UNSET
    location: LocationPublicRef | None | Unset = UNSET
    metadata: None | SessionMetadata | Unset = UNSET
    model: ModelRef | None | Unset = UNSET
    parent_id: None | str | Unset = UNSET
    permissions: list[PermissionRule] | None | Unset = UNSET
    title: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.location_public_ref import LocationPublicRef # noqa: PLC0415
        from ..models.model_ref import ModelRef # noqa: PLC0415
        from ..models.permission_rule import PermissionRule # noqa: PLC0415
        from ..models.session_metadata import SessionMetadata # noqa: PLC0415
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

        location: dict[str, Any] | None | Unset
        if isinstance(self.location, Unset):
            location = UNSET
        elif isinstance(self.location, LocationPublicRef):
            location = self.location.to_dict()
        else:
            location = self.location

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, SessionMetadata):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        model: dict[str, Any] | None | Unset
        if isinstance(self.model, Unset):
            model = UNSET
        elif isinstance(self.model, ModelRef):
            model = self.model.to_dict()
        else:
            model = self.model

        parent_id: None | str | Unset
        if isinstance(self.parent_id, Unset):
            parent_id = UNSET
        else:
            parent_id = self.parent_id

        permissions: list[dict[str, Any]] | None | Unset
        if isinstance(self.permissions, Unset):
            permissions = UNSET
        elif isinstance(self.permissions, list):
            permissions = []
            for componentsschemas_permission_ruleset_item_data in self.permissions:
                componentsschemas_permission_ruleset_item = componentsschemas_permission_ruleset_item_data.to_dict()
                permissions.append(componentsschemas_permission_ruleset_item)


        else:
            permissions = self.permissions

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if agent is not UNSET:
            field_dict["agent"] = agent
        if id is not UNSET:
            field_dict["id"] = id
        if location is not UNSET:
            field_dict["location"] = location
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if model is not UNSET:
            field_dict["model"] = model
        if parent_id is not UNSET:
            field_dict["parentID"] = parent_id
        if permissions is not UNSET:
            field_dict["permissions"] = permissions
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.location_public_ref import LocationPublicRef # noqa: PLC0415
        from ..models.model_ref import ModelRef # noqa: PLC0415
        from ..models.permission_rule import PermissionRule # noqa: PLC0415
        from ..models.session_metadata import SessionMetadata # noqa: PLC0415
        d = dict(src_dict)
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


        def _parse_location(data: object) -> LocationPublicRef | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                location_type_0 = LocationPublicRef.from_dict(data)



                return location_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LocationPublicRef | None | Unset, data)

        location = _parse_location(d.pop("location", UNSET))


        def _parse_metadata(data: object) -> None | SessionMetadata | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = SessionMetadata.from_dict(data)



                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SessionMetadata | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))


        def _parse_model(data: object) -> ModelRef | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                model_type_0 = ModelRef.from_dict(data)



                return model_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ModelRef | None | Unset, data)

        model = _parse_model(d.pop("model", UNSET))


        def _parse_parent_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parent_id = _parse_parent_id(d.pop("parentID", UNSET))


        def _parse_permissions(data: object) -> list[PermissionRule] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                permissions_type_0 = []
                _permissions_type_0 = data
                for componentsschemas_permission_ruleset_item_data in (_permissions_type_0):
                    componentsschemas_permission_ruleset_item = PermissionRule.from_dict(componentsschemas_permission_ruleset_item_data)



                    permissions_type_0.append(componentsschemas_permission_ruleset_item)

                return permissions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PermissionRule] | None | Unset, data)

        permissions = _parse_permissions(d.pop("permissions", UNSET))


        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))


        session_create_body = cls(
            agent=agent,
            id=id,
            location=location,
            metadata=metadata,
            model=model,
            parent_id=parent_id,
            permissions=permissions,
            title=title,
        )

        return session_create_body

