from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.skill_not_found_error_encoded_tag import SkillNotFoundErrorEncodedTag






T = TypeVar("T", bound="SkillNotFoundErrorEncoded")



@_attrs_define
class SkillNotFoundErrorEncoded:
    """ 
        Attributes:
            field_tag (SkillNotFoundErrorEncodedTag):
            message (str):
            skill (str):
     """

    field_tag: SkillNotFoundErrorEncodedTag
    message: str
    skill: str





    def to_dict(self) -> dict[str, Any]:
        field_tag = self.field_tag.value

        message = self.message

        skill = self.skill


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "_tag": field_tag,
            "message": message,
            "skill": skill,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_tag = SkillNotFoundErrorEncodedTag(d.pop("_tag"))




        message = d.pop("message")

        skill = d.pop("skill")

        skill_not_found_error_encoded = cls(
            field_tag=field_tag,
            message=message,
            skill=skill,
        )

        return skill_not_found_error_encoded

