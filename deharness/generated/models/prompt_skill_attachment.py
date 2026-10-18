from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.prompt_mention import PromptMention





T = TypeVar("T", bound="PromptSkillAttachment")



@_attrs_define
class PromptSkillAttachment:
    """ 
        Attributes:
            id (str):
            name (str):
            mention (PromptMention | Unset):
            text (str | Unset):
     """

    id: str
    name: str
    mention: PromptMention | Unset = UNSET
    text: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.prompt_mention import PromptMention # noqa: PLC0415
        id = self.id

        name = self.name

        mention: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mention, Unset):
            mention = self.mention.to_dict()

        text = self.text


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "name": name,
        })
        if mention is not UNSET:
            field_dict["mention"] = mention
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.prompt_mention import PromptMention # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        _mention = d.pop("mention", UNSET)
        mention: PromptMention | Unset
        if isinstance(_mention,  Unset):
            mention = UNSET
        else:
            mention = PromptMention.from_dict(_mention)




        text = d.pop("text", UNSET)

        prompt_skill_attachment = cls(
            id=id,
            name=name,
            mention=mention,
            text=text,
        )

        return prompt_skill_attachment

