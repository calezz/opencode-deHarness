from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.location_public_info_project import LocationPublicInfoProject





T = TypeVar("T", bound="LocationPublicInfo")



@_attrs_define
class LocationPublicInfo:
    """ 
        Attributes:
            directory (str):
            project (LocationPublicInfoProject):
     """

    directory: str
    project: LocationPublicInfoProject





    def to_dict(self) -> dict[str, Any]:
        from ..models.location_public_info_project import LocationPublicInfoProject # noqa: PLC0415
        directory = self.directory

        project = self.project.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "directory": directory,
            "project": project,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.location_public_info_project import LocationPublicInfoProject # noqa: PLC0415
        d = dict(src_dict)
        directory = d.pop("directory")

        project = LocationPublicInfoProject.from_dict(d.pop("project"))




        location_public_info = cls(
            directory=directory,
            project=project,
        )

        return location_public_info

