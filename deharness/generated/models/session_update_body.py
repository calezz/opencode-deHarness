from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.permission_rule import PermissionRule
  from ..models.session_metadata import SessionMetadata





T = TypeVar("T", bound="SessionUpdateBody")



@_attrs_define
class SessionUpdateBody:
    """ 
        Attributes:
            metadata (None | SessionMetadata | Unset):
            permissions (list[PermissionRule] | None | Unset):
            title (None | str | Unset):
     """

    metadata: None | SessionMetadata | Unset = UNSET
    permissions: list[PermissionRule] | None | Unset = UNSET
    title: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.permission_rule import PermissionRule # noqa: PLC0415
        from ..models.session_metadata import SessionMetadata # noqa: PLC0415
        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, SessionMetadata):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

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
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if permissions is not UNSET:
            field_dict["permissions"] = permissions
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.permission_rule import PermissionRule # noqa: PLC0415
        from ..models.session_metadata import SessionMetadata # noqa: PLC0415
        d = dict(src_dict)
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


        session_update_body = cls(
            metadata=metadata,
            permissions=permissions,
            title=title,
        )

        return session_update_body

