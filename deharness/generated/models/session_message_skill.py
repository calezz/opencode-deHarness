from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.session_message_skill_type import SessionMessageSkillType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.session_message_skill_metadata import SessionMessageSkillMetadata
  from ..models.session_message_skill_time import SessionMessageSkillTime





T = TypeVar("T", bound="SessionMessageSkill")



@_attrs_define
class SessionMessageSkill:
    """ 
        Attributes:
            id (str):
            name (str):
            skill (str):
            text (str):
            time (SessionMessageSkillTime):
            type_ (SessionMessageSkillType):
            metadata (SessionMessageSkillMetadata | Unset):
     """

    id: str
    name: str
    skill: str
    text: str
    time: SessionMessageSkillTime
    type_: SessionMessageSkillType
    metadata: SessionMessageSkillMetadata | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.session_message_skill_metadata import SessionMessageSkillMetadata # noqa: PLC0415
        from ..models.session_message_skill_time import SessionMessageSkillTime # noqa: PLC0415
        id = self.id

        name = self.name

        skill = self.skill

        text = self.text

        time = self.time.to_dict()

        type_ = self.type_.value

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "name": name,
            "skill": skill,
            "text": text,
            "time": time,
            "type": type_,
        })
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.session_message_skill_metadata import SessionMessageSkillMetadata # noqa: PLC0415
        from ..models.session_message_skill_time import SessionMessageSkillTime # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        skill = d.pop("skill")

        text = d.pop("text")

        time = SessionMessageSkillTime.from_dict(d.pop("time"))




        type_ = SessionMessageSkillType(d.pop("type"))




        _metadata = d.pop("metadata", UNSET)
        metadata: SessionMessageSkillMetadata | Unset
        if isinstance(_metadata,  Unset):
            metadata = UNSET
        else:
            metadata = SessionMessageSkillMetadata.from_dict(_metadata)




        session_message_skill = cls(
            id=id,
            name=name,
            skill=skill,
            text=text,
            time=time,
            type_=type_,
            metadata=metadata,
        )

        return session_message_skill

