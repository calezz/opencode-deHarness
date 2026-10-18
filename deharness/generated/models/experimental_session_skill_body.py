from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ExperimentalSessionSkillBody")



@_attrs_define
class ExperimentalSessionSkillBody:
    """ 
        Attributes:
            id (str):
            resume (bool | None | Unset):
     """

    id: str
    resume: bool | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        resume: bool | None | Unset
        if isinstance(self.resume, Unset):
            resume = UNSET
        else:
            resume = self.resume


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
        })
        if resume is not UNSET:
            field_dict["resume"] = resume

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_resume(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        resume = _parse_resume(d.pop("resume", UNSET))


        experimental_session_skill_body = cls(
            id=id,
            resume=resume,
        )

        return experimental_session_skill_body

