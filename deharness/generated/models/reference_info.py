from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.reference_git_source import ReferenceGitSource
  from ..models.reference_local_source import ReferenceLocalSource





T = TypeVar("T", bound="ReferenceInfo")



@_attrs_define
class ReferenceInfo:
    """ 
        Attributes:
            name (str):
            path (str):
            source (ReferenceGitSource | ReferenceLocalSource):
            description (str | Unset):
            hidden (bool | Unset):
     """

    name: str
    path: str
    source: ReferenceGitSource | ReferenceLocalSource
    description: str | Unset = UNSET
    hidden: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.reference_git_source import ReferenceGitSource # noqa: PLC0415
        from ..models.reference_local_source import ReferenceLocalSource # noqa: PLC0415
        name = self.name

        path = self.path

        source: dict[str, Any]
        if isinstance(self.source, ReferenceLocalSource):
            source = self.source.to_dict()
        else:
            source = self.source.to_dict()


        description = self.description

        hidden = self.hidden


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "name": name,
            "path": path,
            "source": source,
        })
        if description is not UNSET:
            field_dict["description"] = description
        if hidden is not UNSET:
            field_dict["hidden"] = hidden

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reference_git_source import ReferenceGitSource # noqa: PLC0415
        from ..models.reference_local_source import ReferenceLocalSource # noqa: PLC0415
        d = dict(src_dict)
        name = d.pop("name")

        path = d.pop("path")

        def _parse_source(data: object) -> ReferenceGitSource | ReferenceLocalSource:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_reference_source_type_0 = ReferenceLocalSource.from_dict(data)



                return componentsschemas_reference_source_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_reference_source_type_1 = ReferenceGitSource.from_dict(data)



            return componentsschemas_reference_source_type_1

        source = _parse_source(d.pop("source"))


        description = d.pop("description", UNSET)

        hidden = d.pop("hidden", UNSET)

        reference_info = cls(
            name=name,
            path=path,
            source=source,
            description=description,
            hidden=hidden,
        )

        return reference_info

