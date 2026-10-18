from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.project_not_found_error_encoded_tag import ProjectNotFoundErrorEncodedTag






T = TypeVar("T", bound="ProjectNotFoundErrorEncoded")



@_attrs_define
class ProjectNotFoundErrorEncoded:
    """ 
        Attributes:
            field_tag (ProjectNotFoundErrorEncodedTag):
            message (str):
            project_id (str):
     """

    field_tag: ProjectNotFoundErrorEncodedTag
    message: str
    project_id: str





    def to_dict(self) -> dict[str, Any]:
        field_tag = self.field_tag.value

        message = self.message

        project_id = self.project_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "_tag": field_tag,
            "message": message,
            "projectID": project_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_tag = ProjectNotFoundErrorEncodedTag(d.pop("_tag"))




        message = d.pop("message")

        project_id = d.pop("projectID")

        project_not_found_error_encoded = cls(
            field_tag=field_tag,
            message=message,
            project_id=project_id,
        )

        return project_not_found_error_encoded

